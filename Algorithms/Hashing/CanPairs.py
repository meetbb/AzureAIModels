"""
CHECK IF ARRAY PAIR SUMS DIVISIBLE BY K

Given an array of integers and a number k, write a function that returns true if the given array can be 
divided into pairs such that the sum of every pair is divisible by k.

Example 1:
    Input: arr[] = [9, 7, 5, 3], k = 6
    Output: True
    Explanation: We can divide the array into (9,3) and (7,5). Sum of both of these pairs is a multiple of 6.

Example 2:
    Input: arr[] = [91, 74, 66, 48], k=10
    Output: False
"""
def can_pairs(arr, k):
    """Function to find pairs in arr which can be divided by k"""
    if len(arr) % 2 != 0:
        return False
    
    frequency = [0] * k
    print(f"Frequency is: {frequency}")
    for x in arr:
        print(f"value of x is: {x}")
        remainder = x % k
        print(f"Value of remainder is: {remainder}")
        # If the complement of the current remainder exists in frequency, decrement its count
        print(f"Complement of the remainder in frequency is: {frequency[(k - remainder) % k]}")
        if frequency[(k - remainder) % k] != 0:
            frequency[(k - remainder) % k] -= 1
        else:
            # Otherwise, increment the count of the current remainder
            frequency[remainder] += 1
        print(f"Frequency in iteration is: {frequency}")
    
    # Check if all elements in the frequency array are 0
    print(f"Frequency after iteration is: {frequency}")
    for count in frequency:
        if count != 0:
            return False
    
    return True

if __name__=="__main__":
    arr = [92,75,65,48,45,35]
    k=10
    print("True" if can_pairs(arr=arr, k=k) else "False")