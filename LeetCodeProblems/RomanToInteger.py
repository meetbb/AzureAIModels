def romanToInt(s: str) -> int:
        # A dictionary mapping Roman numeral characters to integer values. Constant time lookup
        # for every symbol.
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Accumulator variable storing the running sum (the integer result).
        total = 0
        # Loop over every index i in the string s from 0 to len(s)-1. We use indices so we
        # can look at the "next" character (s[i+1]) when needed.
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                # i + 1 < len(s) ensures we don't go out-of-bounds when accessing the next character.
                # second condition checks whether the current numeral is smaller than the next one.
                # If yes, by Roman rules this current numeral must be substracted (e.g., I in IV).
                # If both conditions true, we will subtract current value.
                total -= roman_values[s[i]]
                # In above statement, we subtract current symbol value. Example: in IV, I (1) is less than V
                # (5), so subtract 1 giving running total -1 so that after adding V you get 4.
            else:
                # If current symbol is not smaller than the next one (or there is no next symbol), add its
                # value to total.
                total += roman_values[s[i]]
        # After processing all symbols, return the integer result.
        return total
    
print(romanToInt("VVVI"))