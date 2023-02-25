import re

a = open('row.txt', encoding='utf-8')
b = str(a.read())
rez = re.findall('[A-Z][a-z]*', b)
print(rez)