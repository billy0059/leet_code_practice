# Similar to the phone-screen-longest-holiday.py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a map, which the value is the occur times of key (char), aim to find the most frequent char
        # Valid window condition : (r-l+1) - most_freq <= quota (k)
        window_char_times_map = {}
        most_freq = 0
        ret_max = 0
        l = 0
        repeat_char = s[0]
        for r in range(len(s)):
            window_char_times_map[s[r]] = window_char_times_map.get(s[r], 0) + 1
            most_freq = max(most_freq, window_char_times_map[s[r]])
            if (r-l+1) - most_freq <= k: # Valid, compare the current window size with previous max
                ret_max = max(ret_max, (r-l+1))
            else: # Update l, map to make the window valid
                window_char_times_map[s[l]] -= 1
                l = l+1
        return ret_max
