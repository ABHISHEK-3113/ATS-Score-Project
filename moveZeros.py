class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n == 1:
            return [0] 

        curr = 0
        nonzero = 0 

        for curr in range(n):

            if nums[curr] != 0:
                nums[nonzero],nums[curr] = nums[curr], nums[nonzero] 
        
                nonzero += 1 
