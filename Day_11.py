from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

lst = file.read().strip().split(" ")



class Node:
    
    def __init__(self, value):
        self.val = value
        self.next = None
    
        
    def __str__(self):
        ans = ''
        while self:
            ans += str(self.val) + ' -> '
            self = self.next
        return ans
            


def lenght(lst):
    i = 0
    while lst:
        i += 1
        lst = lst.next
    return i



def evaluate_p1(lst):
    new_lst = Node(-1)
    dumm = new_lst
    while lst:
        num = lst.val
        if num == "0":
            new_num = "1"
            dumm.next = Node(new_num)
        elif len(num)%2 == 0:
            n = len(num)//2
            first_half = str(int(num[:n]))
            secon_half = str(int(num[n:]))
            dumm.next = Node(first_half)
            dumm = dumm.next
            dumm.next = Node(secon_half)
        else:
            new_num = str(eval(num+"*2024"))
            dumm.next = Node(new_num)
        lst = lst.next
        dumm = dumm.next
    return new_lst.next




def evaluate_p2(my_dict):
    ans = 0
    new_dict = defaultdict(int)
    for num in my_dict:
        if num == "0":
            new_num = "1"
            new_dict[new_num] += my_dict[num]
        elif len(num)%2 == 0:
            n = len(num)//2
            first_half = str(int(num[:n]))
            secon_half = str(int(num[n:]))
            new_dict[first_half] += my_dict[num]
            new_dict[secon_half] += my_dict[num]
        else:
            new_num = str(eval(num+"*2024"))
            new_dict[new_num] += my_dict[num]
    return new_dict




def solve(part, list):
    if part:
        my_list = Node(-1)
        dum = my_list
        for num in list:
            dum.next = Node(num)
            dum = dum.next
        my_list = my_list.next
        for _ in range(25):
            my_list = evaluate_p1(my_list)
        print(lenght(my_list))
    else:
        my_dict = {num:1 for num in list}
        for _ in range(75):
            my_dict = evaluate_p2(my_dict)
        print(sum(val for val in my_dict.values()))

# part 1
solve(True, lst)
# part 2
solve(False, lst)
