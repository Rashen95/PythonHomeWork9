def add_contact():
    while True:
        last_name = input('Введите фамилию добавляемого человека: ')
        if last_name and last_name.strip():
            break
        else:
            print('Вы ничего не ввели')
    while True:
        first_name = input('Введите имя добавляемого человека: ')
        if first_name and first_name.strip():
            break
        else:
            print('Вы ничего не ввели')
    while True:
        phone_number = input('Введите номер телефона в формате +7ХХХХХХХХХХ или ХХХХХХХ: ')
        if len(phone_number) == 12 and phone_number[0:2] == '+7' and phone_number[2:].isdigit():
            break
        elif len(phone_number) == 7 and phone_number.isdigit():
            break
        else:
            print('Вы ввели телефон в неверном формате!')
    while True:
        description = input('Описание контакта: ')
        if description and description.strip():
            break
        else:
            print('Вы ничего не ввели')
    with open('directory.txt', 'a', encoding="utf-8") as description_file:
        description_file.write(f"\n{last_name}")
        description_file.write(f"\n{first_name}")
        description_file.write(f"\n{phone_number}")
        description_file.write(f"\n{description}\n")
    print(f'{last_name} {first_name} добавлен в список контактов')
