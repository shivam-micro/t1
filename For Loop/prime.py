lower = int(input("enter the lower number: "))

upper = int(input("enter the upper number: "))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)