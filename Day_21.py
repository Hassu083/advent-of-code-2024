from collections import Counter, defaultdict, deque
import math
import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

file = open("input.txt")

pins = []
for line in file:
    pins.append(line.strip())

digit_to_pos = {
    "7" : (0, 0), "8" : (0, 1), "9" : (0, 2),
    "4" : (1, 0), "5" : (1, 1), "6" : (1, 2),
    "1" : (2, 0), "2" : (2, 1), "3" : (2, 2),
                  "0" : (3, 1), "A" : (3, 2),
}

direction_to_pos = {
                  "^" : (0, 1), "A" : (0, 2),
    "<" : (1, 0), "v" : (1, 1), ">" : (1, 2), 
}

@lru_cache(None)
def directional_to_directional(i, string, robots):
    q = deque([(direction_to_pos[string[i-1]], "")])
    ans = math.inf
    while q:

        (x, y), path = q.popleft()
        if (x, y) == direction_to_pos[string[i]]:
            if robots - 1 == 0:
                res = len(path) + 1
            else:
                res = directional_to_directional_top(path+"A", robots-1)
            ans = min(ans, res)
            continue

        if (x, y) != (0, 0):
            if direction_to_pos[string[i]][0] > x:
                q.append(((x + 1, y), path + "v"))
            elif direction_to_pos[string[i]][0] < x:
                q.append(((x - 1, y), path + "^"))
            if direction_to_pos[string[i]][1] > y:
                q.append(((x, y+1), path + ">"))
            elif direction_to_pos[string[i]][1] < y:
                q.append(((x, y-1), path + "<"))
    
    return ans

@lru_cache(None)
def directional_to_directional_top(string, robots):
    lenght = 0
    for i in range(len(string)):
        lenght += directional_to_directional(i, string, robots)
    return lenght

@lru_cache(None)
def numeric_to_directional(i, string, robots):

    q = deque([(digit_to_pos[string[i-1]], "")])
    ans = math.inf
    while q:

        (x, y), path = q.popleft()
        if (x, y) == digit_to_pos[string[i]]:
            res = directional_to_directional_top(path+"A", robots)
            ans = min(ans, res)
            continue

        if (x, y) != (3, 0):
            if digit_to_pos[string[i]][0] > x:
                q.append(((x + 1, y), path + "v"))
            elif digit_to_pos[string[i]][0] < x:
                q.append(((x - 1, y), path + "^"))
            if digit_to_pos[string[i]][1] > y:
                q.append(((x, y+1), path + ">"))
            elif digit_to_pos[string[i]][1] < y:
                q.append(((x, y-1), path + "<"))
    
    return ans
            



def solve(part, pins):

    if part:
        ans = 0
        for pin in pins:
            lenght = 0
            for i in range(len(pin)):
                lenght += numeric_to_directional(i, pin, 2)
            ans += lenght*int(pin[:-1])
        print(ans)
    else:
        ans = 0
        for pin in pins:
            lenght = 0
            for i in range(len(pin)):
                lenght += numeric_to_directional(i, pin, 25)
            ans += lenght*int(pin[:-1])
        print(ans)

# part 1
solve(True, pins)
# part 2
solve(False, pins)
