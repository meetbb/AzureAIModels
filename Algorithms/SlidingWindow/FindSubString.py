"""
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:

    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation:
        The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
        The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    Explanation:
        There is no concatenated substring.

Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    Explanation:
        The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
        The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
        The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

SOLUTION:
    Example:
        s = "barfoothefoobarman"
        words = ["foo","bar"]

    🗓 WALKTHROUGH TABLE:
    
    | Step | Window Start | Current Window | Words Seen        | Action                              |
    | ---- | ------------ | -------------- | ----------------- | ----------------------------------  |
    | 1    | 0            | "bar"          | {"bar":1}         | valid so far                        |
    | 2    | 3            | "foo"          | {"bar":1,"foo":1} | ✅ found all words → record index 0 |
    | 3    | 6            | "the"          | not in words      | reset window                        |
    | 4    | 9            | "foo"          | {"foo":1}         | valid so far                        |
    | 5    | 12           | "bar"          | {"foo":1,"bar":1} | ✅ found all words → record index 9 |
    | End  |              |                |                   | Output: [0, 9]                      |
"""
from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    
    res = []
    
    # We try all possible starting offsets (to align with word boundaries)
    for i in range(word_len):
        left = i
        seen = Counter()
        count = 0
        
        # Slide the window
        for j in range(i, len(s) - word_len + 1, word_len):
            word = s[j:j+word_len]
            
            if word in word_freq:
                seen[word] += 1
                count += 1
                
                # If we’ve seen too many of this word, shrink from left
                while seen[word] > word_freq[word]:
                    left_word = s[left:left+word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1
                
                # If window size equals total words → valid concatenation
                if count == word_count:
                    res.append(left)
                    
                    # Slide one word forward
                    left_word = s[left:left+word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1
            else:
                # Reset if word not found
                seen.clear()
                count = 0
                left = j + word_len
    
    return res

print(findSubstring(s="barfoothefoobarman", words=["foo","bar"]))