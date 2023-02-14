def most_frequent(array):
    counter = 0
    num = array[0]

    for i in array:
        curr_frequency = array.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

array = [2, 1, 2, 2, 1, 3,4,3,3,3]
print(most_frequent(array))
