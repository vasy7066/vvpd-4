""""программа про топологии сетей"""

import sys


def int_input_V_R():
    "функция ввода чисел V и R "
    array = (input("введите пару V и R через пробел ")).split()
    if len(array) >= 2:
        while True:
            try:
                if int(array[0]) > 4 and int(array[1]) > 3 and len(array) == 2:
                    array = [int(array[0]), int(array[1])]
                    return array[0],array[1]
                else:
                    print("Неверный ввод")
                    array = (input("введите пару V и R через пробел ")).split()
            except TypeError:
                print("Неверный ввод")
                array = (input("введите пару V и R через пробел ")).split()

    else:
        print("Неверный ввод")
        array = (input("введите пару V и R через пробел ")).split()


def int_input():
    "функция ввода кортежа связей"
    array = (input("введите пару чисел через пробел ")).split()
    if array[0] == "stop":
        return "stop"
    while True:
        try:
            if int(array[0]) > 0 and int(array[1]) > 0 and len(array) == 2 and array[0] != array[1]:
                tuple = (int(array[0]), int(array[1]))
                return tuple
            else:
                print("Неверный ввод")
                array = (input("введите пару чисел через пробел ")).split()
        except ValueError:
            print("Неверный ввод")
            array = (input("введите пару чисел через пробел ")).split()


def data_about_connections(R):
    "заполнение массива кортежами связей"
    list = []
    for i in range(R):
        tuple1 = int_input()
        if isinstance(tuple1,tuple):
            list.append(tuple1)
        else:
            break
    return list


def is_full_connected (v: int, r: int, links: list[tuple[int, int]]):
    "определяем связность сети"
    list_peaks = []
    for i in range(len(links)):
        list_peaks.append(links[i][0])
        list_peaks.append(links[i][1])
    for i in range(len(list_peaks)):
        if list_peaks[i] > v:
            return False
    for i in range(1,v + 1):
        if i not in list_peaks:
            return False
    return True


def connection_type (v: int, r: int, links: list[tuple[int, int]]):
    "определяем тип сети"
    list_peaks = []
    list_counts = []
    for i in range(len(links)):
        list_peaks.append(links[i][0])
        list_peaks.append(links[i][1])
    for i in range(len(list_peaks)):
        count_connect = 0
        for j in range(len(list_peaks)):
            if list_peaks[i] == list_peaks[j]:
                count_connect += 1
        list_counts.append(count_connect)
    if min(list_counts) == 1 and max(list_counts) == 2:
        return 1
    elif max(list_counts) == 2:
        return 2
    return 3


def menu():
    "выводим данные меню"
    print("[0] Выход из программы")
    print("[1] Провести анализ на полносвязность")
    print("[2] Провести комплексный анализ")


def holiness_check(V,R,list):
    "проверяем полносвязность связи"
    if is_full_connected(V, R, list):
        result = True
        print("Связь полносвязная")
    else:
        result = False
        print("Связь не полносвязная")
    return result


def type_check(V,R,list):
    "находим типип связи"
    RESULT = connection_type(V,R,list)
    if RESULT == 1:
        print("тип связи: Шина")
    elif RESULT == 2:
        print("тип связи: Кольцо")
    elif RESULT == 3:
        print("тип связи: Звезда")


def main():
    "основная функция "
    while True:
        menu()
        comand = input("Введите команду ")
        if comand == "0":
            sys.exit()
        if comand in ["0","1","2"]:
            V, R = int_input_V_R()
            list = data_about_connections(R)
            match comand:
                case "1":
                    holiness_check(V,R,list)
                case "2":
                    result = holiness_check(V,R,list)
                    if result == True:
                        type_check(V,R,list)
        else:
            print("Введите коректную команду")


if __name__ == "__main__":
    main()
















