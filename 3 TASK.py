import os

BASE = os.getcwd()
files = os.listdir(BASE)
txt = filter(lambda x: x.endswith('.txt'), files)
work_list = []

def reading_file(files, newfile):  
    for file in txt:
        with open(file, encoding = 'utf-8') as f:
            text = f.read()
            count = len(text.split('\n'))
            if text == '':
                count = 0
            work_list.append([file, count, text])
            work_list_sort = sorted(work_list, key=lambda x: x[1])
        with open(newfile, 'w', encoding = 'utf-8') as w:
            for file in work_list_sort:
                w.write(f'{file[0]}\n') 
                w.write(f'{file[1]}\n')
                w.write(f'{file[2]}\n\n')

if __name__ == '__main__':
    reading_file(txt, 'newfile.txt')

# перебор списка через for и запись в файл