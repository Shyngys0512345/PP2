import re

def insert_s(string):
    return re.sub('(?!^)(?=[A-Z])', ' ', string)
a = open('row.txt', encoding='utf-8')
b = str(a.read())
rez = insert_s(b)
print(rez)