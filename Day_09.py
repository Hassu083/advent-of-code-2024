from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

disk = file.read().strip()


def checksum(content):
    ans = 0
    for i, num in enumerate(content):
        if num == ".": continue
        ans += i * num
    return ans


def evaluate_p1(content):
    left = 0
    right = len(content) -1
    while left <= right:
        while left <= right and content[left] != ".":
            left += 1
        while left <= right and content[right] == ".":
            right -= 1
        if left < right and content[left] == "." and content[right] != ".":
            content[left], content[right] = content[right], content[left]

    return checksum(content)



def evaluate_p2(file_content, free_sp, file_pointer):
    for a, b in file_pointer[::-1]:
        file_size = b-a+1
        positions = defaultdict(int) # position : space
        for free_space in free_sp.keys():
            if free_space >= file_size and free_sp[free_space][0] < a:
                positions[free_sp[free_space][0]] = free_space
        if positions:
            free_space = positions[sorted(positions.keys())[0]]
            idx = free_sp[free_space].pop(0)
            for i in range(b-a+1):
                file_content[idx+i], file_content[a+i] = file_content[a+i], "."
            if free_space > b-a+1:
                new_space = free_space - (b-a+1)
                new_idx = idx + b-a+1
                free_sp[new_space].append(new_idx)
                free_sp[new_space] = sorted(free_sp[new_space])
            if not free_sp[free_space]:
                del(free_sp[free_space])

    return checksum(file_content)




def solve(part, disk):
    file_content = []
    free_spaces = 0
    free_sp = defaultdict(list)
    file_pointer = []
    for i, data in enumerate(disk):
        if i%2 == 0:
            file_pointer.append([len(file_content),0])
            file_content.extend([i-free_spaces]*int(data))
            file_pointer[-1][1] = len(file_content) - 1
        else:
            free_sp[int(data)].append(len(file_content))
            file_content.extend(["."]*int(data))
            free_spaces += 1
    if part:
        ans = 0
        ans = evaluate_p1(file_content.copy())
        print(ans)
    else:
        ans = 0
        ans = evaluate_p2(file_content, free_sp, file_pointer)
        print(ans)

# part 1
solve(True, disk)
# part 2
solve(False, disk)
