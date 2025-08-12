"""
THE PROBLEM:
You are given a string s and a pattern p. The pattern contains:
    1. normal lowercase letters (match themselves),
    2. . which matches any single character, and
    3. * which matches zero or more of the preceding element (the character just before *, which could be a normal letter or .)

The match must cover the entire input string s (not a substring). You must decide whether s matches p.
"""
# The approach used (Dynamic Programming)
# We use bottom-up dynamic programming with the key idea:
# Define dp[i][j] as a boolean:
# Does s[i:] (the substring from index i to end) match p[j:] (pattern from index j to end)?
# We want the answer dp[0][0]
def isMatch(s: str, p: str) -> bool:
        # Create a table with (len(s)+1) rows and (len(p)+1) columns. Index i runs 0..len(s) where
        # i==len(s) represents the empty suffix of s. Similarly for j and p.
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # Empty String matches empty pattern
        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
                    
        return dp[0][0]