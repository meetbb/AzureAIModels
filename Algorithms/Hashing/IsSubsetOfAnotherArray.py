"""
Given two arrays a[] and b[] of size m and n respectively, the task is to determine 
whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

Example 1:
    Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
    Output: true
Example 2:
    Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
    Output: true
Example 3:
    Input: a[] = [10, 5, 2, 23, 19], b = [19, 5, 3] 
    Output: false
"""
def isSubset(a, b):
    """This function will have the Time Complexity: O(m + n) and Auxiliary Space: O(m)"""
    # Create a hash set and insert all elements of arr1
    hash_set = set(a)
    
    # Check each element of arr2 in the hash set
    for num in b:
        if num not in hash_set:
            return False
    
    # If all elements of arr2 are found in the hash_set
    return True

if __name__ == "__main__":
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 5, 1]
    
    if isSubset(a=a, b=b):
        print("True")
    else:
        print("False")