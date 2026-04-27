class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        l=""
        for i in d:
            l+=str(i)
        j=int(l)+1
        j=list(str(j))
        return [int(i) for i  in j]  