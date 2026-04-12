class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        # heap
        temp = []
        for key, v in d.items():
            heapq.heappush(temp, (v,key))

        return [x[1] for x in heapq.nlargest(k, temp)]