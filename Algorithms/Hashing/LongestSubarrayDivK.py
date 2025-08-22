"""
Given an arr[] containing n integers and a positive integer k, the problem is to 
find the longest subarray's length with the sum of the elements divisible by k.

Example 1:
    Input: arr[] = [2, 7, 6, 1, 4, 5], k = 3
    Output: 4
    Explanation: The subarray [7, 6, 1, 4] has sum = 18, which is divisible by 3.
Example 2:
    Input: arr[] = [-2, 2, -5, 12, -11, -1, 7], k = 3
    Output: 5
    Explanation: The subarray [2, -5, 12, -11, -1], has sum = -3, which is divisible by 3.
"""
def longestSubarrayDivK(arr, k):
    size = len(arr)
    print(f"Array size is: {size}\n\n")
    result = 0
    prefIdx = {}
    sum = 0
    
    # Iterate over all ending points
    for i in range(size):
        print(f"value of 'i' is: {i}")
        print(f"value of 'k' is: {k}")
        # prefix sum mod k
        print(f"value of 'arr[i]' is: {arr[i]}")
        print(f"value of 'sum' before mod is: {sum}")
        sum = (sum + arr[i]) % k
        print(f"value of 'sum' is: {sum}")
        # If sum == 0, then update result with the length of subarray arr[0...i]
        if sum == 0:
            result = i + 1
            print(f"value of 'result' when sum is zero: {result}")
        elif sum in prefIdx:
            # Update max length for repeating sum
            print(f"value of 'sum' is present in prefIdx: {prefIdx[sum]}")
            result = max(result, i - prefIdx[sum])
            print(f"value of 'result' when sum is not zero: {result}")
        else:
            # Store the first occurrence of sum
            prefIdx[sum] = i
            print(f"value of 'prefIdx[sum]' is: {i}")    
        print(f"value of current 'prefIdx' is: {prefIdx}")
        print("---------------------------------------------")
    print(f"Final result is: {result}")
    return result

if __name__=="__main__":
    arr = [2, 7, 6, 1, 4, 5]	
 
    print(longestSubarrayDivK(arr=arr, k=3))