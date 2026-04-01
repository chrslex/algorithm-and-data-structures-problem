class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            if num-1 in numSet:
                continue
            temp = 0
            curr = num
            while curr in numSet:
                temp += 1
                curr +=1
            res = max(res, temp)
        return res
        