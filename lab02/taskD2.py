def find_first_one(s):
    l = 0
    r = len(s)-1
    while l <= r:
        mid = (l + r)//2
        if s[mid] == '1':
            if (mid-1 == -1) or s[mid-1] == '0' :
                print(mid+1)
                break
            else:
                r = mid - 1
        else:
            l = mid + 1
    if l > r:
        print(-1)


T = int(input())  
for i in range(0, T ):
    s=input()
    find_first_one(s)