def read_contact():
    print('Все контакты телефонной книни: \n')
    with open("directory.txt", "r", encoding='UTF-8') as original_file:
        for line in original_file:
            print(line, end="")
