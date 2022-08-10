class Solution:
    def dailyTemperaturesSlow(temperatures: list[int]) -> list[int]:
        result: list[int] = list()
        for l, v in enumerate(temperatures):
            length = len(temperatures)
            for r in range(l + 1, length):
                if temperatures[r] > v:
                    result.append(r - l)
                    break
                if r == len(temperatures) - 1:
                    result.append(0)
        result.append(0)
        return result

    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, 0, -1):
            if temperatures[i] > temperatures[i - 1]:
                result[i - 1] = 1
                continue
            j = i
            while result[j]:
                j += result[j]
                if temperatures[j] > temperatures[i -1]:
                    result[i-1] = j - i + 1
                    break
        return result


temperatures = [30,40,50,60]
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution.dailyTemperatures(temperatures))
