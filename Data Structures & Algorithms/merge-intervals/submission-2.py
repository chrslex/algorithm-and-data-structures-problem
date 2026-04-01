class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x : x[0])
        result = [intervals[0]]
        n = len(intervals)
        print(intervals)

        for i in range(1, n):
            start = result[-1][0]
            end = result[-1][1]

            if intervals[i][0] <= end:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result

        