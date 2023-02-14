number = int(input("enter the number: "))

temp = number
sum = 0
while temp !=0:
    digit = temp%10
    sum += digit*digit*digit
    temp = temp // 10

if sum == number:
    print("it is armstrong number")
else:
    print("it is not armstrong number")