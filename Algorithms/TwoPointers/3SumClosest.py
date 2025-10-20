"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:

    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

SOLUTION:
    Approach would be Two Pointers here.

Time and Space Complexity
    Time: O(n²) - Sorting is O(n ㏒n)
    Space: O(1) - No extra space apart from variables.
    
WALKTHROUGH TABLE:

| i | nums[i]  | left  | nums[left]  | right  | nums[right]   | current_sum  | |target - current_sum|  closest_sum (after update) | Action                        |
|---|----------|-------|-------------|--------|---------------|--------------|----------------------|-----------------------------|-------------------------------|
| 0 | -4       | 1     | -1          | 3      | 2             | -3           | 4                    | -3                          | current_sum < target → left++ |
| 0 | -4       | 2     | 1           | 3      | 2             | -1           | 2                    | -1                          | current_sum < target → left++ |
| 0 | -4       | 3     | 2           | 3      | 2             | —            | —                    | —                           | stop (left == right)          |
| 1 | -1       | 2     | 1           | 3      | 2             | 2            | 1                    | 2                           | current_sum > target → right--|
| 1 | -1       | 2     | 1           | 2      | 1             | —            | —                    | —                           | stop (left == right)          |
| 2 | 1        | —     | —           | —      | —             | —            | —                    | —                           | loop ends                     |

Final closest_sum = 2
"""
def threeSumClosest(nums, target):
    nums.sort()
    arrayLength = len(nums)
    closest_sum = float('inf')
    
    for i in range(arrayLength - 2):
        left, right = i + 1, arrayLength - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest sum if this is nearer to target
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            # Move pointers based on comparison
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum # Perfect match found
    return closest_sum

print(threeSumClosest(nums=[-1,2,1,-4], target=1))