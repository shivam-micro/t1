number = int(input("enter the number: "))

fact = 1
if number < 0:
    print("sorry negative number")

elif number == 0:
    print("factorial = 1")

else:
    for i in range(1, number+1):
        fact = fact * i
    print("factorial of", number, "is", fact)