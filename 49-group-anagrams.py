class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return [[""]]
        str_anagram_map_list=[]
        return_map=collections.defaultdict(list)
        for str in strs:
            anagram_map = collections.defaultdict(int)
            # Use the dict, key is the dict, which represent the anagram ID,
            # while value stands for the strings list, which is the answer
            for c in str:
                anagram_map[c] += 1
            # A dict can be a key in another dict if you
            # First sort the dict with "sorted(dict.item())" and make it tuple:
            # tuple(sorted(dict.items()))
            return_map[tuple(sorted(anagram_map.items()))].append(str)
        return return_map.values()