class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        numset = set()

        for i in range(n):
            if nums[i] in numset:
                return True
            else:
                numset.add(nums[i])
        return False