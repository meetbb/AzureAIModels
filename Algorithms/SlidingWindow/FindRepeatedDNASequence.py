"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
    
✅ Here is a walkthrough each iteration of this below function:

| Step | Window Start (`i`) | Window End (`i+9`) | Current Window (s[i:i+10]) | Seen Before?  | Action            | Seen Set (after step)    | Repeated Set (after step)            |
| ---- | ------------------ | ------------------ | -------------------------- | ------------  | ----------------- | ------------------------ | ------------------------------------ |
| 1    | 0                  | 9                  | **AAAAACCCCC**             | ❌ No         | Add to `seen`     | {AAAAACCCCC}             | ∅                                    |
| 2    | 1                  | 10                 | **AAAACCCCCA**             | ❌ No         | Add to `seen`     | {AAAAACCCCC, AAAACCCCCA} | ∅                                    |
| 3    | 2                  | 11                 | **AAACCCCCAA**             | ❌ No         | Add to `seen`     | {..., AAACCCCCAA}        | ∅                                    |
| 4    | 3                  | 12                 | **AACCCCCAAA**             | ❌ No         | Add to `seen`     | {..., AACCCCCAAA}        | ∅                                    |
| 5    | 4                  | 13                 | **ACCCCCAAAA**             | ❌ No         | Add to `seen`     | {..., ACCCCCAAAA}        | ∅                                    |
| 6    | 5                  | 14                 | **CCCCCAAAAA**             | ❌ No         | Add to `seen`     | {..., CCCCCAAAAA}        | ∅                                    |
| 7    | 6                  | 15                 | **CCCCAAAAAC**             | ❌ No         | Add to `seen`     | {..., CCCCAAAAAC}        | ∅                                    |
| 8    | 7                  | 16                 | **CCCAAAAACC**             | ❌ No         | Add to `seen`     | {..., CCCAAAAACC}        | ∅                                    |
| 9    | 8                  | 17                 | **CCAAAAACCC**             | ❌ No         | Add to `seen`     | {..., CCAAAAACCC}        | ∅                                    |
| 10   | 9                  | 18                 | **CAAAAACCCC**             | ❌ No         | Add to `seen`     | {..., CAAAAACCCC}        | ∅                                    |
| 11   | 10                 | 19                 | **AAAAACCCCC**             | ✅ Yes        | Add to `repeated` | {..., CAAAAACCCC}        | {AAAAACCCCC}                         |
| 12   | 11                 | 20                 | **AAAACCCCCA**             | ✅ Yes        | Add to `repeated` | {...}                    | {AAAAACCCCC, AAAACCCCCA}             |
| 13   | 12                 | 21                 | **AAACCCCCCA**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| 14   | 13                 | 22                 | **AACCCCCCAA**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| 15   | 14                 | 23                 | **ACCCCCCAAA**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| 16   | 15                 | 24                 | **CCCCCCAAAA**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| 17   | 16                 | 25                 | **CCCCCAAAAA**             | ✅ Yes        | Add to `repeated` | {...}                    | {AAAAACCCCC, CCCCCAAAAA, AAAACCCCCA} |
| 18   | 17                 | 26                 | **CCCCAAAAAG**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| 19   | 18                 | 27                 | **CCCAAAAAGG**             | ❌ No         | Add to `seen`     | {...}                    | {...}                                |
| ...  | ...                | ...                | ...                        | ...           | ...               | ...                      | ...                                  |

"""
def findRepeatedDNASequence(s: str) -> list[str]:
    if len(s) < 10:
        return []
    
    seen = set() # stores every distinct 10-letter substring
    repeated = set() # stores those substrings that occur more than once.
    n = len(s)
    
    for i in range(n - 9): # i goes from 0 to n-10 inclusive
        subseq = s[i:i+10] # substring of length 10
        if subseq in seen:
            repeated.add(subseq) # seen before → it's a repeated sequence
        else:
            seen.add(subseq) # first time we see it
    
    return list(repeated)

print(findRepeatedDNASequence(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

"""
A Sliding Window is a subarray or substring that moves through a larger array/string one element at a time.
We use it when:
    1. We need to analyse contiguous parts of a sequence (string, list, array).
    2. The window size is fixed or dynamically adjusted as we iterate.
Think of it like scanning DNA through a microscope - you look at 10 bases at a time, slide one step forward,
and look again.

🔹 Pattern 1: Fixed-length substring/subarray analysis
    "Find all subarrays/substrings of length k that satisfy X."
    
    ✅ Examples:
    
        👉 Find all 10-letter substrings that repeat.
        👉 Find the maximum sum of any subarray of size k.
        👉 Count substrings of length k with distinct characters.

🔹 Pattern 2: Variable-length condition that depends on a range
    "Find the longest/shortest substring that satisfies a condition."
    
    ✅ Examples:
        👉 Longest substring with at most K distinct characters.
        👉 Smallest window containing all characters of another string.
        👉 Longest substring without repeating characters.

🔹 Pattern 3: Continuous/Overlapping sequences
    "We need to check every overlapping segment in order."
    
    ✅ Example:
        👉 In the DNA problem above, we want every overlapping 10-letter sequence - "AAAAACCCCC" overlaps with
        "AAAACCCCCA".
        If the subranges are overlapping, not disjoint, a sliding window is almost always right.

🔹 Pattern 4: Need for O(n) time on contiguous data
    "If a naive approach would take O(n*k) by re-checking overlapping elements, and you can reuse part of the
    previous window's work → Sliding window reduces it to O(n)."
    
    ✅ Example:
        👉 Recomputing substring hash every time → O(n*k)
        👉 But if we "slide" the hash, adding one char and removing one → O(n)

🔹 Pattern 5: Input is a linear sequence (String, List, Array)
    If the problem revolves around continuous data like:
        👉 Strings (DNA, words, etc.)
        👉 Arrays of numbers
        👉 Streams of characters/data
    and the task is about segments of it → Sliding Window often fits perfectly.
"""