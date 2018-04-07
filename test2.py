import re

with open('mystem.xml', 'r', encoding='utf-8') as f:
    text=re.findall(r'<se>(.*?)</se>'
data, re.DOTALL)
    сount=sum(1 for line in text)
print(count)
file=open('data.txt','w')
file.write(count)
file.close()
