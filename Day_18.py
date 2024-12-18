from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

co_ordinates = []
for line in file:
    y, x = map(int, line.split(","))
    co_ordinates.append((x, y))

DIR = [0, 1, 0, -1, 0]
# DIR2 = [1,-1,-1,1,1]
# facing = ["r", "d", "l", "u"]


def useful_function():
    pass


def evaluate_p1(memory, n):
    ans = 0
    q = deque([(0,0)])
    vis = {(0, 0)}
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == n-1 and j == n-1:
                return ans
            for k in range(4):
                x, y = i + DIR[k], j + DIR[k + 1]
                if memory[(x, y)] == "." and (x, y) not in vis:
                    vis.add((x, y))
                    q.append((x, y))
        ans += 1
    return -1


def evaluate_p2(memory, n, index, co_ordinates):
    for co in co_ordinates[:index + 1]:
        memory[co] = "#"
    return evaluate_p1(memory, n)






def solve(part, co_ordinates):
    n = 71
    memory = defaultdict(str)
    for i in range(n):
        for j in range(n):
            memory[(i, j)] = "."
    if part:
        memory_p1 = memory.copy()
        for i in range(1024):
            memory_p1[co_ordinates[i]] = "#"
        ans = evaluate_p1(memory_p1, n)
        print(ans)
    else:
        ans = None
        left, right = 0, len(co_ordinates)-1
        while left <= right:
            mid = (left + right) >> 1
            if evaluate_p2(memory.copy(), n, mid, co_ordinates) != -1:
                left = mid + 1
            else:
                ans = co_ordinates[mid]
                right = mid - 1
        print(ans[1],ans[0])

# part 1
solve(True, co_ordinates)
# part 2
solve(False, co_ordinates)
