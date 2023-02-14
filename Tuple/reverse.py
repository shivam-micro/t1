numbers = (6,3,5,2,7,1,4)
numbers = list(numbers)
last_num = len(numbers) - 1
for i in range(int(len(numbers)/2)):
    numbers[i], numbers[last_num-i] = numbers[last_num-i], numbers[i]

print(tuple(numbers))

