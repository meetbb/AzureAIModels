"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

In video, you can hear the explanation at → 03:38
"""
def lengthOfLongestSubstring(s: str) -> int:
    """Function to find the length of Longest Substring"""
    # Initialize a set to store characters in the current window (substring without duplicates)
    char_set = set()
    # Initialize left pointer of sliding window
    left = 0
    # Variable to store the maximum length of substring found so far
    max_length = 0
    
    # Iterate through the string using 'right' pointer
    for right in range(len(s)):
        # If character at 'right' is already in the set,
        # move the left pointer until the duplicate is removed
        while s[right] in char_set:
            char_set.remove(s[left]) # remove the left most character from the set
            left += 1 # shrink the window from the left
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update max_length (current window size = right - left + 1)
        max_length = max(max_length, right - left + 1)
        
    # Return the maximum length found
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3