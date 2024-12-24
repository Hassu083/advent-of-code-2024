from collections import Counter, defaultdict, deque
import math
import sys

sys.setrecursionlimit(10**6)

file = open("input.txt")

initial_values = {}
equations = []
isInitial = True
for line in file:
    if line == "\n":
        isInitial = False
        continue
    if isInitial:
        variable, value = line.strip().split(": ")
        initial_values.update({variable: int(value)})
    else:
        eq, output = line.strip().split(" -> ")
        var1, operator, var2 = eq.split(" ")
        equations.append((var1, operator, var2, output))


operation = {
                "AND" : lambda x, y : x & y,
                "OR" : lambda x, y : x | y,
                "XOR" : lambda x, y : x ^ y, 
            }


def calculate_value(initial_values):
    ans = 0
    index = 0
    while (z:="z"+str(index).zfill(2)) in initial_values:
        ans += initial_values[z]*2**index
        index += 1
    return ans


def evaluate_p1(graph, initial_values, indegree, equations):
    q = deque([variable for variable in initial_values])
    while q:
        variable = q.popleft()
        for dependent_variable in graph[variable]:
            indegree[dependent_variable] -= 1
            if indegree[dependent_variable] == 0:
                var1, var2, operator = equations[dependent_variable]
                initial_values[dependent_variable] = operation[operator](initial_values[var1], initial_values[var2])
                q.append(dependent_variable)


def eq(var1, var2, operator):
    return f"{var1} {operator} {var2}"

def evaluate_p2(equation_to_variable, variable_to_equation,  n):
    variables = []

    # without cin
    var1, var2 = "x00", "y00"
    xor_eq = eq(var1, var2, "XOR")
    and_eq = eq(var1, var2, "AND")
    sum_var = equation_to_variable[xor_eq]
    if sum_var != "z00":
        variables.extend(["z00", sum_var])
    cout = equation_to_variable[and_eq]

    # complete full adder
    for i in range(1, n):
        var1, var2, var3 = "x"+str(i).zfill(2), "y"+str(i).zfill(2), "z"+str(i).zfill(2)
        cin = cout
        xor_v12_var = equation_to_variable[eq(var1, var2, "XOR")]
        and_v12_var = equation_to_variable[eq(var1, var2, "AND")]
        temp1, temp2 = sorted([xor_v12_var, cin])
        sum_var = equation_to_variable[eq(temp1, temp2, "XOR")]
        if sum_var != var3:
            if xor_v12_var == var3:
                xor_v12_var = sum_var
            elif and_v12_var == var3:
                and_v12_var = sum_var
            temp1, temp2 = sorted([xor_v12_var, cin])
            sum_var = equation_to_variable[eq(temp1, temp2, "XOR")]
        if variable_to_equation[var3] != eq(temp1, temp2, "XOR"):
            v1, op, v2 = variable_to_equation[var3].split(" ")
            lst = [v1, v2]
            if op == "XOR":
                if temp1 in lst and temp2 not in lst:
                    if temp2 == xor_v12_var:
                        xor_v12_var, and_v12_var = and_v12_var, xor_v12_var
                        temp2 = xor_v12_var
                        variables.extend([and_v12_var, xor_v12_var])
                elif temp1 not in lst and temp2 in lst:
                    if temp1 == xor_v12_var:
                        xor_v12_var, and_v12_var = and_v12_var, xor_v12_var
                        temp1 = xor_v12_var
                        variables.extend([and_v12_var, xor_v12_var])
            else:
                variables.extend([sum_var, var3])

                
        and_xor12_cin = equation_to_variable[eq(temp1, temp2, "AND")]
        if and_xor12_cin == var3:
            and_xor12_cin = sum_var
        temp1, temp2 = sorted([and_xor12_cin, and_v12_var])
        cout = equation_to_variable[eq(temp1, temp2, "OR")]
        if cout == var3:
            cout = sum_var


    # only cout
    if cout != (z:="z"+str(n).zfill(2)):
        variables.extend([cout, z])

    return sorted(list(set(variables)))




def solve(part, initial_values, equations):

    if part:
        indegree = defaultdict(int)
        graph = defaultdict(set)
        operators = defaultdict(list)
        for var1, operator, var2, output in equations:
            operators[output] = [var1, var2, operator]
            graph[var1].add(output)
            graph[var2].add(output)
            indegree[output] += 2
        initial_values = initial_values.copy()
        evaluate_p1(graph, initial_values, indegree.copy(), operators)
        print(calculate_value(initial_values))
    else:
        equation_to_variable = defaultdict(str)
        variable_to_equation = defaultdict(list)
        for var1, operator, var2, output in equations:
            var1, var2 = sorted([var1, var2])
            equation_to_variable[f"{var1} {operator} {var2}"] = output
            variable_to_equation[output] = f"{var1} {operator} {var2}"
        variables = evaluate_p2(equation_to_variable, variable_to_equation,  len(initial_values)//2)
        print(",".join(variables))
# part 1
solve(True, initial_values, equations)
# part 2
solve(False, initial_values, equations)
