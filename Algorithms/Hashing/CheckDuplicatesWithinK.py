"""
Given an integer array arr[] and an integer k, determine whether there exist two indices i and j 
such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

Example 1:
    Input: k = 3, arr[] = [1,2,3,4,1,2,3,4]
    Output: No
    Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.
    
Example 2:
    Input: k = 3, arr[] = [1,2,3,1,4,5]
    Output: Yes
    Explanation: 1 is present at index 0 and 3.
"""
def check_duplicates_within_k(arr, k):
    # Creates an empty list
    mySet = set()
    print(f"My initial set is: {mySet}")
    print(f"Array Length is: {len(arr)}")
    # Traverse the input array
    for i in range(len(arr)):
        # If already present in hash, then we found a duplicate within k distance
        print(f"Item at ith index is: {arr[i]}")
        if arr[i] in mySet:
            print(f"Item at ith index is: {arr[i]} present in my set")
            return True
        
        # Add this item in hashset
        mySet.add(arr[i])
        # Remove the k+1 distant item
        print(f"i value is: {i}")
        print(f"My current set is: {mySet}")
        if (i >= k):
            print(f"i minus k is: {i-k}")
            print(f"Item to be removed from set is: {arr[i-k]}")
            mySet.remove(arr[i - k])
        print(f"My set after deletion is: {mySet}")    
    return False

arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if check_duplicates_within_k(arr, 3) else "No")