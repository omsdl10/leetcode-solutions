class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=prev[1]:
                prev[1]=max(prev[1],intervals[i][1])
            else:
                merged.append(prev)
                prev=intervals[i]
        merged.append(prev)
        return merged