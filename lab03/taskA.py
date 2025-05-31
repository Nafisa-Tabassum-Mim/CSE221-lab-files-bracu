def merge(arr,low,mid,high):
  inversion = 0
  temp = []
  left = low
  right = mid+1
  while left <= mid and right <= high:
    if arr[left] <= arr[right]:
      temp.append(arr[left])
      left += 1
    else:
      inversion += mid-left+1
      temp.append(arr[right])
      right += 1

  while left <= mid:
      temp.append(arr[left])
      left += 1
  while right <= high:
      temp.append(arr[right])
      right += 1

  for i in range(0,len(temp)):
    arr[low+i] = temp[i]

  return inversion

def mergeSort(arr,low,high):
    if len(arr) <= 1:
        return arr
    else:
        if low >= high:
          return 0
        mid = (low+high)//2
        left_inversions = mergeSort(arr,low,mid)
        right_inversions = mergeSort(arr,mid+1 , high)
        inversion = merge(arr,low,mid,high) 
        
        return  left_inversions + right_inversions + inversion
        
T = int(input())  
arr = list(map(int, input().split())) 
inversion = mergeSort(arr, 0 , len(arr)-1)
    
print(inversion)
for i in range(len(arr)):
    print(arr[i],end=' ')