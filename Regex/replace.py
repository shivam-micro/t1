import re

string = "aregularuser@gmail.com"
print(re.sub("[a-z]*@", "abc@", string))