from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")


equation = []
for line in file:
    val, nums = line.split(": ")
    equation.append([int(val), list(map(int, nums.split(" ")))])


def evaluate_p1(val, cal, nums, i):
    if i == len(nums) and cal == val:
        return True
    if cal > val:
        return False
    if i == len(nums):
        return False
    if i == 0:
        if evaluate_p1(val, nums[i], nums, i+1):
            return True
        return False
    if evaluate_p1(val, cal + nums[i], nums, i + 1) or evaluate_p1(val, cal*nums[i], nums, i + 1):
        return True
    return False 


def evaluate_p2(val, cal, nums, i):
    if i == len(nums) and cal == val:
        return True
    if cal > val:
        return False
    if i == len(nums):
        return False
    if i == 0:
        if evaluate_p2(val, nums[i], nums, i+1):
            return True
        return False
    if evaluate_p2(val, cal + nums[i], nums, i + 1) or evaluate_p2(val, cal*nums[i], nums, i + 1) or evaluate_p2(val, int(str(cal)+str(nums[i])), nums, i + 1):
        return True
    return False 





def solve(part, eq):
    if part:
        ans = 0
        for val, nums in eq:
            if evaluate_p1(val, 0, nums, 0):
                ans += val
        print(ans)
    else:
        ans = 0
        for val, nums in eq:
            if evaluate_p2(val, 0, nums, 0):
                ans += val
        print(ans)

# part 1
solve(True, equation)
# part 2
solve(False, equation)
