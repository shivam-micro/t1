def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple","orange","AAA","ABC","Banana"]
map_object = map(starts_with_A,fruit)
print(list(map_object))

def fun_filter(variables):
    letters = ['a','e','i','o','u']
    if variables in letters:
        return True
    else:
        return False
sequence = ['g','e','e','j','u']
filtered = filter(fun_filter,sequence)
print("the filtered letters are: ")
for s in filtered:
    print(s)