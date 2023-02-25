import re

a = open('row.txt', encoding='utf-8')
b = str(a.read())
x = re.search("ab{2,3}$", b)
if x:
    print("it's a match")
else:
    print("no match found")