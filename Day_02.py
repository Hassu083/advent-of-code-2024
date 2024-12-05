from collections import Counter
import math

file = open("input.txt")
main_list = []
for line in file:
    main_list.append(list(map(int, line.split())))


def solve(part, lst):
    if part:
        ans = 0
        for ls in lst:
            smallest, largest = math.inf, -math.inf
            isIncreasing = ls[0] > ls[1]
            for i in range(len(ls)-1):
                if isIncreasing and ls[i]<ls[i+1]: break
                elif not isIncreasing and ls[i]>ls[i+1]: break 

                smallest = min(smallest, abs(ls[i]-ls[i+1]))
                largest = max(largest, abs(ls[i]-ls[i+1]))
            else:
                if 0 < smallest <= 3 and 0 < largest <= 3:
                    ans += 1
        print(ans)
    else:
        ans = 0
        for ls in lst:
            for i in range(len(ls)):
                ls_copy = ls.copy()
                del ls_copy[i]
                smallest, largest = math.inf, -math.inf
                isIncreasing = ls_copy[0] > ls_copy[1]
                for i in range(len(ls_copy)-1):
                    if isIncreasing and ls_copy[i]<ls_copy[i+1]: break
                    elif not isIncreasing and ls_copy[i]>ls_copy[i+1]: break 

                    smallest = min(smallest, abs(ls_copy[i]-ls_copy[i+1]))
                    largest = max(largest, abs(ls_copy[i]-ls_copy[i+1]))
                else:
                    if 0 < smallest <= 3 and 0 < largest <= 3:
                        ans += 1
                        break


        print(ans)



        


    
    

# part 1
solve(True, main_list)
# part 2
solve(False, main_list)