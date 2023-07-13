class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # One line solution
        # XXXXXXXXXXXXX Do not write this XXXXXXXXXXXXX
        # return set(s) == set(t)
        # XXXXXXXXXXXXX Do not write this XXXXXXXXXXXXX
        # Above is wrong! you can not just compare the set of the string.
        # For example, "ggd", "gdd", they are not anagram but they share same set (g,d).
        char_times_dict = collections.defaultdict(int)
        for char in s:
            char_times_dict[char] += 1
        for char in t:
            char_times_dict[char] -= 1
        return set(char_times_dict.values()) == {0}