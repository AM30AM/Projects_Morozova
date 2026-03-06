#Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно вставив после каждой строки строку из символов
#«*».

file_in = open('text18-12.txt', 'r', encoding='utf-16')
file = file_in.read()
file_in.close()

space_count = 0
for i in file:
    if i == '\n':
        space_count += 1
print('Количество пробельных символов', space_count)

lines = file.split('\n')
new_file = []

for line in lines:
    new_file.append(line)
    new_file.append('*' * len(line))

file_out = open('text.txt', 'w', encoding='utf-16')
file_out.write('\n'.join(new_file))
file_out.close()

