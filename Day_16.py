from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

map = []
for line in file:
    map.append(line.strip())



DIR = [0, 1, 0, -1, 0]
facing = ["r", "d", "l", "u"]


def evaluate_p1(start, end, map):
    vis = defaultdict(lambda : math.inf)
    pq = [(0, start[0], start[1], facing[0])]
    vis[(start)] = 0

    while pq:
        score, i, j, direction = heappop(pq)
        for k in range(4):
            x, y = i + DIR[k], j + DIR[k + 1]
            new_dir = facing[k]
            if map[(x, y)] == ".":
                if direction == new_dir:
                    new_score = score + 1
                else:
                    if direction == "r" and  new_dir == "l":
                        continue
                    if direction == "l" and  new_dir == "r":
                        continue
                    if direction == "u" and  new_dir == "d":
                        continue
                    if direction == "d" and  new_dir == "u":
                        continue
                    new_score = score + 1000 + 1
                if vis[((x,y))] > new_score:
                    vis[((x,y))] = new_score
                    heappush(pq, (new_score, x, y, new_dir))
            elif map[(x, y)] == "#":
                continue

    return vis[(end)]

def evaluate_p2(start, end, map, actual_acore):
    complete_path = set()
    vis = defaultdict(lambda : math.inf)
    pq = deque([(0, start[0], start[1], facing[0], {start})])
    vis[(start, facing[0])] = 0

    while pq:
        score, i, j, direction, path = (pq).popleft()
        if i == 7 and j == 6:
            print(score, "hey")
        if (i, j) == end and score == actual_acore:
            complete_path |= path
            continue

        for k in range(4):
            x, y = i + DIR[k], j + DIR[k + 1]
            new_dir = facing[k]
            if map[(x, y)] == ".":
                if direction == new_dir:
                    new_score = score + 1
                else:
                    if direction == "r" and  new_dir == "l":
                        continue
                    if direction == "l" and  new_dir == "r":
                        continue
                    if direction == "u" and  new_dir == "d":
                        continue
                    if direction == "d" and  new_dir == "u":
                        continue
                    new_score = score + 1000 + 1
                if vis[((x,y), new_dir)] >= new_score:
                    vis[((x,y), new_dir)] = new_score
                    pq.append((new_score, x, y, new_dir, path | {(x, y)}))
            elif map[(x, y)] == "#":
                continue

    return len(complete_path)


def solve(part, map):
    new_map = defaultdict(str)
    start = None
    end = None
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            new_map[(i,j)] = char
            if char == "S":
                start = (i, j)
                new_map[(i,j)] = "."
            elif char == "E":
                end = (i, j)
                new_map[(i,j)] = "."
    if part:
        ans = evaluate_p1(start, end, new_map)
        print(ans)
    else:
        ans = evaluate_p2(start, end, new_map, evaluate_p1(start, end, new_map))
        print(ans)

# part 1
solve(True, map)
# part 2
solve(False, map)
