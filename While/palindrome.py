number = int(input("enter the number: "))

temp = number
rev = 0
while number > 0 :
    dig = number % 10
    print(dig)
    rev = rev*10 + dig
    number = number // 10
    print(number)

if temp==rev:
    print("palindrome")

else:
    print("not palindrome")