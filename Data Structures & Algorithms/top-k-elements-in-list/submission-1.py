import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            d[nums[i]] = 1 + d.get(nums[i], 0)

        heap = []
        for num in d.keys():
            hq.heappush(heap, (-d[num], num))
            # if(len(heap) > k):
            #     hq.heappop(heap)

        res = []
        for i in range(k):
            res.append(hq.heappop(heap)[1])
        return res