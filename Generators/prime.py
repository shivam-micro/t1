def prime(n):
    if n > 1:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0 :
                yield "not prime"
            else:
                yield n, "is a prime number"
g = next(prime(7))

#p=[i for i in g]
print(g)