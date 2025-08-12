def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as prefix
    prefix = strs[0]
    
    for word in strs[1:]:
        # Shorten prefix until it matches the start of current word
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
            
    return prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))