def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        didswap = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswap = True
        if didswap == False:
            break
        

N = int(input())  
arr = list(map(int, input().split()))[:N] 

bubbleSort(arr)

print(*arr)