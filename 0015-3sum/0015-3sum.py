class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res =set()

        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:

                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return [list(i) for i in res]