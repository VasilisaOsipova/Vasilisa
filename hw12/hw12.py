import re
import string
f = open('file.txt')
ans = ''
for line in f:
    ans = re.sub('Динозавр', 'Кот', line)
    ans = re.sub('динозавр', 'кот', ans)
    print(ans)
f.close()