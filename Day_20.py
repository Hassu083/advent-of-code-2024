from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

map = []
for line in file:
    map.append(list(line.strip()))
m, n = len(map), len(map[0])

DIR = [0, 1, 0, -1, 0]


def traverse(i, j, distance, p_i, p_j, map, e_i, e_j):
    map[i][j] = distance
    if i == e_i and j == e_j:
        return 
    for k in range(4):
        x, y = i+DIR[k], j+DIR[k+1]
        if 0 <= x < m  and 0 <= y < n  and (x,y) != (p_i,p_j) and map[x][y] != "#":
            traverse(x, y, distance+1, i, j, map, e_i, e_j)

def evaluate_p1(i, j):
    mn, mx = math.inf, -math.inf
    for k in range(4):
        x, y = i+DIR[k], j+DIR[k+1]
        if type(map[x][y]) == int:
            mx = max(mx, map[x][y])
            mn = min(mn, map[x][y])
    if mx == -math.inf or mn == math.inf or mx - mn == 0:
        return 0
    return mx - mn - 2



def evaluate_p2(i, j, count, v):
    start = (i, j)
    distance = 0
    q = deque([start])
    vis = {start}
    for _ in range(20):
        if not q: break
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                x, y = i+DIR[k], j+DIR[k+1]
                if 0 <= x < m  and 0 <= y < n:
                    if (x,y) not in vis:
                        if map[x][y] != "#":
                            end = (x, y)
                            if (map[end[0]][end[1]]-map[start[0]][start[1]]-distance -1)>0 and (start, end) not in v:
                                v.add((start, end))
                                v.add((end, start))
                                count[map[end[0]][end[1]]-map[start[0]][start[1]]-distance -1] += 1
                        vis.add((x, y))
                        q.append((x, y))
        distance += 1




def solve(part, map):

    if part:
        start = None 
        walls = set()
        end = None
        for i in range(m):
            for j in range(n):
                if map[i][j] == "S":
                    start = (i, j)
                if map[i][j] == "E":
                    end = (i, j)
                if map[i][j] == "#":
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        continue
                    walls.add((i, j)) 
        traverse(start[0], start[1], 0, -1, -1, map, end[0], end[1])
        for i in range(m):
            for j in range(n):
                if map[i][j] == ".":
                    map[i][j] = math.inf
        ans = 0
        count = defaultdict(int)
        for i,j in walls:
            count[evaluate_p1(i, j)] += 1
        for key in count.keys():
            if key >= 100:
                ans += count[key]
        print(ans)
    else:
        ans = 0
        ans = 0
        count = defaultdict(int)
        v = set()
        for i in range(m):
            for j in range(n):
                if type(map[i][j]) == int:
                    evaluate_p2(i, j, count, v)
        for key in (count.keys()):
            if key >= 100:
                ans += count[key]
        print(ans)

# part 1
solve(True, map)
# part 2
solve(False, map)
