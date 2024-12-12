from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

region = []
for line in file:
    region.append(line.strip())



DIR = [0, 1, 0, -1, 0]

m = len(region)
n = len(region[0])

def valid(x, y):
    return 0<=x<m and 0<=y<n


def evaluate_p1(i, j, vis):
    ans = 0
    vis.add((i, j))
    for k in range(4):
        x, y = i+DIR[k], j+DIR[k+1]
        if not valid(x, y):
            ans += 1
            continue
        if region[x][y] != region[i][j]:
            ans += 1
            continue
        if (x, y) in vis:
            continue
        ans += evaluate_p1(x, y, vis)
    return ans



def dfs(i, j, vis):
    vis.add((i,j))
    for k in range(4):
        x, y = i+DIR[k], j+DIR[k+1]
        if not valid(x, y) or region[x][y] != region[i][j] or (x, y) in vis:
            continue
        dfs(x, y, vis)


def detect_edges(region):
    ans = 0
    min_i = min(i for i,_ in region)
    max_i = max(i for i,_ in region)
    min_j = min(j for _,j in region)
    max_j = max(j for _,j in region)

    top_edge_vis = set()
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if (i,j) in region and (i-1,j) not in region:
                if (i,j-1) not in top_edge_vis:
                    ans += 1
                top_edge_vis.add((i,j))
    topans = ans
    # print("top:", ans)
    bottom_edge_vis = set()
    for i in range(max_i, min_i-1, -1):
        for j in range(min_j, max_j+1):
            if (i,j) in region and (i+1,j) not in region:
                if (i,j-1) not in bottom_edge_vis:
                    ans += 1
                bottom_edge_vis.add((i,j))
    bottomans = ans
    # print("bottom:", ans-topans)
    left_edge_vis = set()
    for j in range(min_j, max_j+1):
        for i in range(max_i, min_i-1, -1):
            if (i, j) in region and (i, j-1) not in region:
                if (i+1, j) not in left_edge_vis:
                    ans += 1
                left_edge_vis.add((i,j))
    leftans = ans
    # print("left:", ans-bottomans)
    right_edge_vis = set()
    for j in range(max_j, min_j-1, -1):
        for i in range(min_i, max_i+1):
            if (i, j) in region and (i, j+1) not in region:
                if (i-1, j) not in right_edge_vis:
                    ans += 1
                right_edge_vis.add((i,j))
    # print("right:", ans-leftans)
    return ans





def solve(part, region):

    if part:
        ans = 0
        vis = set()
        for i, line in enumerate(region):
            for j, _ in enumerate(line):
                if (i, j) not in vis:
                    size_vis = len(vis)
                    perimeter = evaluate_p1(i, j, vis)
                    area = len(vis) - size_vis
                    ans += perimeter*area
        print(ans)
    else:
        ans = 0
        vis_comp = set()
        for i, line in enumerate(region):
            for j, _ in enumerate(line):
                if (i, j) not in vis_comp:
                    vis = set()
                    dfs(i, j, vis)
                    vis_comp |= vis
                    area = len(vis)
                    side = detect_edges(vis)
                    ans += side*area    
        print(ans)

# part 1
solve(True, region)
# part 2
solve(False, region)
