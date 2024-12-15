from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

map = []
moves = []
isMap = True
for line in file:
    if line == "\n":
        isMap = False
        continue
    if isMap:
        map.append(line.strip())
    else:
        moves.append(line.strip())


move_to_cordinate = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}


def calculate_ans_p1(boxes):
    return sum(i*100 + j for i, j in boxes)

def calculate_ans_p2(new_map):
    ans = 0
    for i, row in enumerate(new_map):
        for j, char in enumerate(row):
            if char == "[":
                ans += i*100+j
    return ans

def evaluate_p1(x, y, move, boxes, wall):
    dx, dy = move_to_cordinate[move]
    new_x, new_y = x+dx, y+dy
    while (new_x, new_y) in boxes:
        new_x, new_y = new_x+dx, new_y+dy
        if (new_x, new_y) in wall:
            return x, y
        elif (new_x, new_y) not in boxes:
            boxes.add((new_x, new_y))
            boxes.remove((x+dx, y+dy))
            return x+dx, y+dy
    if (new_x, new_y) in wall:
        return x, y
    return x+dx, y+dy
    
def makeMap(map):
    new_map = []
    x, y = 0, 0
    for row in map:
        new_row = []
        for char in row:
            match(char):
                case "O":
                    new_row.extend(["[","]"])
                case "#":
                    new_row.extend(["#","#"])
                case "@":
                    x, y = len(new_map), len(new_row)
                    new_row.extend(["@","."])
                case ".":
                    new_row.extend([".","."])
        new_map.append(new_row)
    return x, y, new_map

def evaluate_p2_leftright(x, y, move, new_map):
    dx, dy = move_to_cordinate[move]
    new_x, new_y = x+dx, y+dy
    if new_map[new_x][new_y] == "#":
        return x, y
    while new_map[new_x][new_y] != ".":
        new_x, new_y = new_x+dx, new_y+dy
        if new_map[new_x][new_y] == "#":
            return x, y
    while True:
        new_map[new_x][new_y] = new_map[new_x-dx][new_y-dy]
        if new_map[new_x][new_y] == "@":
            new_map[new_x-dx][new_y-dy] = "."
            break
        new_x, new_y = new_x-dx, new_y-dy
    return x+dx, y+dy

def makeMove(level, dx, dy, new_map):
    for x, y in level:
        new_map[x+dx][y+dy] = new_map[x][y]
        new_map[x][y] = "."

def evaluate_p2_updown(level, move, new_map):
    dx, dy = move_to_cordinate[move]
    canMove = True
    for x,y in level:
        if new_map[x+dx][y+dy] == "#":
            return False
        elif new_map[x+dx][y+dy] in "[]":
            canMove = False
    
    if canMove:
        makeMove(level, dx, dy, new_map)
        return True
    
    new_level = []
    vis = set()
    for x, y in level:
        if new_map[x+dx][y+dy] == ".": continue
        elif new_map[x+dx][y+dy] == "]":
            if (x+dx, y+dy-1) not in vis:
                vis.add((x+dx, y+dy-1))
                new_level.append((x+dx, y+dy-1))
            if (x+dx, y+dy) not in vis:
                vis.add((x+dx, y+dy))
                new_level.append((x+dx, y+dy))
        elif new_map[x+dx][y+dy] == "[":
            if (x+dx, y+dy) not in vis:
                vis.add((x+dx, y+dy))
                new_level.append((x+dx, y+dy))
            if (x+dx, y+dy+1) not in vis:
                vis.add((x+dx, y+dy+1))
                new_level.append((x+dx, y+dy+1))
    if evaluate_p2_updown(new_level, move, new_map):
        makeMove(level, dx, dy, new_map)
        return True
    return False
        
def solve(part, map, moves):
    position = defaultdict(set)
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == ".": continue
            position[char].add((i,j))
    if part:
        boxes = position["O"].copy()
        x, y = list(position["@"])[0]
        for row in moves:
            for move in row:
                x, y = evaluate_p1(x, y, move, boxes, position["#"])
        print(calculate_ans_p1(boxes))
    else:
        x, y, new_map = makeMap(map)
        for row in moves:
            for move in row:
                if move in "<>":
                    x, y = evaluate_p2_leftright(x, y, move, new_map)
                else:
                    dx, dy = move_to_cordinate[move]
                    if evaluate_p2_updown([(x, y)], move, new_map):
                        x, y = x+dx, y+dy
        print(calculate_ans_p2(new_map))

# part 1
solve(True, map, moves)
# part 2
solve(False, map, moves)
