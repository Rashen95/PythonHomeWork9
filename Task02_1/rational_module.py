import loger as log
import rational_checker as rc


def round_(number1, number2):  # Определение количества знаков после точки
    if '.' in number1:
        round1 = len(number1[number1.index('.') + 1:])
    else:
        round1 = 0
    if '.' in number2:
        round2 = len(number2[number2.index('.') + 1:])
    else:
        round2 = 0
    if round1 > round2:
        round_max = round1
    else:
        round_max = round2
    return round_max


def rational_actions():
    while True:
        print('1. Сложение\n'
              '2. Вычитание\n'
              '3. Умножение\n'
              '4. Деление')
        sel = input('Какую операцию вы хотите произвести с числами: ')
        if sel.isdigit() and sel.strip() == '1' or sel.strip() == '2' or sel.strip() == '3' or sel.strip() == '4':
            if sel.strip() == '1':
                log.loger('Пользователь выбрал операцию сложения')
                while True:
                    number1 = input('Введите первое слагаемое: ')
                    number1 = number1.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number1} как первое слагаемое')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является рациональным числом')
                        log.loger(f'{number1} не является рациональным числом')
                while True:
                    number2 = input('Введите второе слагаемое: ')
                    number2 = number2.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number2} как второе слагаемое')
                    if rc.checker(number2):
                        break
                    else:
                        print(f'{number2} не является рациональным числом')
                        log.loger(f'{number2} не является рациональным числом')
                print(f'Ответ: '
                      f'{round(float(number1) + float(number2), round_(number1, number2))}')
                log.loger(f'Ответ: '
                          f'{round(float(number1) + float(number2), round_(number1, number2))}')
                break
            if sel.strip() == '2':
                log.loger('Пользователь выбрал операцию вычитания')
                while True:
                    number1 = input('Введите уменьшаемое: ')
                    number1 = number1.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number1} как уменьшаемое')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является рациональным числом')
                        log.loger(f'{number1} не является рациональным числом')
                while True:
                    number2 = input('Введите вычитаемое: ')
                    number2 = number2.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number2} как вычитаемое')
                    if rc.checker(number2):
                        break
                    else:
                        print(f'{number2} не является рациональным числом')
                        log.loger(f'{number2} не является рациональным числом')
                print(f'Ответ: '
                      f'{round(float(number1) - float(number2), round_(number1, number2))}')
                log.loger(f'Ответ: '
                          f'{round(float(number1) - float(number2), round_(number1, number2))}')
                break
            if sel.strip() == '3':
                log.loger('Пользователь выбрал операцию умножения')
                while True:
                    number1 = input('Введите первый множитель: ')
                    number1 = number1.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number1} как первый множитель')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является рациональным числом')
                        log.loger(f'{number1} не является рациональным числом')
                while True:
                    number2 = input('Введите второй множитель: ')
                    number2 = number2.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number2} как второй множитель')
                    if rc.checker(number2):
                        break
                    else:
                        print(f'{number2} не является рациональным числом')
                        log.loger(f'{number2} не является рациональным числом')
                print(f'Ответ: '
                      f'{round(float(number1) * float(number2), round_(number1, number2))}')
                log.loger(f'Ответ: '
                          f'{round(float(number1) * float(number2), round_(number1, number2))}')
                break
            if sel.strip() == '4':
                log.loger('Пользователь выбрал операцию деления')
                while True:
                    number1 = input('Введите делимое: ')
                    number1 = number1.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number1} как делимое')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является рациональным числом')
                        log.loger(f'{number1} не является рациональным числом')
                while True:
                    number2 = input('Введите делитель: ')
                    number2 = number2.replace(',', '.').replace(' ', '')
                    log.loger(f'Пользователь ввел {number2} как делитель')
                    if rc.checker(number2):
                        break
                    else:
                        print(f'{number2} не является рациональным числом')
                        log.loger(f'{number2} не является рациональным числом')
                print(f'Ответ: '
                      f'{float(number1) / float(number2)}')
                log.loger(f'Ответ: '
                          f'{float(number1) / float(number2)}')
                break
        else:
            print('!!!ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ!!!')
            log.loger('Пользователь ввел неверное значение при выборе действия с рациональными числами')
