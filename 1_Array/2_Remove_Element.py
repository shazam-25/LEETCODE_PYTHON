'''
Problem Link: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
Problem Statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).
'''
def removeElement(nums, val):
    k = 0 # Pointer for the next position to place a non-val element
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Example usage
nums = [3,2,2,3]
val = 3
k = removeElement(nums, val)
print(k, nums[:k])  # Output: 2, [2,2]