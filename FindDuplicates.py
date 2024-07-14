class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 


        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 

            if slow == fast:
                break 
            
        slow2 = 0 

        while True:
            slow = nums[slow] 
            slow = nums[slow2] 

            if slow == slow2:
                break 
            
        return slow 



        # map_ = {} 
        # n = len(nums) 
        # for i in range(n):
        #     map_[nums[i]] = 1 + map_.get(nums[i], 0) 
        
        # for i in map_:
        #     if map_[i] > 1:
        #         return i 
        
