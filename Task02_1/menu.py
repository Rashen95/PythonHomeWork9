import loger as log
import rational_module as rm
import complex_module as cm


while True:
    print('1. Работа с рациональными числами\n'
          '2. Работа с комплексными числами\n'
          '3. Выход из приложения')
    sel = input('Выберите необходимый пункт меню путем ввода числа: ')
    if sel.isdigit() and sel.strip() == '1' or sel.strip() == '2' or sel.strip() == '3':
        if sel.strip() == '1':
            log.loger('Пользователь выбрал режим работы с рациональными числами')
            rm.rational_actions()
        elif sel.strip() == '2':
            log.loger('Пользователь выбрал режим работы с комплексными числами')
            cm.complex_actions()
        else:
            print('Работа приложения завершена')
            log.loger('Пользователь завершил работу приложения')
            break
    else:
        print('!!!ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ!!!')
        log.loger('Пользователь ввел неверное значение при выборе режима работы приложения')
