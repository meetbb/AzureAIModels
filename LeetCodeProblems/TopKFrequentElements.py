"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""
import heapq
from collections import Counter
import random

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each number.
    freq_map = Counter(nums) # O(n)
    
    # Step 2: Use a min-heap to keep track of top K elements
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num)) # Push (frequency, number)
        if len(heap) > k: # Maintain size K
            heapq.heappop(heap) # Remove smallest frequency
    
    # Step 3: Extract numbers from heap
    return [num for freq, num in heap]

# Create a list of size 50 with integers between 1 and 10
nums = [random.randint(1, 10) for _ in range(50)]
print(f"Sample array is: {nums}")
# Test the function with k = 3
print(topKFrequent(nums=nums, k=3))
