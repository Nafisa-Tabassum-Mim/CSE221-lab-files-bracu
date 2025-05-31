length,last = map(int, input().split())
arr = list(map(str, input().split()))
newArr=[]
for i in range(last-1,-1,-1):
    newArr.append(arr[i])
    
for i in newArr:
    print(i,end=' ')
