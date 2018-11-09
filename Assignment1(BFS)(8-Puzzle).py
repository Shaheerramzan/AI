
def init():
    p = [[]]
    f = open("Puzzle.txt", "r")
    for x in range(2):
        p[x] = f.readline()

    return p


Puzzle = init()
print(Puzzle)

