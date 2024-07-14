class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums) 

        r = 1


        for i in range(1, n):

            if nums[i] != nums[i-1]:

                nums[r] = nums[i] 
                r += 1 
        

        return r 



