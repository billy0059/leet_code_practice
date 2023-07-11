# https://leetcode.com/problems/roman-to-integer/description/
# 1. Once a left is less than a right, sum -= left, else sum += left
# 2. No matter what, the last roman character is to add for sum
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val_map = {}
        sym_val_map ['I'] = 1
        sym_val_map ['V'] = 5
        sym_val_map ['X'] = 10
        sym_val_map ['L'] = 50
        sym_val_map ['C'] = 100
        sym_val_map ['D'] = 500
        sym_val_map ['M'] = 1000
        val_list = []
        ret = 0
        for i in range(len(s)):
            val_list.append(sym_val_map[s[i]])
        for i in range(len(val_list) - 1):
            if val_list[i] < val_list[i+1]:
                ret -= val_list[i]
            else:
                ret += val_list[i]
        ret += val_list[-1]
        return ret