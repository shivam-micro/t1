person = {3:"bbb", 2:"ccc", 4:"ddd", 1:"aaa"}

print(dict(sorted(person.items(), key = lambda item : item[1])))