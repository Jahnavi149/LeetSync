class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x: x[0])
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
        return merged
        