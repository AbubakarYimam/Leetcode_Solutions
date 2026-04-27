class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]>=0:
                l.append(nums[i])
                nums[i]=-1
        for i in range(len(nums)):
            if nums[i]%2==1 and nums[i]>0:
                l.append(nums[i])
        return l         
                       
