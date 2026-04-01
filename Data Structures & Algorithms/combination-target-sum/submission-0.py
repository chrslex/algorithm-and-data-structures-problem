class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums, target, temp):
            if sum(temp) > target:
                return
            if sum(temp) == target:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                backtrack(nums[i:], target, temp)
                temp.pop()

        backtrack(nums, target, [])
        return res