class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_ = defaultdict() 
        n = len(nums)

        for i in range(n):
            map_[nums[i]] = i 
        

        for i in range(n):
            if target - nums[i] in map_ and map_[target - nums[i]] != i:
                return [i, map_[(target - nums[i])]]
        
