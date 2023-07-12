class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_nums1 = 0
        for i in range(n): # Start with the number in nums2
            while (nums2[i] > nums1[index_nums1]) and (index_nums1 < m+i):
                # If the number is bigger than the number in nums1, add index value for nums1
                # m+i is because the length of nums1 would increase once a number in nums2 has
                # been inserted to nums1
                index_nums1 += 1
            if index_nums1 == m+i: # If the index of nums1 is now equal the length of nums1, append the rest number in nums2 to nums1 and finish the task!
                nums1[index_nums1:] = nums2[i:]
            else: # Insert the value, first we need to shift the value in nums1
                nums1[index_nums1+1:m+i+1] = nums1[index_nums1:m+i-1+1]
                # This is important in python!!!
                # --> a[start:stop]  # items start "through stop-1"
                # If you with include stop, "ADD 1 FOR IT!!""

                nums1[index_nums1] = nums2[i] # Insert the value
