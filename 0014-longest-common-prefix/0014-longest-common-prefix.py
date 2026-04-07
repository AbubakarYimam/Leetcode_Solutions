class Solution:
    def longestCommonPrefix(self, L: List[str]) -> str:
        L.sort()
        l=L
        k=""
        for i in range(len(l[0])):
    
            for j in range(len(l)):
                if l[0][i]!=l[j][i] :
                
                    return k
            k+=l[0][i]        
        return k    


                       

