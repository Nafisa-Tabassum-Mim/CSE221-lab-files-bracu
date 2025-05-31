def count_number(arr,s):
    first,last = s
    i,j=0,len(arr)-1
    while i <= j and arr[i] < first:
            i += 1
    while i <= j and arr[j] > last:
            j -= 1
    print(j-i+1)
            
    
    
arr_size, T = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(0, T ):
    s = list(map(int, input().split())) 
    count_number(arr , s)
    
# # n time complexity 



