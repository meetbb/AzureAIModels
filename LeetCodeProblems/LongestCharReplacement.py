"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing 
the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form 'AABBBBA'.
    The substring BBBB has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.
    
For detailed explanation watch the video at → 03:56
"""
def characterReplacement(s: str, k: int) -> int:
    # Create an array to store occurences of each character (26 upper characters)
    occurences = [0] * 26
    left = 0 # left pointer of the sliding window
    ans = 0 # stores the maximum length found
    max_occurence = 0 # keeps track of the count of the most frequent characters
    
    # Iterate with right pointer
    for right in range(len(s)):
        # Update occurences of current character
        occurences[ord(s[right]) - ord('A')] += 1
        
        # Update max_occurence (frequency of the most common char in substring)
        max_occurence = max(max_occurence, occurences[ord(s[right]) - ord('A')])
        
        # Check if the window is invalid (more than k replacements needed)
        if (right - left + 1) - max_occurence > k:
            # Shrink window from left
            occurences[ord(s[left]) - ord('A')] -= 1
            left += 1
        
        # Update answer with current valid window size
        ans = max(ans, right - left + 1)
    return ans

print(characterReplacement(s="AABABBA", k=1)) # Output: 4