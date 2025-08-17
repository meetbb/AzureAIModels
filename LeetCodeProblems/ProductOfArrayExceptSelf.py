"""
PRODUCT OF ARRAY EXCEPT SELF

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,15,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
"""
from typing import List

def productOfArrayExceptSelf(nums: List[int]) -> List[int]:
    # Initialize result array with 1s
    result = [1] * len(nums)
    
    prefix = 1
    # Left to right pass
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    # Right to left pass
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

print(productOfArrayExceptSelf([1,2,3,4]))