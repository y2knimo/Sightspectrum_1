import re

string = "hii iam gopi"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)
