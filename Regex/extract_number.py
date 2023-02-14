import re


s = 'My date of birth is 25 june 2022 and my favourite numbers are 2 and 5'

lst = re.findall('[0-9]+', s)
print(lst)