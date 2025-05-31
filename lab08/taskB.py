def king(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  
        x = parents[x]
    return x
def union(x, y):
    rt_x = king(x)
    rt_y = king(y)
    if rt_x == rt_y:
        return False
    if size[rt_x] < size[rt_y]:
        rt_x, rt_y = rt_y, rt_x
    parents[rt_y] = rt_x
    size[rt_x] += size[rt_y]
    return True

n, m = map(int, input().split())

edge = []
for i in range(m):
    u, v, w = map(int, input().split())
    edge.append((w, u, v)) 
edge.sort()  
 
parents = [i for i in range(n + 1)]
size = [1] * (n + 1)
 
total_cost = 0
for w, u, v in edge:
    if union(u, v):
        total_cost += w
print(total_cost)