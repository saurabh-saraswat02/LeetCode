class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)

        if n%2 != 0:
            return float(num[n//2])
        else:
            return float((num[n//2-1] + num[n//2])/2)
