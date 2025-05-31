def sortedList():
    N = int(input())
    arr1 = list(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    temp = []
    i,j= 0 ,0 
    
    while i <len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i +=1
        else :
            temp.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        temp.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        temp.append(arr2[j])
        j += 1
    
    print(*temp)
    
sortedList()

