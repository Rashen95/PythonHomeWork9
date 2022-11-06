def export_contact():
    while True:
        export_format = input('В каком формате вы хотите произвести экспорт?\n'
                              '\nВведите 1 если в таком формате:\nФамилия\nИмя\nТелефон\nОписание\n'
                              '\nВведите 2 если в таком формате:\nФамилия, Имя, Телефон, Описание\n'
                              '\nВыбирите формат (1 или 2): ')
        if export_format == '1' or export_format == '2':
            break
        else:
            print('Вы ввели неверное значение')
    while True:
        file_name = input('Введите название для файла в который будет произведен экспорт: ')
        if file_name == 'directory':
            print('Имя файла не может совпадать с экспортируемым')
        elif file_name and file_name.strip():
            break
        else:
            print('Вы ничего не ввели')
    if export_format == '1':
        with open("directory.txt", "r", encoding="utf-8") as original_file:
            list_contact = original_file.readlines()
        with open(f"{file_name}.txt", "w", encoding="utf-8") as export_file:
            for i in list_contact:
                export_file.write(i)
    else:
        with open(f"directory.txt", "r", encoding="utf-8") as original_file:
            list_contact = original_file.readlines()
        for i in range(len(list_contact)):
            if list_contact[i] == '\n':
                continue
            else:
                list_contact[i] = list_contact[i][:-1]
        with open(f"{file_name}.txt", "w", encoding="utf-8") as export_file:
            for i in range(len(list_contact)):
                if i + 1 < len(list_contact):
                    if list_contact[i + 1] == '\n':
                        export_file.write(f'{list_contact[i]}')
                    elif list_contact[i] != '\n':
                        export_file.write(f'{list_contact[i]}, ')
                    else:
                        export_file.write(f'{list_contact[i]}')
                else:
                    export_file.write(f'{list_contact[len(list_contact)-1]}\n')
    print(f'Ваши контакты испортированы в файл {file_name}.txt')
