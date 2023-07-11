'''
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from typing import Optional
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ret = []
        def genPar(ret: List[str], l: int, r: int, par: str):
            if (l==0 and r==0):
                ret.append(par)
                return
            if l > 0:
                genPar(ret, l-1, r, par + '(')
            if l < r:
                genPar(ret, l, r-1, par + ')')
        genPar(ret, n, n, "")
        return ret

def main():
    n=3
    solution = Solution()
    print(solution.generateParenthesis(n))


if __name__ == '__main__':
    main()