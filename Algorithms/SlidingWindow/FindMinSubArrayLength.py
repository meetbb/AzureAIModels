"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1
Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    
👉 Here you must find the minimum-length contiguous subarray such that the sum ≥ target.
If no such subarray exists → return 0.

✅ Detailed explanation per step.

| Step | left | right | Window Elements | sum | Action                                  |
| ---- | ---- | ----- | --------------- | --- | --------------------------------------- |
| 1    | 0    | 0     | [2]             | 2   | sum < 7 → expand right                  |
| 2    | 0    | 1     | [2,3]           | 5   | sum < 7 → expand right                  |
| 3    | 0    | 2     | [2,3,1]         | 6   | sum < 7 → expand right                  |
| 4    | 0    | 3     | [2,3,1,2]       | 8   | sum ≥ 7 → record len=4; now shrink left |
| 5    | 1    | 3     | [3,1,2]         | 6   | sum < 7 → stop shrinking; expand right  |
| 6    | 1    | 4     | [3,1,2,4]       | 10  | sum ≥ 7 → len=4; shrink left            |
| 7    | 2    | 4     | [1,2,4]         | 7   | sum ≥ 7 → len=3; shrink left            |
| 8    | 3    | 4     | [2,4]           | 6   | sum < 7 → expand right                  |
| 9    | 3    | 5     | [2,4,3]         | 9   | sum ≥ 7 → len=3; shrink left            |
| 10   | 4    | 5     | [4,3]           | 7   | sum ≥ 7 → len=2 ✅ (minimum)            |

"""
def minSubArrayLength(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        total += nums[right]
        
        # Shrink from left while sum ≥ target
        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if min_length == float('inf') else min_length

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLength(target=target, nums=nums))