class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num-1 in nums_set:
                continue
            temp = 0
            curr = num
            while curr in nums_set:
                temp += 1
                curr += 1
            res = max(res, temp)
        return res