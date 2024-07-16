class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        for i in range(len(haystack) - len(needle)+1):
            if (haystack[i: i+len(needle)] == needle):
                return i
        return -1
        
        ans = -1 
        n = len(needle)
        m = len(haystack) 

        if m < n:
            return - 1 

        x = 0 

        while x < m :

            y = 0
            j = x 

            while x < m and y < n and haystack[x] == needle[y]:
                x += 1 
                y += 1 


                if y == n:
                    return x-y 

            

            x = j + 1 
        
        return -1
       
