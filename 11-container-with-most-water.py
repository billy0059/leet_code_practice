'''
https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''
from typing import Optional
from typing import List

class Solution:
    # "Time Limit Exceeded" solution... (brute force)
    def maxArea(self, height: List[int]) -> int:
        def area(w, h) -> int:
            return w * h
        res=0
        for i in range (len(height)-1):
            for j in range(i+1, len(height)):
                tmp_area = area(j-i, min(height[i], height[j]))
                if tmp_area > res:
                    res = tmp_area
        return res

    # Solution 2, Start with the longest WIDTH
    def maxArea(self, height: List[int]) -> int:
        def area(w, h) -> int:
            return w * h
        res=0
        i = 0
        j = len(height)-1
        while i<j:
            res = max(res, area(j-i, min(height[i], height[j])))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res

    # Optimization: Start with the longest WIDTH, if the next height is less or equal the previous one, skip it.
    def maxArea(self, height: List[int]) -> int:
        def area(w, h) -> int:
            return w * h
        res=0
        i = 0
        j = len(height)-1
        while i<j:
            tempHeight = min(height[i], height[j])
            res = max(res, area(j-i, tempHeight))
            if height[i]<height[j]:
                while i<j and height[i]<=tempHeight:
                    i+=1
            else:
                while i<j and height[j]<=tempHeight:
                    j-=1
        return res

def main():
    input=[1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(input))

if __name__ == '__main__':
    main()