"""
Given two arrays a and b, check if they are disjoint, i.e., there is no element common 
between both the arrays.

Example 1:
    Input: a[] = {12, 34, 11, 9, 3}, b[] = {2, 1, 3, 5}
    Output: False
    Explanation: 3 is common in both the arrays.

Example 2:
    Input: a[] = {12, 34, 11, 9, 3}, b[] = {7, 2, 1, 5}
    Output: True 
    Explanation: There is no common element in both the sets.
"""
def areDisjoint(arr1, arr2):
    """Function to check if two arrays are disjoint of each other."""
    hash_set = set()
    
    # Insert all elements of array arr1 into hash set
    for element in arr1:
        hash_set.add(element)
    
    for element in arr2:
        # If an element from arr2 is found in the hash set, arrays are not disjoint
        if element in hash_set:
            return False
    
    return True

if __name__ == "__main__":
    a = [12, 34, 11, 9, 3]
    b = [7, 2, 1, 5]
    
    if areDisjoint(arr1=a, arr2=b):
        print("True")
    else:
        print("False")