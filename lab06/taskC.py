from collections import deque

def bfs(x1, y1, x2, y2):
    vis = [[0 for i in range(n + 1)] for j in range(n + 1)]
    queue = deque([(x1, y1, 0)])
    valid_moves = [(-1,  2), ( 1,  2), (-2,  1),( 2,  1),
           (-2, -1),( 2, -1),(-1, -2), ( 1, -2)]

    while queue:
        X, Y, Count = queue.popleft()
        if X == x2 and Y == y2:
            return Count
        
        for dx, dy in valid_moves:
            nX, nY = X + dx, Y + dy

            if 1 <= nX <= n and 1 <= nY <= n and vis[nX][nY] == 0:
                queue.append((nX, nY, Count + 1))
                vis[nX][nY] = 1
    return -1

n = int(input())
x1, y1, x2, y2 = map(int, input().split())

print(bfs(x1, y1, x2, y2))