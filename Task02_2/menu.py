import read
import add
import import_module
import export_module

while True:
    menu = input(('1 Просмотр записей\n'
                  '2 Добавление записи\n'
                  '3 Экспорт\n'
                  '4 Импорт\n'
                  '5 Выход из программы\n'
                  'Выберите нужный пункт меню: '))
    if menu == '1':
        read.read_contact()
    if menu == '2':
        add.add_contact()
    if menu == '3':
        export_module.export_contact()
    if menu == '4':
        import_module.import_contact()
    if menu == '5':
        print('Завершаю работу приложения')
        break
