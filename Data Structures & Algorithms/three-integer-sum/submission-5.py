class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lp,rp = i + 1, len(nums)-1

            while lp < rp:
                check = nums[i] + nums[lp] + nums[rp]
                if check < 0:
                    lp += 1
                elif check > 0:
                    rp -= 1
                else:
                    res.append([nums[i], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp-1]:
                        rp -=1
                    lp += 1
                    rp -= 1
        return res 
                
                