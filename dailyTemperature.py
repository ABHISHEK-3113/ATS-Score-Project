class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T) 
        ans = [0]*n 
        stack = []

        for i, t in enumerate(T): 

            while stack and T[stack[-1]] < t:
                curr = stack.pop() 
                ans[curr] = i - curr 
            
            stack.append(i)
        
        return ans
        
