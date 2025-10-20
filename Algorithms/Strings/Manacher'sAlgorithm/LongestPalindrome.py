"""
Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"
    
SOLUTION: MANACHER'S ALGORITHM

TIME AND SPACE COMPLEXITY
    Time: O(n)
    Space: O(n)

s = "babad"
target transformed T = ^#b#a#b#a#d#$

| i  | T[i] | mir | initP (from mirror/min)          | expanded | P[i] | C (after) | R (after) | substr (mapped to s) |
|----|------|-----|----------------------------------|----------|------|-----------|-----------|----------------------|
| 1  | #    | -1  | -                                | 0        | 0    | 1         | 1         |                      |
| 2  | b    | 0   | -                                | 1        | 1    | 2         | 3         | b                    |
| 3  | #    | 1   | -                                | 0        | 0    | 2         | 3         |                      |
| 4  | a    | 0   | -                                | 3        | 3    | 4         | 7         | bab                  |
| 5  | #    | 3   | min(R-i=2, P[mir]=0) => 0        | 0        | 0    | 4         | 7         |                      |
| 6  | b    | 2   | min(R-i=1, P[mir]=1) => 1        | 2        | 3    | 6         | 9         | aba                  |
| 7  | #    | 5   | min(R-i=2, P[mir]=0) => 0        | 0        | 0    | 6         | 9         |                      |
| 8  | a    | 4   | min(R-i=1, P[mir]=3) => 1        | 0        | 1    | 6         | 9         | a                    |
| 9  | #    | 3   | -                                | 0        | 0    | 6         | 9         |                      |
| 10 | d    | 2   | -                                | 1        | 1    | 10        | 11        | d                    |
| 11 | #    | 9   | -                                | 0        | 0    | 10        | 11        |                      |

Notes:
- Rows show index `i` in the transformed string T = '^#b#a#b#a#d#$'.
- `initP` is the initial radius we copy from the mirror or compute with min(R - i, P[mir]) when i < R.
- `expanded` counts how many characters matched during the explicit expansion loop.
- `P[i]` is the final radius (total) at index i in T.
- `substr` maps P[i] back to the original string s by:
    start = (i - P[i]) // 2
    substring = s[start : start + P[i]]

Max P[i] = 3 occurs at i = 4 and i = 6:
- center_index = 4 -> start = (4 - 3)//2 = 0 -> s[0:3] = "bab"
- center_index = 6 -> start = (6 - 3)//2 = 1 -> s[1:4] = "aba"

Either "bab" or "aba" is a valid longest palindrome of length 3.

Final output (one valid answer): "bab"

"""
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    # Transform: add separators and sentinels
    T = '^#' + '#'.join(s) + '#$'   # e.g. '^#b#a#b#a#d#$'
    n = len(T)
    P = [0] * n
    C = 0  # center of current rightmost palindrome
    R = 0  # right boundary (index of rightmost matched char)

    for i in range(1, n - 1):  # skip the sentinels at ends
        mir = 2 * C - i
        if i < R:
            P[i] = min(R - i, P[mir])
        # expand around i with explicit bounds checking
        while (i + 1 + P[i] < n) and (i - 1 - P[i] >= 0) and (T[i + 1 + P[i]] == T[i - 1 - P[i]]):
            P[i] += 1
        # update center and right boundary
        if i + P[i] > R:
            C = i
            R = i + P[i]

    # find max
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    start = (center_index - max_len) // 2
    return s[start:start + max_len]


print(longestPalindrome(s="babad"))