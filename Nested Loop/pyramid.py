x = int(input("enter the row number: "))
y = x - 1
for i in range(x):
    for j in range(y):
        print(" ",end ="")
    y = y - 1
    for j in range(i+1):
            print("*",end =" ")
    print("")