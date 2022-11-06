import telebot
import loger as log
import rational_checker as rc

bot = telebot.TeleBot('5517601396:AAGU-xfZxNb_c1Kc5p_0KT-IL7STeJQxFf0')


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


@bot.message_handler(commands=['start'])
def start(message):
    log.loger(f'Пользователь {message.from_user.first_name} начал пользоваться калькулятором')
    bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
    bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                      '2. Работа с комплексными числами\n'
                                      '3. Выход из приложения')
    bot.register_next_step_handler(callback=change, message=message)


def change(message):
    if message.text.strip() == '1':
        bot.send_message(message.chat.id, 'Вы выбрали работу с рациональными числами')
        log.loger(f'Пользователь {message.from_user.first_name} выбрал режим работы с рациональными числами')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание\n'
                                          '3. Умножение\n'
                                          '4. Деление')
        bot.register_next_step_handler(callback=rational_actions, message=message)
    elif message.text.strip() == '2':
        bot.send_message(message.chat.id, 'Вы выбрали работу с комплексными числами')
        log.loger(f'Пользователь {message.from_user.first_name} выбрал режим работы с комплексными числами')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание')
        bot.register_next_step_handler(callback=complex_actions, message=message)
    elif message.text.strip() == '3':
        log.loger(f'Пользователь {message.from_user.first_name} завершил работу приложения')
        bot.send_message(message.chat.id, 'Работа приложения завершена')
    else:
        log.loger(f'Пользователь {message.from_user.first_name} ввел {message.text} при попытке режима работы')
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)


def rational_actions(message):
    if message.text.strip() == '1':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию сложения')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=summator, message=message)
    elif message.text.strip() == '2':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию вычитания')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я вычту из первого второе')
        bot.register_next_step_handler(callback=subtraction, message=message)
    elif message.text.strip() == '3':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию умножения')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их перемножу')
        bot.register_next_step_handler(callback=multiplication, message=message)
    elif message.text.strip() == '4':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию деления')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я поделю первое на второе')
        bot.register_next_step_handler(callback=division, message=message)
    else:
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание\n'
                                          '3. Умножение\n'
                                          '4. Деление')
        bot.register_next_step_handler(callback=rational_actions, message=message)


def summator(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        bot.send_message(message.chat.id,
                         f'Ответ: {round(float(lst[0]) + float(lst[1]), round_(lst[0], lst[1]))}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ: {round(float(lst[0]) + float(lst[1]), round_(lst[0], lst[1]))}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=summator, message=message)


def subtraction(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        bot.send_message(message.chat.id,
                         f'Ответ: {round(float(lst[0]) - float(lst[1]), round_(lst[0], lst[1]))}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ: {round(float(lst[0]) - float(lst[1]), round_(lst[0], lst[1]))}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=subtraction, message=message)


def multiplication(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        bot.send_message(message.chat.id,
                         f'Ответ: {round(float(lst[0]) * float(lst[1]), round_(lst[0], lst[1]))}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ: {round(float(lst[0]) * float(lst[1]), round_(lst[0], lst[1]))}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=multiplication, message=message)


def division(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        bot.send_message(message.chat.id,
                         f'Ответ: {(float(lst[0]) / float(lst[1]))}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ: {(float(lst[0]) / float(lst[1]))}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=division, message=message)


def complex_actions(message):
    if message.text.strip() == '1':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию сложения')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю сумму получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_summator, message=message)
    elif message.text.strip() == '2':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию вычитания')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю разность получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_subtraction, message=message)
    else:
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание')
        bot.register_next_step_handler(callback=complex_actions, message=message)


def comp_summator(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        number1 = round(float(lst[0]) + float(lst[2]), round_(lst[0], lst[2]))
        number2 = round(float(lst[1]) + float(lst[3]), round_(lst[1], lst[3]))
        if number1 % 1 == 0:
            number1 = int(number1)
        if number2 % 1 == 0:
            number2 = int(number2)
        if number1 == 0:
            if number2 == 0:
                log.loger(f'Ответ: 0')
                bot.send_message(message.chat.id,
                                 f'Ответ: 0')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: i')
                log.loger(f'Ответ: i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: -i')
                log.loger(f'Ответ: -i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number2}i')
                log.loger(f'Ответ: {number2}i')
        else:
            if number2 == 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}')
                log.loger(f'Ответ: {number1}')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+i')
                log.loger(f'Ответ: {number1}+i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}-i')
                log.loger(f'Ответ: {number1}-i')
            elif number2 < -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}{number2}i')
                log.loger(f'Ответ: {number1}{number2}i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+{number2}i')
                log.loger(f'Ответ: {number1}+{number2}i')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю сумму получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_summator, message=message)


def comp_subtraction(message):
    lst = message.text.replace(',', '.').split(' ')
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        number1 = round(float(lst[0]) - float(lst[2]), round_(lst[0], lst[2]))
        number2 = round(float(lst[1]) - float(lst[3]), round_(lst[1], lst[3]))
        if number1 % 1 == 0:
            number1 = int(number1)
        if number2 % 1 == 0:
            number2 = int(number2)
        if number1 == 0:
            if number2 == 0:
                log.loger(f'Ответ: 0')
                bot.send_message(message.chat.id,
                                 f'Ответ: 0')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: i')
                log.loger(f'Ответ: i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: -i')
                log.loger(f'Ответ: -i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number2}i')
                log.loger(f'Ответ: {number2}i')
        else:
            if number2 == 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}')
                log.loger(f'Ответ: {number1}')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+i')
                log.loger(f'Ответ: {number1}+i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}-i')
                log.loger(f'Ответ: {number1}-i')
            elif number2 < -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}{number2}i')
                log.loger(f'Ответ: {number1}{number2}i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+{number2}i')
                log.loger(f'Ответ: {number1}+{number2}i')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю сумму получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_subtraction, message=message)


bot.infinity_polling()
