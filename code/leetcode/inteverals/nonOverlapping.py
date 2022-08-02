class Solution:
    def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        # sort the list
        intervals.sort()
        oldsize = len(intervals)
        if oldsize == 0:
            return 0
        nonOverlap: list[list[int]] = list()
        oldStart, oldEnd = intervals[0]
        for i, element in enumerate(intervals):
            start, end = element
            if start >= oldEnd:
                nonOverlap.append((oldStart, oldEnd))
                oldStart, oldEnd = start, end
                if i == oldsize - 1:
                    nonOverlap.append((oldStart, oldEnd))
                    return oldsize - len(nonOverlap)
            else:
                if end < oldEnd:
                    oldStart, oldEnd = start, end

        if not nonOverlap:
            return 1
        if nonOverlap[-1][1] <= start:
            nonOverlap.append((start, end))
        
        return oldsize - len(nonOverlap)


intervals = [[1, 2], [1, 2], [1, 2]]
#intervals = [[1, 2], [2, 3]]
print(Solution.eraseOverlapIntervals(intervals))
