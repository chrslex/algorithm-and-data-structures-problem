class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        l,r = 0, len(nums) -1
        track = {}

        for i in range(n):
            track[nums[i]] = i
        
        for i in range(n):
            if(target-nums[i] in track and i != track[target-nums[i]]):
                return [min(i, track[target-nums[i]]), max(i, track[target-nums[i]])]