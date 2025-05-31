# def max_pair_square(arr, left, right):

#     if right - left < 1:
#         return -float('inf')

#     if right - left == 1:
#         return arr[left] + (arr[right] ** 2)

#     mid = (left + right) // 2

#     left_max = max_pair_square(arr, left, mid)
#     right_max = max_pair_square(arr, mid + 1, right)
#     max_A_j_squared = max([arr[j] ** 2 for j in range(mid + 1, right + 1)])
#     max_A_i = max([arr[i] for i in range(left, mid + 1)])
#     cross_max = max_A_i + max_A_j_squared
#     return max(left_max, right_max, cross_max)


# n = int(input())
# arr = list(map(int, input().split()))
# result = max_pair_square(arr, 0, n - 1)
# print(result)

# Function to find the maximum subarray sum crossing the middle point
# def MAX_CROSS_SUBARRAY(A, low, mid, high):
#     left_sum = float('-inf')  # Initialize left_sum to negative infinity
#     sum_left = 0
#     max_left = mid
    
#     # Find the maximum subarray sum in the left half (A[low..mid])
#     for i in range(mid, low - 1, -1):
#         sum_left += A[i]
#         if sum_left > left_sum:
#             left_sum = sum_left
#             max_left = i

#     right_sum = float('-inf')  # Initialize right_sum to negative infinity
#     sum_right = 0
#     max_right = mid + 1

#     # Find the maximum subarray sum in the right half (A[mid+1..high])
#     for j in range(mid + 1, high + 1):
#         sum_right += A[j]
#         if sum_right > right_sum:
#             right_sum = sum_right
#             max_right = j

#     # Return the total maximum sum for the cross-subarray
#     return left_sum + right_sum

# # Function to find the maximum subarray sum using divide and conquer
# def MAXIMUM_SUBARRAY(A, low, high, count):
#     # Base case: if the subarray has only one element
#     if low == high:
#         return A[low], count
#     else:
#         # Find the middle point
#         mid = (low + high) // 2

#         # Recursively find the maximum subarray sum for the left, right, and crossing parts
#         max_left_sum, count = MAXIMUM_SUBARRAY(A, low, mid, count)
#         max_right_sum, count = MAXIMUM_SUBARRAY(A, mid + 1, high, count)
#         max_cross_sum = MAX_CROSS_SUBARRAY(A, low, mid, high)

#         # Check if the Cross-Sum exceeds both the Left-Sum and Right-Sum
#         if max_cross_sum > max_left_sum and max_cross_sum > max_right_sum:
#             count += 1

#         # Return the maximum of the three sums and the updated count
#         return max(max_left_sum, max_right_sum, max_cross_sum), count

# # Example usage
# A = [1, 4, 3, -5, 5, 6, 1, -4]
# n = len(A)
# result, count = MAXIMUM_SUBARRAY(A, 0, n - 1, 0)

# print(f"Maximum subarray sum is: {result}")
# print(f"Number of times the Cross-Sum exceeds both Left-Sum and Right-Sum: {count}")


def MAX_CONSECUTIVE_POSITIVE(A, low, high):
    if low == high:
        return A[low]
    
    mid = (low + high) // 2
    
    # Recursively find the longest positive streak in the left and right halves
    left_streak = MAX_CONSECUTIVE_POSITIVE(A, low, mid)
    right_streak = MAX_CONSECUTIVE_POSITIVE(A, mid + 1, high)
    
    # Find the longest crossing streak
    crossing_streak = FIND_CROSSING_STREAK(A, low, mid, high)
    
    # Return the maximum of the three
    return max(left_streak, right_streak, crossing_streak)

def FIND_CROSSING_STREAK(A, low, mid, high):
    # Find the longest streak in the left half
    left_count = 0
    for i in range(mid, low - 1, -1):
        if A[i] > 0:
            left_count += A[i]
        else:
            break
    
    # Find the longest streak in the right half
    right_count = 0
    for j in range(mid + 1, high + 1):
        if A[j] > 0:
            right_count += A[j]
        else:
            break
    
    # Return the total length of the crossing streak
    return left_count + right_count

# Example usage
A = [1, 4, 3, -5, 5, 6, 1, -4]
n = len(A)
result = MAX_CONSECUTIVE_POSITIVE(A, 0, n - 1)
print(f"Maximum consecutive positive goal difference: {result}")
