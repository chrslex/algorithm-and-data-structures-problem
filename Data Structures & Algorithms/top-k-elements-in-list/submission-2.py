class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq = heapq.heapify(nums)
        m = {}

        for num in nums:
            m[num] = m.get(num, 0) + 1
        
        temp = []

        for elm in m.items():
            heapq.heappush(temp, (elm[1], elm[0]))
        
        return [x[1] for x in heapq.nlargest(k, temp)]