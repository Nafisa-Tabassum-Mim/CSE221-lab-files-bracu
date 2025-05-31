N = int(input())
x, y = map(int, input().split())

directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
output = []
for a, b in directions:
    c, d = x + a, y + b
    if 1 <= c <= N and 1 <= d <= N:
        output.append((c, d))
    output.sort()

# print('output',output)
print(len(output))
for num1, num2 in output:
    print(num1, num2)
