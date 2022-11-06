def import_contact():
    while True:
        file_name = input('Введите имя файла предварительно размещенного в данной директории для импорта: ')
        if file_name and file_name.strip():
            try:
                with open(f"{file_name}.txt", "r", encoding="utf-8") as import_file:
                    for line in import_file:
                        list_contact = line.split()
                        for i in range(len(list_contact)):
                            if list_contact[i][-1:] == ',':
                                list_contact[i] = list_contact[i][:-1]
                        if len(list_contact) > 1:
                            with open(f"directory.txt", "a", encoding="utf-8") as original_file:
                                for i in range(len(list_contact)):
                                    if i == 0:
                                        original_file.write(f'\n{list_contact[i]}\n')
                                    elif i < len(list_contact):
                                        original_file.write(f'{list_contact[i]}\n')
                        else:
                            with open(f"directory.txt", "a", encoding="utf-8") as original_file:
                                if list_contact:
                                    original_file.write(f'\n{list_contact[0]}')
                                else:
                                    original_file.write('\n')
            except FileNotFoundError:
                print(f'В данной директории отсутствует файл {file_name}.txt')
            else:
                print(f'Файл найден. Импорт из файла {file_name}.txt в файл directory.txt был произведен.')
                break
        else:
            print('Вы ничего не ввели')
