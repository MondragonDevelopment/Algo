"""
O(n^2) time | O(n) space
def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n-1) + fib(n-2)

O(n) time | O(n) space
def fib(n, memoize = {0:0, 1:1}):
    if n in memoize: return memoize[n]
    else:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
        return memoize[n]
"""

# O(n) time | O(1) space
def fib(n):
    lastTwo = [0, 1]
    counter = 2
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n >0 else 0

print(fib(7))