from collections import defaultdict

def easyTree():
    N, R = map(int, input().split())

    trees = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        trees[u].append(v)
        trees[v].append(u)

    subtree_size = [0] * (N + 1)
    visited = [False] * (N + 1)


    stack = [(R, -1)]
    post_order = []

    while stack:
        node, parent = stack.pop()
        post_order.append((node, parent))
        for i in trees[node]:
            if i != parent:
                stack.append((i, node))

    for node, parent in reversed(post_order):
        subtree_size[node] = 1
        for i in trees[node]:
            if i != parent:
                subtree_size[node] += subtree_size[i]

    Q = int(input())
    for j in range(Q):
        X = int(input())
        print(subtree_size[X])

easyTree()