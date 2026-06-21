from random import randint
igra = input("Вы хотите сыграть в камень-ножницы=бумагу или угадайку числа(1 - угадайка, 2 - камень-ножницы-бумага):")
if igra == "2":
    result_my = 0
    result_comp = 0
    my = 0
    comp = 0
    h = True
    vibor = input("Вы хотите играть в одиночку?\n")
    print("-----------------------------")
    if vibor == "да":
        while h:
            xod = input("Введите ваш ход с маленькой буквы:\n")
            i = 0
            bot = 0
            k = randint(1,3)
            t = ""
            if k == 1:
                t = "ножницы"
            elif k == 2:
                t = "камень"
            else:
                t = "бумага"
            while xod != "бумага" and xod != "камень" and xod != "ножницы":
                print("Вы ввели некорректные данные, попробуйте снова")
                xod = input("Введите ваш ход с маленькой буквы:\n")
            if xod != t:
                if xod == "бумага" and t == "камень":
                    i += 1
                elif xod == "ножницы" and t == "камень":
                    bot += 1
                elif xod == "камень" and t == "ножницы":
                    i += 1
                elif xod == "бумага" and t == "ножницы":
                    bot += 1
                elif xod == "камень" and t == "бумага":
                    bot += 1
                else: i += 1
                print(f"Мой ход:{t}")
                print(f"Ваш ход:{xod}")
                print(i==1 and "Вы победили\U0001F389\U0001F389\U0001F389" or "Вы проиграли\U0001F641\U0001F641\U0001F641")
                if i == 1:
                    my += 1
                else:
                    comp += 1
            else:
                print(f"Мой ход:{t}")
                print(f"Ваш ход:{xod}")
                print("Ничья")
            print(f"У меня побед:{comp}\nУ вас побед:{my}")
            print("-----------------------------")
            if my == 3:
                print(f"Вы победили со счетом {my}:{comp}")
                result_my += 1
                print(f"Итоговый счет: PC {result_comp}: PlAYER {result_my}")
                a = input("Хотите сыграть еще?\n")
                if a == "да" or a == "Да":
                    h = True
                else:
                    h = False
                result_my += 1
            if comp == 3:
                print(f"Вы проиграли со счетом {comp}:{my}")
                result_comp += 1
                print(f"Итоговый счет: PC {result_comp}: PlAYER {result_my}")
                print("-----------------------------")
                a = input("Хотите сыграть еще?\n")
                if a == "да" or a == "Да":
                    h = True
                else:
                    h = False
                print("-----------------------------")
    else:
        while h:
            i = 0
            bot = 0
            t = input("Первый игрок, введите ваш ход с маленькой буквы:\n")
            while t != "бумага" and t != "камень" and t != "ножницы":
                print("Вы ввели некорректные данные, попробуйте снова")
                t = input("Первый игрок, введите ваш ход с маленькой буквы:\n")
            xod = input("Второй игрок, введите ваш ход с маленькой буквы:\n")
            while xod != "бумага" and xod != "камень" and xod != "ножницы":
                print("Вы ввели некорректные данные, попробуйте снова")
                xod = input("Второй игрок, введите ваш ход с маленькой буквы:\n")
            if xod != t:
                if xod == "бумага" and t == "камень":
                    i += 1
                elif xod == "ножницы" and t == "камень":
                    bot += 1
                elif xod == "камень" and t == "ножницы":
                    i += 1
                elif xod == "бумага" and t == "ножницы":
                    bot += 1
                elif xod == "камень" and t == "бумага":
                    bot += 1
                else: i += 1
                print(f"Ход первого игрока:{t}")
                print(f"Ход второго игрока:{xod}")
                print(i==1 and "Победил второй игрок\U0001F389\U0001F389\U0001F389" or "Победил первый игрок\U0001F389\U0001F389\U0001F389")
                if i == 1:
                    my += 1
                else:
                    comp += 1
            else:
                print(f"Ход первого игрока:{t}")
                print(f"Ход второго игрока:{xod}")
                print("Ничья")
            print(f"Счет первого игрока:{comp}\nСчет второго игрока:{my}")
            print("-----------------------------")
            if my == 3:
                print(f"Второй игрок победил со счетом {my}:{comp}")
                result_my += 1
                print(f"Итоговый счет: FIRST PLAYER {result_my}: SECOND PlAYER {result_comp}")
                print("-----------------------------")
                a = input("Хотите сыграть еще?\n")
                if a == "да" or a == "Да":
                    h = True
                else:
                    h = False
            if comp == 3:
                print(f"Первый игрок победил со счетом {comp}:{my}")
                result_comp += 1
                print(f"Итоговый счет: FIRST PLAYER {result_comp}: SECOND PlAYER {result_my}")
                print("-----------------------------")
                a = input("Хотите сыграть еще?\n")
                if a == "да" or a == "Да":
                    h = True
                else:
                    h = False
else:
    win = 0
    lose = 0
    h = True
    while h:
        k = randint(1, 99)
        for _ in range(5):
            a = int(input("Введите число от 1 до 99:\n"))
            if a == k:
                break
            elif a > k:
                print("Меньше")
            else: print("Больше")
        if a == k:
            win += 1
        else:
            lose += 1
        print(f"Загаданное число - {k}")
        print(f"Статистика: WINS {win}: :LOSES {lose}")
        select = input("Вы хотите сыграть снова?\n")
        if select == "да":
            h = True        
        else: h = False
