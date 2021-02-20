print('\n{:^65}'.format('«Калькулятор расписания уроков»'))

# Функция длительности урока
def f_lg():
    global lg
    print('\nДлина урока - 45 минут.')
    while True:
        lg_inp = input('Изменить? [да/нет]\n')
        lg_inp = lg_inp.lower()
        if lg_inp == 'да':
            lg = input('Длина урока: ')
            while True:
                if not lg.isnumeric():
                    lg = input('Введите цифру. ')
                else:
                    break
            break
        elif lg_inp == 'нет':
            lg = 45
            break
        elif lg_inp != 'да' or 'нет':
            f_lg()
            break
    lg = int(lg)

# Функция длительности большой перемены
def f_br():
    global br
    print('\nБольшая перемена - 15 минут.')
    while True:
        br_inp = input('Изменить? [да/нет]\n')
        br_inp = br_inp.lower()
        if br_inp == 'да':
            br = input('Длина большой перемены: ')
            while True:
                if not br.isnumeric():
                    br = input('Введите цифру. ')
                else:
                    break
            break
        elif br_inp == 'нет':
            br = 15
            break
        elif br_inp != 'да' or 'нет':
            f_br()
            break
    br = int(br)

# Основная функция
def calc():
    f_lg()
    f_br()

    # Получение часов на ввод и проверка на 24-часовой формат
    ch = input('Введите час начала уроков: ')
    while True:
        if not ch.isnumeric():
            ch = input('Введите цифру. ')
        elif int(ch) > 24 or int(ch) < 0:
            ch = input('Неверно задан час. Введите снова: ')
        else:
            break
    ch = int(ch)

    # Получение минут на ввод и проверка на 24-часовой формат
    mn = input('Введите минуты начала уроков: ')
    while True:
        if not mn.isnumeric():
            mn = input('Введите цифру. ')
        elif int(mn) >= 60 or int(mn) < 0:
            mn = input('Неверно заданы минуты. Введите снова: ')
        else:
            break
    mn = int(mn)

    # Получение кол-ва уроков на ввод
    kl = (input('Введите количество уроков: '))
    while True:
        if not kl.isnumeric():
            kl = input('Введите цифру. ')
        elif kl == '0':
            kl = input('Введите число больше нуля: ')
        else:
            break
    kl = int(kl)

    # Вычисление общей длительности перемен
    pr = (kl * 5) - 5
    if kl > 3:
        pr += br - 5

    # Вычисление общей длительности часов
    ch = ch + (((kl * lg) + pr) // 60)
    while True:
        if ch > 24:
            ch -= 24
        else:
            break

    # Вычисление общей длительности минут
    mn = mn + (((kl * 45) + pr) % 60)
    while True:
        if mn >= 60:
            mn -= 60
            ch += 1
        else:
            break
    if mn < 10:
        mn = '0' + str(mn)

    # Вывод
    print('\nУроки закончатся в', str(ch) + ':' + str(mn) + '.')

calc()
# Цикл с условием перезапуска
while True:
    print('\nВыйти - любая клавиша.\nНачать заново? [да] ')
    flag = input()
    flag = flag.lower()
    if flag == 'да':
        calc()
    else:
        break
