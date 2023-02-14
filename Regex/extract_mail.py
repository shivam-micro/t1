import re
s = """Hello you got mail from hamgshubh1930@gmail.com
        to riyaaman@yahoo.com @7pm meeting invite """

lst = re.findall('\S+@\S+', s)

print(lst)