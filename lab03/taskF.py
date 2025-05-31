
def postOrder(inOrder, preOrder):
    if not inOrder or not preOrder:
        return []

    mid = preOrder[0]
    i = inOrder.index(mid)
    leftin = inOrder[:i]
    rightin = inOrder[i+1:]
    lpre = preOrder[1:len(leftin)+1]
    rpre = preOrder[len(leftin)+1:]

    r_postOrder = postOrder(rightin, rpre)
    l_postOrder = postOrder(leftin, lpre)

    result = l_postOrder + r_postOrder + [mid]
    return result

N = int(input())
inOrder = list(map(int, input().split()))
preOrder = list(map(int, input().split()))
postOrder = postOrder(inOrder, preOrder)

for i in postOrder:
    print(i, end=" ")