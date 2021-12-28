'''
https://leetcode.com/problems/string-to-integer-atoi/
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.
'''
from typing import Optional
from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # Set the variables and the const MAX, MIN
        MAX = pow(2, 31)-1
        MIN = -pow(2, 31)
        positive_signed = 1
        result = 0

        # Dealing with step 1, remove the leading whitespaces for the input string s.
        whitespace_end_index = 0
        while whitespace_end_index<len(s) and s[whitespace_end_index] == " ":
            whitespace_end_index += 1
        s = s[whitespace_end_index:]

        # If the input s has only whitespaces, return 0
        if len(s) == 0:
            return 0

        # Check if s got sign or not
        if s[0]=="-":
            positive_signed=0
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]

        # Dealing the main process, that is, concat the digits.
        i = 0
        while i < len(s) and s[i].isdigit():
            # Check if the result is going to exceed the boundary
            if (result > MAX//10) or ((result == MAX//10) and int(s[i]) > MAX%10):
                return MAX if positive_signed == 1 else MIN
            result = result*10 + int(s[i])
            i+=1

        return int(result) if positive_signed == 1 else -int(result)

def main():
    input="   42456415 fewf"
    solution = Solution()
    print(solution.myAtoi(input))


if __name__ == '__main__':
    main()