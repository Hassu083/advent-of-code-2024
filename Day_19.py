from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

available_patterns = None
isavailable = True
patterns = []
for line in file:
    if line == "\n":
        isavailable = False
        continue
    if isavailable:
        available_patterns = line.strip().split(", ")
    else:
        patterns.append(line.strip())



class TrieNode():
    def __init__(self):
        self.next = dict()
        self.pattern_complete = False


def evaluate_p1(i, word, memo):

    if i >= len(word):
        return True
    if i in memo:
        return memo[i]
    ans = False
    tree_node = root
    for j in range(i, len(word)):
        if word[j] not in tree_node.next:
            break
        if tree_node.next[word[j]].pattern_complete:
            ans = ans or evaluate_p1(j+1, word, memo)
            if ans:
                return True
        tree_node = tree_node.next[word[j]]
    memo[i] = ans
    return ans



def evaluate_p2(i, word, memo):

    if i >= len(word):
        return 1
    if i in memo:
        return memo[i]
    ans = 0
    tree_node = root
    for j in range(i, len(word)):
        if word[j] not in tree_node.next:
            break
        if tree_node.next[word[j]].pattern_complete:
            ans += evaluate_p2(j+1, word, memo)
        tree_node = tree_node.next[word[j]]
    memo[i] = ans
    return ans


root = None

def solve(part, available_patterns, patterns):
    global root
    root = TrieNode()
    for pattern in available_patterns:
        root_copy = root
        for char in pattern:
            if char not in root_copy.next:
                root_copy.next[char] = TrieNode()
            root_copy = root_copy.next[char]
        root_copy.pattern_complete = True

    if part:
        ans = 0
        for i, pattern in enumerate(patterns):
            memo = dict()
            ans += int(evaluate_p1(0, pattern, memo))
        print(ans)
    else:
        ans = 0
        for i, pattern in enumerate(patterns):
            memo = dict()
            ans += evaluate_p2(0, pattern, memo)
        print(ans)

# part 1
solve(True, available_patterns, patterns)
# part 2
solve(False, available_patterns, patterns)
