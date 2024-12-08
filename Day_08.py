from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")
locations = defaultdict(set)

map = []
for line in file:
    map.append(line.strip())

def validate(loc, m, n):
    x, y = loc
    return 0 <= x < m and 0 <= y < n 


def evaluate_p1(map, locations, rows, cols, vis):
    n = len(locations)
    ans = 0
    for i, loc in enumerate(locations):
        for j in range(i+1, n):
            x1, y1 = locations[i]
            x2, y2 = locations[j]
            dx, dy = abs(x2-x1), abs(y2-y1)
            if x1 <= x2 and y1 <= y2:
                newloc1 = (x1-dx, y1-dy)
                newloc2 = (x2+dx, y2+dy)
                if validate(newloc1, rows, cols) and newloc1 not in vis:
                    vis.add(newloc1)
                    ans += 1
                if validate(newloc2, rows, cols) and newloc2 not in vis:
                    vis.add(newloc2)
                    ans += 1

            elif x1 >= x2 and y1 >= y2:
                newloc1 = (x1+dx, y1+dy)
                newloc2 = (x2-dx, y2-dy)
                if validate(newloc1, rows, cols) and newloc1 not in vis:
                    vis.add(newloc1)
                    ans += 1
                if validate(newloc2, rows, cols) and newloc2 not in vis:
                    vis.add(newloc2)
                    ans += 1

            elif x1 >= x2 and y1 <= y2:
                newloc1 = (x1+dx, y1-dy)
                newloc2 = (x2-dx, y2+dy)
                if validate(newloc1, rows, cols) and newloc1 not in vis:
                    vis.add(newloc1)
                    ans += 1
                if validate(newloc2, rows, cols) and newloc2 not in vis:
                    vis.add(newloc2)
                    ans += 1
            
            elif x1 <= x2 and y1 >= y2:
                newloc1 = (x1-dx, y1+dy)
                newloc2 = (x2+dx, y2-dy)
                if validate(newloc1, rows, cols) and newloc1 not in vis:
                    vis.add(newloc1)
                    ans += 1
                if validate(newloc2, rows, cols) and newloc2 not in vis:
                    vis.add(newloc2)
                    ans += 1
           

    return ans



def evaluate_p2(map, locations, rows, cols, vis):
    n = len(locations)
    ans = 0
    for i, loc in enumerate(locations):
        for j in range(i+1, n):
            x1, y1 = locations[i]
            x2, y2 = locations[j]
            if locations[j] not in vis:
                vis.add(locations[j])
                ans += 1
            if locations[i] not in vis:
                vis.add(locations[i])
                ans += 1
            dx, dy = abs(x2-x1), abs(y2-y1)
            
            if x1 <= x2 and y1 <= y2:
                newloc1 = (x1-dx, y1-dy)
                newloc2 = (x2+dx, y2+dy)

                while validate(newloc1, rows, cols): 
                    if newloc1 not in vis:
                        vis.add(newloc1)
                        ans += 1
                    x1, y1 = newloc1
                    newloc1 = (x1-dx, y1-dy)

                while validate(newloc2, rows, cols): 
                    if newloc2 not in vis:
                        vis.add(newloc2)
                        ans += 1
                    x2, y2 = newloc2
                    newloc2 = (x2+dx, y2+dy)

            elif x1 >= x2 and y1 >= y2:
                newloc1 = (x1+dx, y1+dy)
                newloc2 = (x2-dx, y2-dy)

                while validate(newloc1, rows, cols): 
                    if newloc1 not in vis:
                        vis.add(newloc1)
                        ans += 1
                    x1, y1 = newloc1
                    newloc1 = (x1+dx, y1+dy)

                while validate(newloc2, rows, cols): 
                    if newloc2 not in vis:
                        vis.add(newloc2)
                        ans += 1
                    x2, y2 = newloc2
                    newloc2 = (x2-dx, y2-dy)

            elif x1 >= x2 and y1 <= y2:
                newloc1 = (x1+dx, y1-dy)
                newloc2 = (x2-dx, y2+dy)
 
                while validate(newloc1, rows, cols): 
                    if newloc1 not in vis:
                        vis.add(newloc1)
                        ans += 1
                    x1, y1 = newloc1
                    newloc1 = (x1+dx, y1-dy)

                while validate(newloc2, rows, cols): 
                    if newloc2 not in vis:
                        vis.add(newloc2)
                        ans += 1
                    x2, y2 = newloc2
                    newloc2 = (x2-dx, y2+dy)
            
            elif x1 <= x2 and y1 >= y2:
                newloc1 = (x1-dx, y1+dy)
                newloc2 = (x2+dx, y2-dy)

                while validate(newloc1, rows, cols): 
                    if newloc1 not in vis:
                        vis.add(newloc1)
                        ans += 1
                    x1, y1 = newloc1
                    newloc1 = (x1-dx, y1+dy)

                while validate(newloc2, rows, cols): 
                    if newloc2 not in vis:
                        vis.add(newloc2)
                        ans += 1
                    x2, y2 = newloc2
                    newloc2 = (x2+dx, y2-dy)
           

    return ans




def solve(part, map):
    m, n = len(map), len(map[0])
    locations = defaultdict(list)
    for i in range(m):
        for j in range(n):
            locations[map[i][j]].append((i,j))
        
    if part:
        ans = 0
        vis = set()
        for key in locations:
            if key == ".": continue
            ans += evaluate_p1(map, locations[key], m, n, vis)
        print(ans)
    else:
        ans = 0
        vis = set()
        for key in locations:
            if key == ".": continue
            ans += evaluate_p2(map, locations[key], m, n, vis)
        print(ans)

# part 1
solve(True, map)
# part 2
solve(False, map)
