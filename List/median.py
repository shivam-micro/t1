numbers = [6,3,5,2,7,1,4]
data_sort = sorted(numbers)
data_len = len(data_sort)
middle = (data_len-1)//2
print(middle)
if middle % 2:
    print(data_sort[middle])
else:
    print((data_sort[middle] + data_sort[middle+1])/2)