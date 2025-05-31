def orderingBinary(A):
    result = []

    def divcon(start, end):
        if start > end:
            return
        mid = (start + end) // 2
        result.append(A[mid])
        divcon(start, mid - 1)
        divcon(mid + 1, end)

    divcon(0, len(A) - 1)
    return result

N = int(input())
A = list(map(int, input().split()))
result = orderingBinary(A)
for i in result:
    print(i, end=" ")
