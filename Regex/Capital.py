import re
def uppercase(a):
    return a.group(1) + a.group(2).upper()
s = "my name is mohan and i am an employee"
result = re.sub("(^|\s)(\S)", uppercase, s)
print(result)