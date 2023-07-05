import re

s = 'Hii I am Gopi'

match = re.search(r'Gopi', s)

print('Start Index:', match.start())
print('End Index:', match.end())
