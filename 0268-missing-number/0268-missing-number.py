class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range (0,nums[-1]+1):
            if i not in nums:
                return i
        return i+1        