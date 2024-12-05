from collections import Counter

file = open("input.txt")

list_1 = []
list_2 = []

 
for line in file:
    num1, num2 = map(int, line.split())
    list_1.append(num1)
    list_2.append(num2)

def solve(list_1, list_2, part):
    if part:
        list_1.sort()
        list_2.sort()
        total_distance = sum(abs(list_1[i]-list_2[i]) for i in range(len(list_2)))
        print(total_distance)
    else:
        list_2 = Counter(list_2)
        similarity = 0
        for num in list_1:
            similarity += num * list_2[num]
        print(similarity)

# part 1
solve(list_1, list_2, True)
# part 2
solve(list_1, list_2, False)