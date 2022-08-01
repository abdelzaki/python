class Solution:
    def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        newStart, newStop = newInterval
        result = list()
        if not intervals:
            result.append(newInterval)
            return result
        for start, stop in intervals:
            if (start > newStop ):
                result.append((newStart, newStop))
                result.append((start, stop))

            elif (stop < newStart):
                result.append((start, stop))
            else:
                newStart = min(newStart,start)
                newStop = max(newStop, stop)
                #result.append((overlapStart,overlapSopt))
        
                
            
        return result


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = [] #[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(Solution.insert(intervals, newInterval))