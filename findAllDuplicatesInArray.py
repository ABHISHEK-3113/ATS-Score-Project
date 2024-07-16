class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums) 

        hashmap = {} 

        for i in range(n): 
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)  
        
        for i in hashmap:
            if hashmap[i] > 1:
                ans.append(i) 
    
        return ans



