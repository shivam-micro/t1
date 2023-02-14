from time import time

def timer(func):

    def func_wrap(*args):
        t1 = time()
        result = func(*args)
        t2 = time()
        print("function executed in ", str(float(t2-t1)) + "s")
    return func_wrap
@timer
def multiply(n):
    for i in range(1,100000):
        print(n*i)

multiply(7)