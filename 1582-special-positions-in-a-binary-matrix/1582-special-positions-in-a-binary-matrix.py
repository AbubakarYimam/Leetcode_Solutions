class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        t = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    g = 0
                    for k in range(len(mat[0])):
                        if mat[i][k] == 1:
                            g += 1
                    for k in range(len(mat)):
                        if mat[k][j] == 1:
                            g += 1        
                    
                    if g == 2:
                        t += 1        
        return t