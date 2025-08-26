"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array
    [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
    are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9
    
Approach: Use two pointers solution
"""
from typing import List

def trapRainWater(height: List[int]) -> int:
    """Python program to trap rain water."""
    left = 0
    right = len(height) - 1
    
    total = 0
    leftMax = height[0]
    rightMax = height[right]
    
    while left < right:
        if height[left] < height[right]:
            leftMax = max(leftMax, height[left])
            if leftMax - height[left] > 0:
                total = total + (leftMax - height[left])
            left += 1
        else:
            rightMax = max(rightMax, height[right])
            if rightMax - height[right] > 0:
                total = total + (rightMax - height[right])
            right -= 1
    return total

if __name__=="__main__":
    print(trapRainWater(height=[4,2,0,3,2,5]))