terms = int(input("how many terms: "))
a, b = 0, 1
count = 0

if terms<=0:
    print("enter number greater than 0")

elif terms == 1:
    print("a = 0")
else:
    while count < terms:
        print(a)
        sum = a + b
        a = b
        b = sum
        count += 1