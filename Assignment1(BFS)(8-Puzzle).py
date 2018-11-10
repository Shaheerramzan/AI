def init():
    p = [[], [], []]
    f = open("Puzzle.txt", "r")
    for x in range(3):
        p[x] = f.readline()

    return p


Puzzle = init()

print(Puzzle)
a = Puzzle[0][0]
Puzzle[0][0] = Puzzle[1][1]
Puzzle[1][1] = a
print(Puzzle)
