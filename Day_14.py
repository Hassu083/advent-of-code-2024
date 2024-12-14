from collections import Counter, defaultdict, deque
import math
import sys
import time 

sys.setrecursionlimit(10**6)

file = open("input.txt")

positions = []
for line in file:
    pos, vel = line.split(" ")
    positions.append([list(map(int, pos[2:].split(","))), list(map(int, vel[2:].split(",")))])


# DIR = [0, 1, 0, -1, 0]
# DIR2 = [1,-1,-1,1,1]
# facing = ["r", "d", "l", "u"]


def useful_function(quadrant):
    m, n = len(quadrant), len(quadrant[0])
    missX, missy = m//2, n//2
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(m):
        for j in range(n):
            if i == missX or j == missy: continue
            elif i < missX and j < missy:
                q1 += quadrant[i][j]
            elif i > missX and j < missy:
                q2 += quadrant[i][j]
            elif i < missX and j > missy:
                q3 += quadrant[i][j]
            else:
                q4 += quadrant[i][j]
    return q1 * q2 * q3 * q4
            



def evaluate_p1(pos, vel, second, quadrant):
    m, n = len(quadrant), len(quadrant[0])
    x, y = pos
    vx, vy = vel
    for _ in range(second):
        x = (x + vx)%m
        y = (y + vy)%n
    quadrant[x][y] += 1 




def evaluate_p2(positions, quadrant):
    m, n = len(quadrant), len(quadrant[0])
    for i, [pos, vel] in enumerate(positions):
        x, y = pos
        vx, vy = vel
        x = (x + vx)%m
        y = (y + vy)%n
        positions[i][0] = [x, y]
        quadrant[x][y] += 1





def solve(part, positions):

    if part:
        quadrant = [[0]*103 for _ in range(101)]
        for pos, vel in positions:
            evaluate_p1(pos, vel, 100, quadrant)
        print(useful_function(quadrant))
    else:
        for second in range(10000):
            quadrant = [[0]*103 for _ in range(101)]
            evaluate_p2(positions, quadrant)
            for row in quadrant:
                for col in row:
                    if col > 1:
                        break
                else:
                    continue
                break
            else:
                print(second+1)

# part 1
solve(True, positions)
# part 2
solve(False, positions)
