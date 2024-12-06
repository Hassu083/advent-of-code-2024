from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")
mmap = []
for line in file:
    mmap.append(line.strip())
n = len(mmap[0])
m = len(mmap)
vis = [[False]*n for _ in range(m)]

def path_before_leave(i, j, direction, map, vis, extra = None):
    visited_pairs = set()

    while not (i >= m or j >= n or i < 0 or j < 0):
        if ((i,j), direction) in visited_pairs:
            break
        visited_pairs.add(((i,j), direction) )
        if map[i][j] == "#" or (i,j) == extra:
            match(direction):
                case "u":
                    direction = "r"
                    i += 1
                case "d":
                    direction = "l"
                    i -= 1
                case "l":
                    direction = "u"
                    j += 1
                case "r":
                    direction = "d"
                    j -= 1
        vis.add((i,j))

        match(direction):
            case "u":
                i -= 1
            case "d":
                i += 1
            case "l":
                j -= 1
            case "r":
                j += 1
    else:
        return vis
    return True





def solve(part,map):
    if part:
        vis = set()
        for i in range(m):
            for j in range(n):
                if map[i][j] == "^":
                    path_before_leave(i, j, 'u', map, vis)
                    break
            else:
                continue
            break  
        print(len(vis))
    else:
        vis = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if map[i][j] == "^":
                    path_before_leave(i, j, 'u', map, vis)
                    break
            else:
                continue
            break  
        path = vis
        for (x, y) in path:
            vis = set()
            if path_before_leave(i, j, 'u', map, vis, extra = (x, y)) == True:
                ans += 1
        print(ans)

# part 1
solve(True, mmap)
# part 2
solve(False, mmap)
