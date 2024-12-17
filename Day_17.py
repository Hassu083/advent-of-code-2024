from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

operands = {}
program = None
isoperands = True
for line in file:
    if line == "\n":
        isoperands = False
        continue
    if isoperands:
        _, register, value = line.strip().split(" ")
        operands[register[:-1]] = int(value)
    else:
        program = list(map(int, line.strip().split(" ")[1].split(",")))


def useful_function():
    pass

# 21741053
def evaluate(opcode, operand, operands):
    match opcode:
        case 0:
            operands["A"] = math.trunc(operands["A"]/(2**operands[operand]))
            operands[4] = operands["A"]
        case 1:
            operands["B"] = operands["B"]^operands[operand]
            operands[5] = operands["B"]
        case 2:
            operands["B"] = (operands[operand]%8)
            operands[5] = operands["B"]
        case 3:
            if operands["A"] != 0:
                operands["pointer"] = operands[operand]
                return None, operands
        case 4:
            operands["B"] = operands["B"]^operands["C"]
            # print(operands["C"])
            operands[5] = operands["B"]
        case 5:
            operands["pointer"] += 2
            return operands[operand]%8, operands
        case 6:
            operands["B"] = math.trunc(operands["A"]/(2**operands[operand]))
            operands[5] = operands["B"]
        case 7:
            operands["C"] = math.trunc(operands["A"]/(2**operands[operand]))
            operands[6] = operands["C"]
    operands["pointer"] += 2
    return None, operands



def evaluate_A(idx, output, AA, a_idx, maain_ans):
    # print("".join(AA)[::-1], a_idx)
    # if  AA and "x" not in "".join(AA)[::-1]:
    #     print(int("".join(AA)[::-1], 2), a_idx)
    
    if idx == len(output):
        if 'x' not in AA:
            maain_ans.append(int("".join(AA)[::-1], 2))
        return 
    for b in range(8):
        for c in range(8):
            if (b^c^3) == output[idx]:
                # print(i,j)
                A = AA.copy()
                AB = bin(b^3)[2:].zfill(3)[::-1]
                C = bin(c)[2:].zfill(3)[::-1]
                # fit B
                for k in range(len(AB)):
                    # inside
                    if len(A) > int(a_idx+k):
                        if A[a_idx+k] == "x" or A[a_idx+k] == AB[k]:
                            A[a_idx+k] = AB[k]
                            continue
                        break
                    # outside
                    else:
                        A.append(AB[k])
                else:
                
                    # leave bits
                    for k in range(b):
                        if len(A) < a_idx+k+1:
                            A.append("x")
                    
                    # fit C
                    # print(a_idx+i)
                    for l in range(len(C)):
                        # inside
                        if len(A) > a_idx+b+l:
                            if A[a_idx+b+l] == "x" or A[a_idx+b+l] == C[l]:
                                A[a_idx+b+l] = C[l]
                                continue
                            break
                        # outside
                        else:
                            A.append(C[l])
                    
                    else:
                        # print(A)
                        print(AB, C,b, c, output[idx])
                        new = evaluate_A(idx+1, output, A, a_idx+3, maain_ans)
                        # if new != None:
                        #     return new
                
    return None
    






def solve(part, operands, program):
    operands["pointer"] = 0
    operands[0] = 0
    operands[1] = 1
    operands[2] = 2
    operands[3] = 3
    operands[4] = operands["A"]
    operands[5] = operands["B"]
    operands[6] = operands["C"]
    if part:
        operands_p1 = operands.copy()
        ans = []
        while (operands_p1["pointer"]+1) < len(program):
            out, operands_p1 = evaluate(program[operands_p1["pointer"]], program[operands_p1["pointer"]+1], operands_p1)
            if out != None:
                ans.append(str(out))
            # print(operands_p1)
        print(",".join(ans))
    else:
        maain_ans = []
        evaluate_A(0, program, [], 0, maain_ans)
        for val_a in maain_ans:
            operands_p1 = operands.copy()
            operands_p1["A"] = val_a
            ans = []
            while (operands_p1["pointer"]+1) < len(program):
                out, operands_p1 = evaluate(program[operands_p1["pointer"]], program[operands_p1["pointer"]+1], operands_p1)
                if out != None:
                    ans.append(str(out))
            print(val_a,",".join(ans))


# part 1
solve(True, operands, program)
# part 2
solve(False, operands, program)
