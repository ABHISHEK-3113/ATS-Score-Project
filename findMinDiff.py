class Solution:

    def findMinDiff(self, A,N,M):
        
        
        A.sort() 
        # print(A)
        min_ = float('inf')
        
        i = 0 
        
        j = M-1 
        
        while j < N:
            
            min_ = min((A[j]-A[i]), min_)
            i += 1 
            j += 1
        
        return min_ 
            
        # code here
