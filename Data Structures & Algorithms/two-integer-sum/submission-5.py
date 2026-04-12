class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if target-nums[i] in d:
                idx = d[target-nums[i]]
                return [min(idx, i), max(idx,i)]
            else:
                if nums[i] not in d:
                    d[nums[i]] = i