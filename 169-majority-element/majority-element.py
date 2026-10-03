class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1

            else:
                dict[num] = 1

        for val in dict:
            if dict[val] > len(nums) / 2:
                return val

        return -1
        