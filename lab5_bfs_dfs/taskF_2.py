row, col = list(map(int, input().split()))
grid = [input().strip() for _ in range(row)]
 
v = [[False] * col for _ in range(row)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
# print('grid-',grid) 
# print('grid-',grid[0][0]) 

def BFS(x, y):
    queue = [(x, y)]
    v[x][y] = True
    diamond = 0
 
    while queue:
        a, b = queue.pop(0)
        if grid[a][b] == 'D':
            diamond += 1
 
        for dx, dy in directions:
            e, f = a + dx, b + dy
            if 0 <= e < row and 0 <= f < col and not v[e][f] and grid[e][f] != '#':
                v[e][f] = True
                queue.append((e, f))
 
    return diamond
 
max_diamond = 0
for i in range(row):
    for j in range(col):
        if not v[i][j] and grid[i][j] != '#':
            max_diamond = max(max_diamond, BFS(i, j))
 
print(max_diamond)