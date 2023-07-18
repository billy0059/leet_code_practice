class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window problem with the check condition : Permutation ID
        s1_id = [0 for i in range(26)]
        for c in s1:
            s1_id[ord(c)-ord("a")] += 1
        window_id = [0 for i in range(26)]
        l = 0
        for r in range(len(s2)):
            window_id[ord(s2[r])-ord("a")] += 1
            if window_id == s1_id:
                return True
            else:
                while window_id[ord(s2[r])-ord("a")] - s1_id[ord(s2[r])-ord("a")] > 0:
                    window_id[ord(s2[l])-ord("a")] -= 1
                    l+=1
        return False