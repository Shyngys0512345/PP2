import re

def camel(s):
    return re.sub('_([a-z])', lambda match: match.group(1).upper(), s)
a = open('row.txt', encoding='utf-8')
b = str(a.read())
rez = camel(b)
print(rez)