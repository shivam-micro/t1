numbers = (6,3,5,2,7,1)

max = min = numbers[0]

for i in range(1,len(numbers)):
    if numbers[i] > max:
        max = numbers[i]

    elif numbers[i] < min:
        min = numbers[i]

print(max, min)