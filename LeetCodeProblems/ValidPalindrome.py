"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""
def isValidPalindrome(s: str) -> bool:
    # Step 1: Use two pointers, left starting at 0 and right starting at the last index. 
    left, right = 0, len(s) - 1
    
    # Step 2: Keep changing characters while left < right
    while left < right:
        # Move left pointer forward until we find an alphanumeric character
        # str.isalnum() checks if a character is a letter or digit
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer backward until we find an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        # Step 3: Compare characters (ignoring case by converting both to lowercase)
        if s[left].lower() != s[right].lower():
            return False # if mismatch found → not a palindrome
        # Step 4: Move both pointers inward
        left += 1
        right -= 1
        
        # Step 5: If all characters matched, return True
    return True

print(isValidPalindrome("A man, a plan, a canal: Panama"))  # True
print(isValidPalindrome("race a car"))                      # False
print(isValidPalindrome(" "))                               # True
