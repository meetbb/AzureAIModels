"""
Given two arrays, a and b of equal length. The task is to determine if the given arrays are 
equal or not. Two arrays are considered equal if:
1. Both arrays contain the same set of elements may be different.
2. The arrangements (or permutations) of elements may be different.
3. If there are repeated elements, the counts of each element must be the same in both arrays.

Example 1:
    Input: a[] = {1, 2, 5, 4, 0}, b[] = {2, 4, 5, 0, 1}
    Output: True
Example 2:
    Input: a[] = {1, 7, 1}, b[] = {7, 7, 1}
    Output: False
"""
def checkEqual(arr1, arr2):
    """Function to check if two arrays are equal or not."""
    n, m = len(arr1), len(arr2)
    if n != m:
        return False
    
    hash_map = {}
    for num in arr1:
        hash_map[num] = hash_map.get(num, 0) + 1
    
    for num in arr2:
        if num not in hash_map:
            return False
        if hash_map[num] == 0:
            return False
        hash_map[num] -= 1
    return True

if __name__=="__main__":
    a = [1, 7, 1]
    b = [7, 7, 1]
    
    if checkEqual(arr1=a, arr2=b):
        print("True")
    else:
        print("False")