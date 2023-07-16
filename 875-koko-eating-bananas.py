class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        # Given array : [3, 6, 7, 11], and speed = k
        # Time needed : 3//k(+1 if 3%k!=0) + 6//k + 7//k + 11//k

        # Idea: Do binary search on every speed candidates (1~max(piles))
        #       Each k in speed candidates will have a corresponding h, and
        #       the bigger the k is, the smaller the h would be neeed. (faster speed, fewer time needed)
        #       The goal is to find the minimum speed we need.
        #       (Let's say if the speed K1 needs H1 to finish eating, if H1 < given H, then K1 is OK for the requirement.)
        def calculate_h(k: int, piles: list[int] ) -> int: # To calculate the needed H for speed k
            total_h = 0
            for p in piles:
                total_h += math.ceil(p/k)
            print (k, total_h)
            return total_h
        # Start doing binary search on speed candidates (1~max(piles)), target would be "less than h"
        l, r = 1, max(piles)
        ret_k = max(piles) # Set the return speed to maximum for the init.
        while l<=r: # Loop the binary search process
            mid = l + (r-l)//2 # (l+r)//2 --> This would cause memory limit exceeded problem
            if calculate_h(mid, piles) <= h: # HIT! The speed is OK for the given hour
                ret_k = min(ret_k, mid) # We want the speed to be as small as it can be.
                r = mid - 1 # We want to see if there is smaller speed could satisfy the given hour,
                            # so set the right bound to mid-1 (degrade the possible maximum speed)
            else: # Speed is too slow, increase the speed to mid+1
                l = mid + 1

        return ret_k

        '''
        Brute force solution, time complexity is bad
        for k in range(1, max(piles)):
            total_time = 0
            for num in piles:
                if num % k != 0:
                    total_time += num//k + 1
                else:
                    total_time += num//k
            if total_time == h:
                return k
        '''
