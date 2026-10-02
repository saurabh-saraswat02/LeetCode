class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        n = len(nums)

        new_set = set(nums)
        res = []

        for i in range(1, n+1):
            if i not in new_set:
                res.append(i)


        return res
       