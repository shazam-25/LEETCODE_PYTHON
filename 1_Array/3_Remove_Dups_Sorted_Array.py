'''
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
Problem Statement:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.class
'''
def removeDUplicates(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k + 1
# Example usage:
nums = [0,0,1,1,1,2,2,3,3,4]
length = removeDUplicates(nums)
print("The length of the array after removing duplicates is:", length)