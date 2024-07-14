class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        ans = 0 
        pre = 0 

        cnt = Counter() 

        for i in nums: 

            pre += i 

            if pre % k == 0: ans += 1 

            ans += cnt[pre % k] 

            cnt[pre % k] += 1 
        

        return ans
