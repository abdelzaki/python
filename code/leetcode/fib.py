

calls: int = 0


def fib(n: int):
    global calls
    calls += 1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n - 2)


print(fib(5))
print(calls)

calls = 0


def fibDynamic(n: int):
    global calls
    calls += 1
    result = [0] * (n + 1)
    result[0] = 0
    result[1] = 1
    result[2] = 1
    i = 2
    while i <= n:
        result[i] = result[i-1] + result[i-2]
        i += 1
    return result[n]


print("dynamic")
print(fibDynamic(5))
print(calls)
