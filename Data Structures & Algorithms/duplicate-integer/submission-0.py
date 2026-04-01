class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        count = set()

        for i in range(n):
            if(nums[i] in count) :
                return True
            else:
                count.add(nums[i])
        return False