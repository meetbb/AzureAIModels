"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
 
Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Approach 1 (O(n²)): Brute Force
Approach 2 (O(n ㏒n)): Binary Search (Since we have already sorted array)
Approach 3 Optimal approach (O(n)): Two Pointers
"""
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    # Step 1: Initialize two pointers
    left, right = 0, len(numbers) - 1
    
    # Step 2: Loop until the two pointers meet
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        # Step 3: Check if the sum matches the target
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
print(twoSum([2,7,11,15], 9))   # [1, 2]
print(twoSum([2,3,4], 6))       # [1, 3]
print(twoSum([-1,0], -1))       # [1, 2]
