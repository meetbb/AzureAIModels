"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

SOLUTION: ZIGZAG TRAVERSAL

TIME: O(N)
SPACE: O(N)

| Step | Char  | cur_row  | Direction  | Row Contents                        |
|------|-------|----------|------------|-------------------------------------|
| 1    | P     | 0        | down       | ["P", "", ""]                       |
| 2    | A     | 1        | down       | ["P", "A", ""]                      |
| 3    | Y     | 2        | up         | ["P", "A", "Y"]                     |
| 4    | P     | 1        | up         | ["P", "AP", "Y"]                    |
| 5    | A     | 0        | down       | ["PA", "AP", "Y"]                   |
| 6    | L     | 1        | down       | ["PA", "APL", "Y"]                  |
| 7    | I     | 2        | up         | ["PA", "APL", "YI"]                 |
| 8    | S     | 1        | up         | ["PA", "APLS", "YI"]                |
| 9    | H     | 0        | down       | ["PAH", "APLS", "YI"]               |
| 10   | I     | 1        | down       | ["PAH", "APLSI", "YI"]              |
| 11   | R     | 2        | up         | ["PAH", "APLSI", "YIR"]             |
| 12   | I     | 1        | up         | ["PAH", "APLSII", "YIR"]            |
| 13   | N     | 0        | down       | ["PAHN", "APLSII", "YIR"]           |
| 14   | G     | 1        | down       | ["PAHN", "APLSIIG", "YIR"]          |

FINAL CONCATENATION:
    "PAHN" + "APLSIIG" + "YIR" = "PAHNAPLSIIGYIR"
    
OUTPUT: "PAHNAPLSIIGYIR"

"""
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    cur_row = 0
    going_down = False
    
    for c in s:
        rows[cur_row] += c
        # reverse direction when reaching top or bottom
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    return ''.join(rows)

print(convert(s="PAYPALISHIRING", numRows=3))