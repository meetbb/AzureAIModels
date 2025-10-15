"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
if no such substring exists, return 0.

Example 1:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Walkthrough of solution

| Step  | Substring being processed |        Frequency map |    Any char with freq < k? | Split char | Parts after split |              Recursive results on parts | Return for this call |
| ----- | ------------------------- | -------------------: | -------------------------: | ---------: | ----------------: | --------------------------------------: | -------------------: |
| 1     | `"aaabb"`                 | `{ 'a': 3, 'b': 2 }` | Yes (`'b'` has freq 2 < 3) |      `'b'` |     `["aaa", ""]` | `helper("aaa") -> ?`, `helper("") -> 0` |           `max(...)` |
| 2     | `helper("aaa")`           |         `{ 'a': 3 }` |               No (all ≥ 3) |          — |                 — |                returns `len("aaa") = 3` |                    3 |
| Final | for `"aaabb"`             |                    — |                          — |          — |                 — |                           max(3, 0) = 3 |                **3** |
"""

from typing import List
from collections import Counter

def longestSubString(s: str, k: int) -> int:
    def helper(sub: str) -> int:
        # base case
        if len(sub) < k:
            return 0
        freq = Counter(sub)
        
        # Find a splitting character whose total count < k
        for ch, cnt in freq.items():
            if cnt < k:
                # split on ch and solve each part
                parts = sub.split(ch)
                # recursively solve each non-empty part and take max
                return max(helper(part) for part in parts)
        # if we didn't find any splitting char, all chars frequency >= k
        return len(sub)
    
    return helper(sub=s)

input = "aaabb"
k = 3
print(longestSubString(s=input, k=k))