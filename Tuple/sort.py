def insertion(array):
    for i in range(1,len(array)):
        key = array[i]

        j = i - 1

        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return tuple(array)
value = 5,3,6,2,7,1,4
a = list(value)
print(insertion(a))