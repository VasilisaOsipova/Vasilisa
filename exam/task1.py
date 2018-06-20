#! python3 -v
# -*- coding: utf-8 -*-
import os
import re

current_directory = os.path.dirname(__file__)
files = [file for file in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, file))]
for filename in files:
    if filename.split('.')[1] in ('py','txt'):
        continue
    else:
        with open(filename, mode='r', encoding='utf-8') as file:
            lines = [line.rstrip('\n') for line in file]
            regex_tag = re.compile('<.*?>')
            for i in range(len(lines)):
                lines[i] = re.sub(regex_tag, '', lines[i])
                lines[i] = lines[i].replace('`','')
            result = "\n".join([line.rstrip() for line in lines if line.strip()])

            new_filename = os.path.splitext(filename)[0] + ".txt"
            with open(new_filename, mode='w',encoding='cp1251') as file_output:
                file_output.write(result)