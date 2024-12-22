from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

sc_number = []
for line in file:
    sc_number.append(line.strip())




def next_number(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


def find_sequences(number, hashmap):
    sequence = []
    temp_number = number
    for _ in range(2000):
        nextnumber = next_number(number)
        change = int(str(nextnumber)[-1]) - int(str(number)[-1])
        sequence.append(change)
        if len(sequence) == 4:
            if temp_number not in hashmap[tuple(sequence)]:
                hashmap[tuple(sequence)][temp_number] = int(str(nextnumber)[-1])
            sequence.pop(0)
        number = nextnumber



def evaluate_p2(hashmap):
    ans = 0
    for seq in hashmap:
        val = sum(v for k,v in hashmap[seq].items())
        ans = max(ans, val)
    return ans




def solve(part, sc_number):

    if part:
        ans = 0
        for number in map(int, sc_number):
            for _ in range(2000):
                number = next_number(number)
            ans += number
        print(ans)
    else:
        hashmap = defaultdict(dict)
        for number in map(int, sc_number):
            find_sequences(number, hashmap)
        print(evaluate_p2(hashmap))

# part 1
solve(True, sc_number)
# part 2
solve(False, sc_number)
