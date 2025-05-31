def find_first_one(s):
    l, r = 0, len(s) - 1
    result = -1  

    while l <= r:
        mid = (l + r) // 2

        if s[mid] == '1':
            result = mid + 1  
            r = mid - 1  
        else:
            l = mid + 1  

    print(result)

T = int(input())  
for i in range(0, T):
    s=input()
    find_first_one(s)