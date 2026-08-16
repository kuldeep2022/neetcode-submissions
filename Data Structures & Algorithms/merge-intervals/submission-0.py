class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the interval with the starting value
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastEnd = output[-1][1]

            # That means they are overlapping
            if start <= lastEnd:
                output[-1][1] = max(end,lastEnd)
            else:
                output.append([start,end]) 
        
        return output

        