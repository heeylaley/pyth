dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
text = []

with open(r"C:\Users\Катя\Desktop\text_4.txt", encoding='utf-8') as new_file_1:
    for line in new_file_1:
        line_list = line.split()
        insert = dictionary.get(line_list[0])
        line_list.insert(0, insert)
        line_list.remove(line_list[1])
        text.append(' '.join(line_list))
        text.append('\n')

with open('new_text_4.txt', 'w+', encoding='utf-8') as new_file_2:
    new_file_2.writelines(text)
    new_file_2.seek(0)
    print(new_file_2.read())
