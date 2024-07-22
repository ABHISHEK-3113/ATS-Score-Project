class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = [] 
        

        n = len(strs) 
        if n == 0:
            return "" 

        
        reference = strs[0]

        for i in range(1, len(strs)):

            while strs[i].find(reference) != 0:
                reference = reference[0 : len(reference) -1]  
            
                if reference == "":
                    return "" 
        
        return reference
