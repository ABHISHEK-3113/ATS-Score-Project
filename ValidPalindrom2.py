class Solution:
    def validPalindrome(self, s: str) -> bool:
        cnt = 0 
        n = len(s) 

        l, r = 0, n - 1 

        while l< r:

            if s[l] == s[r]:
                l += 1 
                r -= 1 
            else:
                return self.help(s, l+1, r) or self.help(s, l, r-1)  
        
        return True 
    
    def help(self, s,i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1 
            
                j -= 1 
            else:
                return False

        return True 
