import re

def snake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()
a = open('row.txt', encoding='utf-8')
b = str(a.read())
rez = snake(b)
print(rez)