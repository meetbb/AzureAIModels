"""
Given an integer n, for every positive integer i <= n, the task is to print,

"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3,
"Buzz" if i is divisible by 5
"i" as a string, if none of the conditions are true.

Example:
    Input n = 20
    Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"]
"""
def fizBuzz(n):
    """Function for FizzBuzz problem by checking every integer individually with hashing"""
    result = []
    
    # Dictionary to store all FizzBuzz mappings.
    hash_map = {3: "Fizz", 5: "Buzz"}
    divisors = [3, 5]
    
    for i in range(1, n + 1):
        value = ""
        for d in divisors:
            # If the i is divisible by d, add the corresponding string mapped with d
            if i % d == 0:
                value += hash_map[d]
        
        # Not divisible by 3 or 5, add the number
        if not value:
            value += str(i)
            
        # Append the current answer str to the result list
        result.append(value)
    
    return result

if __name__=="__main__":    
    result = fizBuzz(n=20)
    for s in result:
        print(s, end=" ")