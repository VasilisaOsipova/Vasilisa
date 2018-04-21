import os
file_list = os.listdir()
answer = 0
fold_names = ''
for i in range(0, len(file_list)):
    path = './' + file_list[i]
    valid = False
    if os.path.isdir(path):
        for letter in file_list[i]:
            if letter == ' ':
                valid = True
        if valid:
            answer += 1
            fold_names += file_list[i] + ', '
print('Папок, состоящих из более чем одного слова', answer)
help = fold_names.split(',')
del help[-1]
fold_names = ', '.join(help)
print('Эти папки: ', fold_names)
