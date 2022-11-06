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


def complex_actions():
    while True:
        print('1. Сложение\n'
              '2. Вычитание')
        sel = input('Какую операцию вы хотите произвести с комплексными числами: ')
        if sel.isdigit() and sel.strip() == '1' or sel.strip() == '2':
            if sel.strip() == '1':
                log.loger('Пользователь выбрал операцию сложения')
                while True:
                    print('Вводим первое комплексное число a + bi')
                    number1 = input('Введите коэфициент a, он должен являться вещественным числом: ')
                    number1 = number1.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number1} как коэфициент a для первого комплексного числа')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является вещественным числом')
                        log.loger(f'{number1} не является вещественным числом')
                while True:
                    number2 = input('Введите коэфициент b, он должен являться вещественным числом: ')
                    number2 = number2.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number2} как коэфициент b для первого комплексного числа')
                    if rc.checker(number2):
                        if number2 == '0':
                            print('Коэфициент b не может быть равен 0')
                        else:
                            break
                    else:
                        print(f'{number2} не является вещественным числом')
                        log.loger(f'{number2} не является вещественным числом')
                if float(number1) == 0:
                    print(f'Первое комплексное число - {number2}i')
                    log.loger(f'Первое комплексное число - {number2}i')
                else:
                    if float(number2) < 0:
                        print(f'Первое комплексное число - {number1}{number2}i')
                        log.loger(f'Первое комплексное число - {number1}{number2}i')
                    else:
                        print(f'Первое комплексное число - {number1}+{number2}i')
                        log.loger(f'Первое комплексное число - {number1}+{number2}i')
                while True:
                    print('Вводим второе комплексное число a + bi')
                    number3 = input('Введите коэфициент a, он должен являться вещественным числом: ')
                    number3 = number3.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number3} как коэфициент a для второго комплексного числа')
                    if rc.checker(number3):
                        break
                    else:
                        print(f'{number3} не является вещественным числом')
                        log.loger(f'{number3} не является вещественным числом')
                while True:
                    number4 = input('Введите коэфициент b, он должен являться вещественным числом: ')
                    number4 = number4.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number4} как коэфициент b для второго комплексного числа')
                    if rc.checker(number4):
                        if number4 == '0':
                            print('Коэфициент b не может быть равен 0')
                        else:
                            break
                    else:
                        print(f'{number4} не является вещественным числом')
                        log.loger(f'{number4} не является вещественным числом')
                if float(number3) == 0:
                    print(f'Второе комплексное число - {number4}i')
                    log.loger(f'Второе комплексное число - {number4}i')
                else:
                    if float(number4) < 0:
                        print(f'Второе комплексное число - {number3}{number4}i')
                        log.loger(f'Второе комплексное число - {number3}{number4}i')
                    else:
                        print(f'Второе комплексное число - {number3}+{number4}i')
                        log.loger(f'Второе комплексное число - {number3}+{number4}i')
                number5 = round(float(number1) + float(number3), round_(number1, number3))
                number6 = round(float(number2) + float(number4), round_(number2, number4))
                if number5 % 1 == 0:
                    number5 = int(number5)
                if number6 % 1 == 0:
                    number6 = int(number6)
                if number5 == 0:
                    if number6 == 0:
                        print(f'Ответ: 0')
                        log.loger(f'Ответ: 0')
                    elif number6 == 1:
                        print(f'Ответ: i')
                        log.loger(f'Ответ: i')
                    elif number6 == -1:
                        print(f'Ответ: -i')
                        log.loger(f'Ответ: -i')
                    else:
                        print(f'Ответ: {number6}i')
                        log.loger(f'Ответ: {number6}i')
                else:
                    if number6 == 0:
                        print(f'Ответ: {number5}')
                        log.loger(f'Ответ: {number5}')
                    elif number6 == 1:
                        print(f'Ответ: {number5}+i')
                        log.loger(f'Ответ: {number5}+i')
                    elif number6 == -1:
                        print(f'Ответ: {number5}-i')
                        log.loger(f'Ответ: {number5}-i')
                    elif number6 < -1:
                        print(f'Ответ: {number5}{number6}i')
                        log.loger(f'Ответ: {number5}{number6}i')
                    else:
                        print(f'Ответ: {number5}+{number6}i')
                        log.loger(f'Ответ: {number5}+{number6}i')
                break
            if sel.strip() == '2':
                log.loger('Пользователь выбрал операцию вычитания')
                while True:
                    print('Вводим первое комплексное число a + bi')
                    number1 = input('Введите коэфициент a, он должен являться вещественным числом: ')
                    number1 = number1.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number1} как коэфициент a для первого комплексного числа')
                    if rc.checker(number1):
                        break
                    else:
                        print(f'{number1} не является вещественным числом')
                        log.loger(f'{number1} не является вещественным числом')
                while True:
                    number2 = input('Введите коэфициент b, он должен являться вещественным числом: ')
                    number2 = number2.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number2} как коэфициент b для первого комплексного числа')
                    if rc.checker(number2):
                        if number2 == '0':
                            print('Коэфициент b не может быть равен 0')
                        else:
                            break
                    else:
                        print(f'{number2} не является вещественным числом')
                        log.loger(f'{number2} не является вещественным числом')
                if float(number1) == 0:
                    print(f'Первое комплексное число - {number2}i')
                    log.loger(f'Первое комплексное число - {number2}i')
                else:
                    if float(number2) < 0:
                        print(f'Первое комплексное число - {number1}{number2}i')
                        log.loger(f'Первое комплексное число - {number1}{number2}i')
                    else:
                        print(f'Первое комплексное число - {number1}+{number2}i')
                        log.loger(f'Первое комплексное число - {number1}+{number2}i')
                while True:
                    print('Вводим второе комплексное число a + bi')
                    number3 = input('Введите коэфициент a, он должен являться вещественным числом: ')
                    number3 = number3.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number3} как коэфициент a для второго комплексного числа')
                    if rc.checker(number3):
                        break
                    else:
                        print(f'{number3} не является вещественным числом')
                        log.loger(f'{number3} не является вещественным числом')
                while True:
                    number4 = input('Введите коэфициент b, он должен являться вещественным числом: ')
                    number4 = number4.replace(' ', '').replace(',', '.')
                    log.loger(f'Пользователь ввел {number4} как коэфициент b для второго комплексного числа')
                    if rc.checker(number4):
                        if number4 == '0':
                            print('Коэфициент b не может быть равен 0')
                        else:
                            break
                    else:
                        print(f'{number4} не является вещественным числом')
                        log.loger(f'{number4} не является вещественным числом')
                if float(number3) == 0:
                    print(f'Второе комплексное число - {number4}i')
                    log.loger(f'Второе комплексное число - {number4}i')
                else:
                    if float(number4) < 0:
                        print(f'Второе комплексное число - {number3}{number4}i')
                        log.loger(f'Второе комплексное число - {number3}{number4}i')
                    else:
                        print(f'Второе комплексное число - {number3}+{number4}i')
                        log.loger(f'Второе комплексное число - {number3}+{number4}i')
                number5 = round(float(number1) - float(number3), round_(number1, number3))
                number6 = round(float(number2) - float(number4), round_(number2, number4))
                if number5 % 1 == 0:
                    number5 = int(number5)
                if number6 % 1 == 0:
                    number6 = int(number6)
                if number5 == 0:
                    if number6 == 0:
                        print(f'Ответ: 0')
                        log.loger(f'Ответ: 0')
                    elif number6 == 1:
                        print(f'Ответ: i')
                        log.loger(f'Ответ: i')
                    elif number6 == -1:
                        print(f'Ответ: -i')
                        log.loger(f'Ответ: -i')
                    else:
                        print(f'Ответ: {number6}i')
                        log.loger(f'Ответ: {number6}i')
                else:
                    if number6 == 0:
                        print(f'Ответ: {number5}')
                        log.loger(f'Ответ: {number5}')
                    elif number6 == 1:
                        print(f'Ответ: {number5}+i')
                        log.loger(f'Ответ: {number5}+i')
                    elif number6 == -1:
                        print(f'Ответ: {number5}-i')
                        log.loger(f'Ответ: {number5}-i')
                    elif number6 < -1:
                        print(f'Ответ: {number5}{number6}i')
                        log.loger(f'Ответ: {number5}{number6}i')
                    else:
                        print(f'Ответ: {number5}+{number6}i')
                        log.loger(f'Ответ: {number5}+{number6}i')
        else:
            print('!!!ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ!!!')
            log.loger('Пользователь ввел неверное значение при выборе действия с рациональными числами')
