'''
Problem Link:https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
Problem Statement:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. 
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''
def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2 and the end of the merged array
    p1, p2, p = m-1, n-1, m+n-1
    # Merge in reverse order
    while p1>=0 and p2>=0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    return nums1
# Example usage
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))  # Output: [1,2,2,3,5,6]

