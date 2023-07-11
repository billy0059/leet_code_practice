'''
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # There are two cases of palindrome, ODD and EVEN.
        # "Expand from Center" to get the logest palinfrome length for "each char", need to consider two cases.
        s_len = len(s)
        longestPalindrome_length=0
        ret_string=""
        logest_palindrome_start_index=0
        for i in range(s_len):
            temp_len = max(self.get_longest_palindrome_len_from_center(s,i,i), self.get_longest_palindrome_len_from_center(s,i,i+1))
            if temp_len > longestPalindrome_length:
                print("Longer palindrome found!")
                longestPalindrome_length = temp_len
                logest_palindrome_start_index = i - (longestPalindrome_length-1) // 2
                print("longestPalindrome_length = " + str(longestPalindrome_length))
        return s[logest_palindrome_start_index : logest_palindrome_start_index + longestPalindrome_length]


    def get_longest_palindrome_len_from_center(self, s: str, l: int, r: int) -> int:
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return (r-1) - (l+1) + 1


def main():
    s="babad"
    solution = Solution()
    print(solution.longestPalindrome(s))


if __name__ == '__main__':
    main()