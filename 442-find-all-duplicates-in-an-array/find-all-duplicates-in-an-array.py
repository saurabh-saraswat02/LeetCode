class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:

        new_set = set()
        lt = []

        for num in nums:
            if num in new_set:
                lt.append(num)

            else:
                new_set.add(num)

        return lt

        