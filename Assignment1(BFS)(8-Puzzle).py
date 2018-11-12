import queue
import copy


class State:
    def __init__(self, st):
        self.state = st
        self.parent = None


class Stack:
    def __init__(self):
        self.item = []

    def push(self, items):
        self.item.insert(0, items)

    def peek(self):
        return self.item[0]

    def pop(self):
        return self.item.pop()

    def empty(self):
        return self.item == []


def is_valid_init(p):
    for row in range(3):
        for col in range(3):
            if p[row][col] > 9 or p[row][col] < 1:
                return False
    return True


def move_up(p):
    for row in range(2):
        for col in range(3):
            if p[row+1][col] == 9:
                a = p[row+1][col]
                p[row+1][col] = p[row][col]
                p[row][col] = a
                return p


def move_right(p):
        for row in range(3):
            for col in range(2):
                if p[row][col] == 9:
                    a = p[row][col]
                    p[row][col] = p[row][col+1]
                    p[row][col+1] = a
                    return p


def move_down(p):
    for row in range(2):
        for col in range(3):
            if p[row][col] == 9:
                a = p[row][col]
                p[row][col] = p[row+1][col]
                p[row+1][col] = a
                return p


def move_left(p):
    for row in range(3):
        for col in range(2):
            if p[row][col+1] == 9:
                a = p[row][col]
                p[row][col] = p[row][col+1]
                p[row][col+1] = a
                return p


def is_valid_move(p, ch):
    if ch == "u":
        if p[0][0] == 9 or p[0][1] == 9 or p[0][2] == 9:
            return False
        else:
            return move_up(copy.deepcopy(p))
    if ch == "r":
        if p[0][2] == 9 or p[1][2] == 9 or p[2][2] == 9:
            return False
        else:
            return move_right(copy.deepcopy(p))
    if ch == "d":
        if p[2][0] == 9 or p[2][1] == 9 or p[2][2] == 9:
            return False
        else:
            return move_down(copy.deepcopy(p))
    if ch == "l":
        if p[0][0] == 9 or p[1][0] == 9 or p[2][0] == 9:
            return False
        else:
            return move_left(copy.deepcopy(p))


def is_win(board):
    i = 1
    for R in range(3):
        for C in range(3):
            if board[R][C] != i:
                return False
            i += 1
    return True


def in_explored(state, explored):
    if explored.count(state) > 0:
        return True
    else:
        return False


def copy_queue(src, des):
    x = src.qsize()
    for y in range(x):
        temp = src.get()
        des.put(temp)
        src.put(temp)


def in_frontier(state, frontier):
    temp = queue.Queue()
    copy_queue(frontier, temp)
    while not temp.empty():
        st = temp.get()
        if state == st:
            return True
    return False


def bfs(puzzle):
    frontier = queue.Queue()
    explored = []
    ans = []
    if is_win(puzzle.state) and frontier.empty():
        return puzzle
    frontier.put(puzzle)
    while not is_win(puzzle.state):
        if frontier.empty():
            return None
        p = frontier.get()
        explored.append(p.state)
        up = State(is_valid_move(copy.deepcopy(p.state), "u"))
        up.parent = p
        rp = State(is_valid_move(copy.deepcopy(p.state), "r"))
        rp.parent = p
        dp = State(is_valid_move(copy.deepcopy(p.state), "d"))
        dp.parent = p
        lp = State(is_valid_move(copy.deepcopy(p.state), "l"))
        lp.parent = p
        if up.state:
            if not in_explored(up.state, explored):
                if not in_frontier(up.state, frontier):
                    if is_win(up.state):
                        return up
                    else:
                        frontier.put(up)
        if rp.state:
            if not in_explored(rp.state, explored):
                if not in_frontier(rp.state, frontier):
                    if is_win(rp.state):
                        return rp
                    else:
                        frontier.put(rp)
        if dp.state:
            if not in_explored(dp.state, explored):
                if not in_frontier(dp.state, frontier):
                    if is_win(dp.state):
                        return dp
                    else:
                        frontier.put(dp)
        if lp.state:
            if not in_explored(lp.state, explored):
                if not in_frontier(lp.state, frontier):
                    if is_win(lp.state):
                        return lp
                    else:
                        frontier.put(lp)
    return ans


def print_answer(ans):
    s = Stack()
    while ans is not None:
        s.push(ans.state)
        ans = ans.parent
    while not s.empty():
        print(s.pop())


InitPuzzle = [[1, 2, 3], [4, 9, 6], [7, 5, 8]]
while not is_valid_init(InitPuzzle):

    for b in range(3):
        for c in range(3):
            print("Input values in", b+1, " row ", c+1, " column (for space enter 9): ")
            InitPuzzle[b][c] = int(input())
init = State(copy.deepcopy(InitPuzzle))
init.parent = None
answer = bfs(init)
print_answer(answer)

