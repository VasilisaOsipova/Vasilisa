import re
import string
f = open('textt.txt')
f2 = open('data.txt', 'w')
ans = ''
for line in f:
    ans = re.sub('Динозавр', 'Кот', line)
    ans = re.sub('динозавр', 'кот', ans)
    f2.write(ans)
f.close()
f2.close()
