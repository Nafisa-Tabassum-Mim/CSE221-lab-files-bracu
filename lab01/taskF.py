def selectionMinSwap(id,mark):
    swap = 0
    for i in range(0,len(mark)):
        max = i
        for j in range(i+1,len(mark)):
            if mark[j] > mark[max] or (mark[j]==mark[max] and id[j]<id[max]):
                max = j
        if max != i :
            mark[i], mark[max] = mark[max], mark[i]
            id[i], id[max] = id[max], id[i]
            swap+=1
    return swap

N = int(input())  
id = list(map(int, input().split()))[:N] 
mark = list(map(int, input().split()))[:N] 
swap = selectionMinSwap(id,mark)

print('Minimum swaps:',swap)
for i in range(0,len(mark)):
    print(f'ID: {id[i]} Mark: {mark[i]}')
        