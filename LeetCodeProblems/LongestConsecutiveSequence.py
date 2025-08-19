"""
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. 
You must write an algorithm that runs in O(n) time.

Example 1: 
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1,2,3,4].
    Therefore its length is 4.
    
Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
"""
from typing import List

def longestConsecutiveSequence(nums: List[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums) # O(n) space
    longestSubSequence = 0
    
    # Iterate through unique numbers
    for n in num_set:
        # Only start a sequence if n is the *start* of one
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longestSubSequence = max(longestSubSequence, length)
    return longestSubSequence

print(longestConsecutiveSequence([100,4,200,1,3,2]))    # Output: 4
print(longestConsecutiveSequence([0,3,7,2,5,8,4,6,0,1])) # Output: 9
print(longestConsecutiveSequence([1,0,1,2]))             # Output: 3
