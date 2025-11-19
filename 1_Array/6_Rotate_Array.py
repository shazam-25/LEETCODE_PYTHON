'''
Problem Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
Problem Statement:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Thought Process:
To rotate the array to the right by k steps, we can use the following approach:
Reverse: [7,6,5,4,3,2,1]
Arrange last k elements to front: [5,6,7,4,3,2,1]
Arrange remaining n-k elements: [5,6,7,1,2,3,4]
'''
def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than n
    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n-k elements
    reverse(k, n - 1)
    return nums
# Example usage:
nums = [1,2,3,4,5,6,7]
k = 3
rotated_array = rotate(nums, k)
print("The rotated array is:", rotated_array)
print(f'Runtime:', rotate.__code__.co_consts)  # To show the runtime information
    