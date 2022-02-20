
from typing import List
# Following the requirements of the question, there are two steps to find the median from two sorted arrays:
# 1. Merge two sorted arrays.
    # 1.1 Create a new array to store the merged array.
    # 1.2 Compare the last element of nums1 and the last element of nums2.
    # 1.3 Put the greater last element between nums1 and nums2 to the new array and remove it in the original array.
    # 1.4 Repeat
    # 1.5 We will have the result of the merged array, with descending order. E.g. [9,8,7,6,5]
    # 1.6 Reverse the result to get the ascending order.
    # 1.7 Append remaining elements of nums1 and nums2 to the result.
    # 1.8 Return the result.

    # Time complexity: O(m + n), m and n are the lengths of nums1 and nums2 respectively.

# 2. Find the median of the merged array.
    # 2.1 Find the median of the merged array with the function find_median.
    # 2.2 Return the median.

    # Time complexity: O(1)

# Time complexity: O(m + n) and O(1) => O(m + n)
# With m, n is the lengths of nums1 and nums2 respectively.

def merge(nums1, nums2) -> List[int]:
    """Merge two sorted arrays""" 
    res = []
    m = len(nums1) # length of nums1
    n = len(nums2) # length of nums2 
    while m > 0 and n > 0:              # while there are still elements in both nums1 and nums2
        if nums1[m-1] >= nums2[n-1]:    # if the last element of nums1 is not smaller than the last element of nums2
            res.append(nums1[m-1])      # append the last element of nums1 to the result
            m -= 1                      # remove the last element of nums1
        else:                           # if the last element of nums1 is smaller than the last element of nums2
            res.append(nums2[n-1])      # append the last element of nums2 to the result
            n -= 1                      # remove the last element of nums2
    if m > 0:                           # if there are still elements in nums1
        res = nums1[:m] + res[::-1]     # append the remaining elements of nums1 to the beginning of the result. res[::-1] to reverse the temp result.
    else:                               # if there are still elements in nums2
        res = nums2[:n] + res[::-1]     # append the remaining elements of nums2 to the beginning of the result. res[::-1] to reverse the temp result.
    return res                          # return the merged array from two sorted arrays
    


def find_median(arr) -> float:
    """Find the median of a list of numbers"""
    size = len(arr) # length of arr
    if size % 2 == 0:                                           # if the length of arr is even
        median = (arr[int(size/2) - 1] + arr[int(size/2)]) / 2  # calculate the median
    else:                           # if the length of arr is odd
        median = arr[int(size/2)]   # calculate the median
    return median                   # return the median

if __name__ == "__main__":
    nums1 = [1, 3, 5, 6]
    nums2 = [1, 2, 10]
    merged = merge(nums1, nums2)
    print("The median: ", find_median(merged))

