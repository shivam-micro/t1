def fib(a=0,b=1):
    while True:
        yield a
        a,b = b, a+b

f = fib()
print(', '.join(str(next(f)) for i in range(10)))