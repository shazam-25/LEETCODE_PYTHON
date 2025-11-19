'''
Problem Link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
Problem Statement:
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times. 
You may assume that the array is non-empty and the majority element always exists in the array.
Solve the problem in linear time and in O(1) space.
Example:
Input: nums = [3,2,3]
Output: 3
'''
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        else:
            count += (1 if num == candidate else -1)
    return candidate
# Example usage:
nums = [6,5,5]
result = majorityElement(nums)
print("The majority element is:", result)