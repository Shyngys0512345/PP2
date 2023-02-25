import re

a = open('row.txt', encoding='utf-8')
b = str(a.read())
x = re.sub(" ", ',', b)
print(x)