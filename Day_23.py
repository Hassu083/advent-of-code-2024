from collections import Counter, defaultdict, deque
from itertools import permutations
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

graph = defaultdict(set)
for line in file:
    a, b = line.strip().split("-")
    graph[a].add(b)
    graph[b].add(a)


# DIR = [0, 1, 0, -1, 0]
# DIR2 = [1,-1,-1,1,1]
# facing = ["r", "d", "l", "u"]


def useful_function():
    pass


def evaluate_p1(node, path, all_sets, level):
    if level == 3:
        if len(path) == 4 and path[0] == path[-1] and len(set(path)) == 3:
            all_sets.add(tuple(path[:-1]))
        return
    for child in graph[node]:
        evaluate_p1(child, path + [child], all_sets, level + 1)





def evaluate_p2(node, graph):
    
    my_set = graph[node].copy()
    my_set.add(node)
    for child in graph[node]:
        new_set = graph[child].copy()
        new_set.add(child)
        if len(my_set & new_set) <= 2:
            continue
        my_set = my_set & new_set

    return my_set




def solve(part, graph):

    if part:
        ans = 0
        all_sets = set()
        for node in graph:
            evaluate_p1(node, [node], all_sets, 0)
    
        another_set = set()
        for seq in all_sets:
            if all(perm_seq not in another_set for perm_seq in permutations(seq)):
                for val in seq:
                    if "t" == val[0]:
                        ans += 1
                        break
                another_set.add(seq)
        print(ans)
    else:
        ans = 0
        my_password = None
        for node in graph:
            password = evaluate_p2(node, graph)
            if len(password) > ans:
                my_password = password
                ans = len(my_password)
        print(",".join(sorted(list(my_password))))

# part 1
solve(True, graph)
# part 2
solve(False, graph)
