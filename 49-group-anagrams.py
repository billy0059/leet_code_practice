class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        if len(strs) == 0:
            return [[""]]
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
        '''

        #######################################################################################
        # More efficient way for the hash map key is a tuple of list, instead of sorted dict. #
        #######################################################################################
        ret_anagram_map = collections.defaultdict(list)
        for str in strs:
            anagram_id = [0] * 26 # This is the anagram ID for the string
            for c in str:
                anagram_id[ord(c) - ord("a")] += 1
            ret_anagram_map[tuple(anagram_id)].append(str)
        return ret_anagram_map.values()