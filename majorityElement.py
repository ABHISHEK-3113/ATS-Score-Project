class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums) 

        count = {} 
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        

        for i in count:
            if count[i] > (n//2):
                return i 
        
