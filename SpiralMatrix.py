class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row = len(matrix) 
        col = len(matrix[0]) 

        ans = [] 

        rowbegin = 0 
        colbegin = 0 
        rowend = row - 1
        colend = col - 1

        while rowbegin <= rowend and colbegin <= colend:

            for i in range(colbegin, colend+1):
                ans.append(matrix[rowbegin][i]) 

            rowbegin += 1 

            for j in range(rowbegin, rowend+1):
                ans.append(matrix[j][colend]) 
            
            colend-=1 
        

            if rowbegin <= rowend:
                for j in range(colend,colbegin-1, -1):
                    ans.append(matrix[rowend][j]) 
            
            rowend -= 1 


            if colbegin <= colend:

                for j in range(rowend, rowbegin-1, -1):

                    ans.append(matrix[j][colbegin]) 

            colbegin+=1
        
        return ans
