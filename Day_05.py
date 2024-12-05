from collections import Counter, defaultdict, deque
import math

file = open("input.txt")
orders = []
order = True
before = defaultdict(set)
after = defaultdict(set)

for line in file:
    if line == "\n":
        order = False
        continue
    if order:
        a, b = list(map(int, line.split("|")))
        before[b].add(a)
        after[a].add(b)
    else:
        orders.append(list(map(int, line.split(","))))

def isCorrectOrder(order, rules_after):
    visited = set()
    for num in order:
        for nums in rules_after[num]:
            if nums in visited:
                return False
        visited.add(num)
    return True


def solve(part, orders,rules_before, rules_after):
    if part:
        ans = 0
        for order in orders:
            if isCorrectOrder(order, rules_after):
                ans += order[len(order)//2]        
        print(ans)
    else:
        ans = 0
        for order in orders:
            if not isCorrectOrder(order, rules_after):
                n = len(order)
                new_order = []
                order = set(order)

                # topological sort
                for num in order:
                    if len(rules_before[num].intersection(order)) == 0:
                        new_order.append(num)

                for num in new_order:
                    order.remove(num)

                q = deque(list(new_order))
                while order:
                    num = q.popleft()
                    for child in rules_after[num]:
                        if child in order:
                            if len(rules_before[child].intersection(order)) == 0:
                                new_order.append(child)
                                order.remove(child)
                                q.append(child)
                                
                ans += new_order[n//2]
        
        print(ans)



        


    
    

# part 1
solve(True, orders, before, after)
# part 2
solve(False, orders, before, after)
