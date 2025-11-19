'''
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
Problem Statement: 
Given a sorted array nums, remove the duplicates in-place such that each element appears at most twice and returns the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
Example:
Input: nums = [0,0,1,1,1,1,2,2,3,3,4]
Output: 9, nums = [0,0,1,1,2,2,3,3,4]
'''
def removeDuplicates(nums):
    k = 0
    for x in nums:
        if k < 2 or x != nums[k - 2]:
            nums[k] = x
            k += 1
    return k
# Example usage:
nums = [0,0,1,1,1,1,2,2,3,3,4]
length = removeDuplicates(nums)
print("The length of the array after removing duplicates is:", length)