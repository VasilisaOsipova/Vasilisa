import re
import string
f = open('file.txt')
fam = False
ans = False
for line in f:
    if not fam:
        fam = re.search('Семейство', line)
    if fam:
        pos = line.find('Семейство') + 9
        line = line[pos:]
        line = line.replace('ё', 'е')
        ans = re.search('[А-я]+', line)
    if ans:
        ans = ans.group()
        break
print(ans)
f.close()