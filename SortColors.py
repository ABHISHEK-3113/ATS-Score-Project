class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums) 

        # Bucket Sort  

        bucket = {0:0, 1:0, 2:0} 

        end = 0

        for i in nums:
            bucket[i] = 1 + bucket.get(i, 0)
        
        zeros = bucket[0] 
        ones = bucket[1] 
        twos = bucket[2] 

        for i in range(0, zeros):
            nums[i] = 0 
        
        for i in range(zeros, zeros+ones):
            nums[i] = 1 
        

        for i in range(zeros+ones, n):
            nums[i] = 2 
        
        # nums.sort() 
        return nums
