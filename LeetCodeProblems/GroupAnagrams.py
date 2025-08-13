"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Here, key: anagram signature, value: list of words
    groups = defaultdict(list)
    
    for word in strs:
        # Build a 26-length frequency signature for "a...z"
        print(f"\nCurrent word: {word}")
        counts = [0] * 26
        print(f"Counts default array is: {counts}")
        for ch in word:
            print(f"---Character is: {ch}")
            counts[ord(ch) - ord('a')] += 1
            print(f"Count array with new ch is: {counts}")
        # lists aren't hashable; tuples are
        key = tuple(counts)
        print(f"key is: {key}")
        groups[key].append(word)
    return list(groups.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))