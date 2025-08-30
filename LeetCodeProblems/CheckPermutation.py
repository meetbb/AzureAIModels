"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
 

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Approach: Using Sliding Window
"""
class CheckPermutation:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for s1's permutation to be in s2
        if len(s1) > len(s2):
            return False
        
        # Create frequency arrays for s1 and the first window of s2
        s1Map = [0] * 26
        s2Map = [0] * 26
        
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1
        
        # Slide the window across s2
        for i in range(len(s2) - len(s1)):
            if self.matches(s1Map=s1Map, s2Map=s2Map):
                return True
            
            # Add next character into the window
            s2Map[ord(s2[i + len(s1)]) - ord('a')] += 1
            # Remove the character going out of the window
            s2Map[ord(s2[i]) - ord('a')] -= 1
        
        # Final check for the last window
        return self.matches(s1Map=s1Map, s2Map=s2Map)
            
    def matches(self, s1Map, s2Map):
        for i in range(26):
            if s1Map[i] != s2Map[i]:
                return False
        return True
    
sol = CheckPermutation()
print(sol.checkInclusion("ab", "eidbaooo"))  # True
print(sol.checkInclusion("ab", "eidboaoo"))  # False
