import csv
import random

# 指定.tsv文件路径
filename = './cscd-ime/dev.tsv'
output = './cscd-ime/dev.txt'

# 使用csv.DictReader读取.tsv文件，这里设定分隔符为'\t'
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', fieldnames=['errors', 'query', 'answer'])
    with open(output, 'w', encoding='utf-8') as out:
        for row in reader:
            sublen = random.randint(1, 3)
            mask = random.sample(range(1, len(row['query'])), sublen)
            for i,char in enumerate(row['query'][:-1]):
                if i in mask:
                    continue
                out.write(char + ' ')
            out.write(row['query'][-1] + '\t')
            for char in row['answer'][:-1]:
                out.write(char + ' ')
            out.write(row['answer'][-1] + '\n')
        