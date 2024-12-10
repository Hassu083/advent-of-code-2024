from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")
map = []
for line in file:
    map.append(line.strip())

DIR = [0, 1, 0, -1, 0]

def valid(i, j, m, n):
    return 0<=i<m and 0<=j<n


def evaluate_p1(i, j, m, n, map, vis):
    if int(map[i][j]) == 9:
        return 1
    ans = 0
    for k in range(4):
        x, y = i + DIR[k], j + DIR[k+1]
        if valid(x, y, m, n) and (x,y) not in vis:
            if int(map[i][j])+1 == int(map[x][y]):
                vis.add((x, y))
                ans += evaluate_p1(x, y, m, n, map, vis)
    return ans



def evaluate_p2(i, j, m, n, map):
    if int(map[i][j]) == 9:
        return 1
    ans = 0
    for k in range(4):
        x, y = i + DIR[k], j + DIR[k+1]
        if valid(x, y, m, n):
            if int(map[i][j])+1 == int(map[x][y]):
                ans += evaluate_p2(x, y, m, n, map)
    return ans




def solve(part, map):
    m, n = len(map), len(map[0])
    if part:
        ans = 0
        for i, line in enumerate(map):
            for j, char in enumerate(line):
                if char == "0":
                    vis = set()
                    ans += evaluate_p1(i, j, m, n, map, vis)
        print(ans)
    else:
        ans = 0
        for i, line in enumerate(map):
            for j, char in enumerate(line):
                if char == "0":
                    vis = set()
                    ans += evaluate_p2(i, j, m, n, map)
        print(ans)

# part 1
solve(True, map)
# part 2
solve(False, map)
