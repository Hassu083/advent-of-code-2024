from collections import Counter, defaultdict, deque
import math

file = open("input.txt")
order = True
for line in file:
    if line == "\n":
        order = False
        continue
    if order:
        a, b = list(map(int, line.split("|")))
    else:
        (list(map(int, line.split(","))))


def solve(part):
    if part:
        ans = 0       
        print(ans)
    else:
        ans = 0
        print(ans)



# part 1
solve(True)
# part 2
solve(False)
