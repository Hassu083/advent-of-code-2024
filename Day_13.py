from collections import Counter, defaultdict, deque
from sympy import symbols, Eq, solve
from sympy.abc import a, b
import numpy as np
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

buttons = []
inputs = file.read().strip().split("\n\n")
for input in inputs:
    A, B, C = input.strip().split("\n")
    _, _, X, Y = A.split(" ")
    _, _, X1, Y1 = B.split(" ")
    _, X2, Y2 = C.split(" ")
    buttons.append(
        [
            (int(X[2:-1].strip()), int(Y[2:].strip())),(int(X1[2:-1].strip()), int(Y1[2:].strip())),(int(X2[2:-1].strip()), int(Y2[2:].strip()))
        ]
    )




def evaluate_p1(ba_press, bb_press, buttonA, buttonB, result, memory):
    if ba_press > 100 or bb_press > 100:
        return math.inf
    if ba_press*buttonA[0] + bb_press*buttonB[0] > result[0] or ba_press*buttonA[1] + bb_press*buttonB[1] > result[1]:
        return math.inf
    if ba_press*buttonA[0] + bb_press*buttonB[0] == result[0] and ba_press*buttonA[1] + bb_press*buttonB[1] == result[1]:
        return 0
    if (ba_press,bb_press) in memory:
        return memory[(ba_press,bb_press)]
    memory[(ba_press,bb_press)] =  min(3+evaluate_p1(ba_press+1, bb_press, buttonA, buttonB, result, memory), 1+evaluate_p1(ba_press, bb_press+1, buttonA, buttonB, result, memory))
    return memory[(ba_press,bb_press)]



def evaluate_p2(buttonA, buttonB, result):
    ax, ay = buttonA
    bx, by = buttonB
    px, py = result
    px += 10000000000000
    py += 10000000000000
    m = (px * by - py * bx) // (ax * by - ay * bx)
    if m * (ax * by - ay * bx) != (px * by - py * bx):
        return math.inf
    n = (py - ay * m) // by
    if n * by != (py - ay * m):
        return math.inf
    return 3 * m + n




def solve(part, buttons):
    if part:
        ans = 0
        for buttonA, buttonB, result in buttons:
            memory = {}
            val = evaluate_p1(0, 0, buttonA, buttonB, result, memory)
            ans += val if val != math.inf else 0
        print(ans)
    else:
        ans = 0
        for buttonA, buttonB, result in buttons:
            val = evaluate_p2(buttonA, buttonB, result)
            print(val)
            ans += val if val != math.inf else 0
        print(ans)

# part 1
solve(True, buttons)
# part 2
solve(False, buttons)
