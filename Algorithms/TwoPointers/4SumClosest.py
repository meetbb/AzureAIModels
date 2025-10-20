"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
    
TIME AND SPACE COMPLEXITY:
    TIME: O(㎥) - where m is length of array
    SPACE: O(1) - Excluding output list
"""
def fourSum(nums, target):
    nums.sort()
    arrayLength = len(nums)
    response = []
    
    for i in range(arrayLength - 3):
        # Skip duplicate for j
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, arrayLength - 2):
            # Skip duplicate for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, arrayLength - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    response.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Move both pointers skipping duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return response

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums=nums, target=target))