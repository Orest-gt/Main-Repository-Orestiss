def fib(n, cache={}):
    if n in cache:
        return cache[n]
    elif n <= 1:
        cache[n] = n
    else:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

for i in range(100):
    print(fib(i))


''''''''


import time
from functools import lru_cache

time.sleep(1)

class Fibo:
    def __init__(self, epochs):
        self.epochs = epochs

    @staticmethod
    @lru_cache
    def fib_(n):
        if n <= 1:
            return n
        else:
            n = Fibo.fib_(n-1) + Fibo.fib_(n-2)
            return n

    def test(self):
        for i in range(self.epochs):
            print(Fibo.fib_(i))

epochs = int(input("\nEpochs: "))
model = Fibo(epochs)
model.test()