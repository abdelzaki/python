class Solution:
    def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = list()
        if not intervals:
            result.append(newInterval)
            return result
        newStart, newStop = newInterval
        for i, element in enumerate(intervals):
            start, stop = element
            if (start > newStop):
                result.append((newStart, newStop))
                result += intervals[i:]
                return result
            elif (stop < newStart):
                result.append((start, stop))
            else:
                newStart = min(newStart, start)
                newStop = max(newStop, stop)
        result.append((newStart, newStop))
        return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

intervals = []  # [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4, 8]

print(Solution.insert(intervals, newInterval))
