class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window with the loop :
        # 1. Check after adding "new char" to the window set, the set would be valid:
        #    To achieve that, remove "new char" in the set if exists. (remove s[l]; l+=1)
        # 2. Add new char to the set and calculate the window size (r-l+1)
        # 3. Compare the size with previous one
        # 4. To next round, back to 1.
        l = 0
        ret_max_len = 0
        window_set = set()
        for r in range(len(s)):
            while s[r] in window_set: # First remove all s[r] in the set,
                                      # This is to make sure that the window will be valid after adding s[r]
                window_set.remove(s[l])
                l+=1
            window_set.add(s[r]) # Since we have eliminate all s[r] in advance,
                                 # window is going to be valid after adding s[r]
            ret_max_len = max(ret_max_len, r-l+1) # Compare the window size with the previous one.
        return ret_max_len