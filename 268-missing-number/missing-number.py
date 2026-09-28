class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)//2
        sum = 0
        for num in nums:
            sum += num

        return total_sum - sum
        