from collections import Counter
import math

file = open("input.txt")
search_space = []
for line in file:
    search_space.append(line.strip())

def find_all_xmas(grid, word="xmas"):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  
        (1, 0), 
        (0, -1),  
        (-1, 0),  
        (1, 1),   
        (1, -1), 
        (-1, 1),  
        (-1, -1)  
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(i, j, direction):
        x, y = i, j
        for k in range(word_length):
            if not is_valid(x, y) or grid[x][y].lower() != word[k].lower():
                return False
            x += direction[0]
            y += direction[1]
        return True

    matches = 0
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if search_from(i, j, direction):
                    matches += 1
    
    return matches



def solve(part, grid):
    if part:
        print(find_all_xmas(grid))
    else:
        rows, cols = (len(grid), len(grid[0]))
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "A":
                    if (0 < i < rows-1 and 0 < j < cols-1 and
                        ((grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or 
                        (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M")) and 
                        ((grid[i+1][j-1] == "M" and grid[i-1][j+1] == "S") or 
                        (grid[i+1][j-1] == "S" and grid[i-1][j+1] == "M"))):
                        ans += 1
        
        print(ans)



        


    
    

# part 1
solve(True, search_space)
# part 2
solve(False, search_space)