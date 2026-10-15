# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# arr=[10,50,30,20]
# target=20
# result=linear_search(arr,target)
# if result!=-1:
#     print("Element found at index: ", result)    #Element found at index:  3
# else:
#     print("Not found")


# binar search 
#divide and conquyer
# eg:
#     arr[10,20,30,40,50] 

# How It Works (Step-by-Step)

# 1. Initialize pointers: Set a low pointer to the first index and a high pointer to the last index of the sorted array.
# 2. Find the middle: Calculate the mid index of the current window.
# 3. Compare:
# 	• If array[mid] equals the target, the search is complete (Element found).
# 	• If array[mid] is greater than the target, narrow the window to the left half (high = mid - 1).
# 	• If array[mid] is less than the target, narrow the window to the right half (low = mid + 1).
# 4. Repeat: Continue steps 2 and 3 as long as low <= high. If low exceeds high, the target is not in the array.


# Core Performance Metrics


# Metric	Complexity	Explanation
# Best Case Time	O(1)	The target element is located exactly at the first mid checked.
# Worst/Average Time	\(O(\log n)\)	The search space is cut in half with every single comparison step.
# Space Complexity	O(1)	The iterative approach requires no extra memory allocations.

# 

# def binary_search(arr,target):
#     left=0
#     right=len(arr)
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# arr=[10,20,30,40,50]
# target=60
# result=binary_search(arr,target)
# if result!=-1:
#     print("Element found at index: ", result)    #Element found at index:  2
# else:
#     print("Not found")








