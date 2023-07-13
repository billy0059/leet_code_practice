class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # One line solution
        # return set(s) == set(t)
        char_times_dict = collections.defaultdict(int)
        for char in s:
            char_times_dict[char] += 1
        for char in t:
            char_times_dict[char] -= 1
        return set(char_times_dict.values()) == {0}