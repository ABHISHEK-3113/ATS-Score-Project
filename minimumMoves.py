class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums) 
        mid = n // 2
        # return 2*(nums[mid] - nums[0])
        steps = 0 
        for i in range(n): 
            steps += abs(nums[i]-nums[mid])
        return steps
