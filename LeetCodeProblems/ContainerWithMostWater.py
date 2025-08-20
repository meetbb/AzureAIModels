"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Optimal approach: Two pointers
"""
from typing import List

def maxArea(height: List[int]) -> int:
    # Two pointers
    left, right = 0, len(height) - 1
    max_area = 0 # Track the maximum area found so far
    
    while left < right:
        # Width between two lines
        width = right - left
        
        # Container height is limited by the shorter line
        current_height = min(height[left], height[right])
        
        # Calculate current area
        current_area = width * current_height
        
        # Update maximum area if current is larger
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))