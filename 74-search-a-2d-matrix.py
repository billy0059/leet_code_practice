class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]: # The target is in this row, do binary search in this row
                ### Memorize binary search!!! ###
                ### Memorize binary search!!! ###
                ### Memorize binary search!!! ###
                l, r = 0, len(row)-1
                while l<=r:
                    mid = (l+r) // 2
                    if target > row[mid]:
                        l = mid + 1
                    elif target < row[mid]:
                        r = mid - 1
                    else:
                        return True
                ### Memorize binary search!!! ###
                ### Memorize binary search!!! ###
                ### Memorize binary search!!! ###
            else: # The target is bigger than this row, moving to next row
                continue
        return False