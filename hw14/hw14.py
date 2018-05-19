

import os

start_path = '.'
for root, dirs, files in os.walk(start_path):
    print('Где мы сейчас:', root)
    print('Папки на этом уровне:', dirs)
    print('Файлы на этом уровне:', files)

    names = {}
    for file in files:
    	names[os.path.splitext(file)[0]] = 0

    print('Количество разных названий файлов без учёта расширений:',len(names))
    print()
