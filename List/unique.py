numbers = [6,3,5,2,7,1,4,5,2,7,1]
temp_array = []
count = 0
for ele in numbers:
    if ele not in temp_array:
        count = count + 1
        temp_array.append(ele)
print(count)