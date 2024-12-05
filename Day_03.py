from collections import Counter
import math

file = open("input.txt")

inst = file.read().strip()
n = len(inst)


def do_mul(inst):
    ans = 0
    inst = inst.split("mul(")
    new_inst = []
    for chars in inst:
        new_inst.extend(chars.split(")"))
    for chars in new_inst:
        chars = chars.split(",")
        if len(chars) == 2 and chars[0].isdigit() and chars[1].isdigit():
            ans += int(chars[0]) * int(chars[1])
    return ans


def solve(part, inst):
    if part:
        print(do_mul(inst))
    else:
        inst = inst.split("don't()")
        new_inst = [inst[0]]
        for chars in inst[1:]:
            chars = "".join(chars.split("do()")[1:])
            new_inst.append(chars)
        inst = "".join(new_inst)
        print(do_mul(inst))



        


    
    

# part 1
solve(True, inst)
# part 2
solve(False, inst)