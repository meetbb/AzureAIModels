"""
Given two integers a and b(b!=0), the task is to return the fraction a/b in string format. If the fractional 
part is repeating, enclose the repeating part in parantheses.
Example 1:
    Input: a = 1, b = 2
    Output: "0.5"
    Explanation: 1/2 = 0.5 with no repeating part.

Example 2:
    Input: a = 50, b = 22
    Output: "2.(27)"
    Explanation: 50/22 = 2.27272727... Since fractional part (27) is repeating, it is enclosed in parentheses.
    
Approach: The idea is to first calculate the integral quotient (absolute part before decimal point) and then 
calculate the fractional part. To check if the fractional part is repeating, insert the remainder (a%b) in a 
hashmap with key as remainder and value as the index position at which this remainder occurs. If at any point 
of time, the remainder becomes zero, then there doesn't exist a repeating fraction otherwise if the remainder 
is already found in the map, then there exists a repeating fraction.
"""
def calculateRecurringDecimal(a, b):
    """Program to convert fraction to string"""
    # If the numerator is zero, answer is "0"
    if a == 0:
        return "0"
    
    # If exactly one of the numerator or denominator is negative,
    # then result will be negative
    res = "-" if (a < 0) ^ (b < 0) else ""
    
    a = abs(a) # Return the absolute value of variable
    b = abs(b)
    
    # Calculate and append the part before decimal point
    res += str(a // b)
    
    remainder = a % b
    
    if remainder == 0:
        return res
    
    res += "."
    hash_map = {}
    
    while remainder > 0:
        #If the remainder is already seen,
        # then there exists a repeating fraction.
        print(f"Default map is: {hash_map}")
        if remainder in hash_map:
            print(f"When remainder is present the res is: {res}")
            print(f"When remainder is present the first part of stringbuilder is: {res[:hash_map[remainder]]}")
            print(f"When remainder is present the second part of stringbuilder is: {res[hash_map[remainder]:]}")
            res = res[:hash_map[remainder]] + "(" + res[hash_map[remainder]:] + ")"
            break
        
        # If the remainder is seen for the first time,
        # store its index
        hash_map[remainder] = len(res)
        remainder = remainder * 10
    
        # Calculate quotient, append it to result and
        # calculate next remainder
        res += str(remainder // b)
        remainder = remainder % b
    return res

if __name__=="__main__":
    print(calculateRecurringDecimal(a=50, b=22))