class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums) 
        table = [0]*(n+1) 

        for i in nums:
            
            if not table[i]:
                table[i] = 1 
            else:
                ans.append(i) 
            
        # print(table)
        return ans


        # hashmap = {} 

        # for i in range(n): 
        #     hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)  
        
        # for i in hashmap:
        #     if hashmap[i] > 1:
        #         ans.append(i) 
    
        # return ans

 

