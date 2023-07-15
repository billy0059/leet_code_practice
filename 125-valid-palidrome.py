class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        check = []
        for c in s:
            if c.isalpha() or c.isnumeric():
                # or we can simply use isalnum.()
                check.append(c.lower())
        i = 0
        j = len(check) -1
        while i<j:
            if check[i] != check[j]:
                return False
            i+=1
            j-=1
        return True
        '''
        ###########################################################
        # Follow up : do not use build-in function to determine if
        # a char is alphanumeric. And no more space needed (O(1))
        ###########################################################
        def ifalphanumeric (c) -> bool:
            return ord("0") <= ord(c) <= ord("9") or ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z")

        i=0
        j=len(s) - 1
        while i<j:
            while ifalphanumeric(s[i]) != True and i<j:
                i += 1
            while ifalphanumeric(s[j]) != True and i<j:
                j -= 1
            if ord("0") <= ord(s[i]) <= ord("9") or ord("0") <= ord(s[j]) <= ord("9"):
                # for the numeric cases
                if ord(s[i]) != ord(s[j]):
                    return False
                else:
                    i+=1
                    j-=1
            elif s[i] == s[j] or ord(s[i]) - ord("a") == ord(s[j]) - ord("A") or ord(s[i]) - ord("A") == ord(s[j]) - ord("a"):
                # for the letters (alpha) cases
                i+=1
                j-=1
            else:
                return False

        return True
