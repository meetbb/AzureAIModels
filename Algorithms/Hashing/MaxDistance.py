"""
Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.

Example: 
    Input: a[] = [1,1,2,2,2,1]
    Output: 5
    Explanation: distance for 1 is 5-0=5, distance for 2 is: 4-2=2, So max distance is 5.
"""
def maxDistance(arr):
    """Program to find max distance between two occurrences in array using hashing"""
    hash_map = {}
    result = 0
    
    for i in range(len(arr)):
        # If this is the first occurrence of the element, store its index
        if arr[i] not in hash_map:
            hash_map[arr[i]] = i
        else:
            # Else update max distance
            result = max(result, i - hash_map[arr[i]])
    return result

if __name__=="__main__":
    array = [1,1,2,2,2,1]
    print(maxDistance(arr=array))