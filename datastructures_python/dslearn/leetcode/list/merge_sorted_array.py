
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:m]
        j = 0
        for i in range(m,m+n,1):
            nums1[i] = nums2[j]
            j=j+1

        nums1.sort(reverse=False)
        print(nums1)

solution = Solution()

solution.merge(nums1,m,nums2,n)