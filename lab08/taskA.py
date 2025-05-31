def friendship(x):
    root = x
    while friend[root] != root:
        root = friend[root]
    while friend[x] != root:
        friend[x], x = root, friend[x]
    return root
 
def union(x, y):
    rt_x = friendship(x)
    rt_y = friendship(y)
    if rt_x != rt_y:
        if size[rt_x] < size[rt_y]:
            rt_x, rt_y = rt_y, rt_x
        friend[rt_y] = rt_x
        size[rt_x] += size[rt_y]
    return size[rt_x]
 
N, K = map(int, input().split())
 
friend = [i for i in range(N + 1)]
size = [1] * (N + 1)
 
for i in range(K):
    a, b = map(int, input().split())
    print(union(a, b))