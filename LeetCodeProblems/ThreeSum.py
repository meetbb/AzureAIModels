"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
    
Two solutions can work here for most of sum problems.
1. Hashing: We already used it in Leetcode 1 (Two sum problem)
2. Two Pointers: We used it in Leetcode 153 (Two Sum ||)
"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # First, sort the array to simplify the two-pointer approach
    nums.sort()
    result = [] # This will hold the unique triplets
    
    # Loop through the array, fixing one number at a time
    for i in range(len(nums)):
        # Skip duplicate numbers for nums[i] (to avoid duplicate triplets)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two-pointer approach
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                # Sum too small, move left pointer to increase it
                left += 1
            elif total > 0:
                # Sum too large, move right pointer to decrease it
                right -= 1
            else:
                # Found a triplet!
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for nums[left] and nums[right]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers after processing a valid triplet
                left += 1
                right -= 1   
        
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))