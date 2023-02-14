def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

number = int(input("enter the number: "))

if number < 0:
    print("do not put negative numbers")
elif number == 0:
    print("factorial of 0 is 1")
else:
    print("the factorial of number is", factorial(number))