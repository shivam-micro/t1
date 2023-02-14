s = input("enter the string: ")

try:
    num = int(input("enter the num: "))
    print(s + num)

except (TypeError, ValueError) as e:
    print("e: ", e)