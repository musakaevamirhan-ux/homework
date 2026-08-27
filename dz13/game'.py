import time
from datetime import datetime
from random import randint
timE = 90
print("Приветствую вас в игре, суть которой заключается в том, чтобы за необходимое время сложить два числа, за каждый пройденный раунд вам начисляется 50 очков. Стартовое время 90 секунд, с каждым раундом будет отниматься по 3 секунды. Удачи!!!")
score = 0
with open("highscore.txt", "r", encoding="utf-8") as file:
    highscore = int(file.read())
v = input("Вы готовы начать игру(Введите 'да', кода будете готовы): ")
while v != "нет" and v != "да":
    print("Вы ввели некорректные данные")
    v = input("Вы готовы начать игру(Введите 'да', кода будете готовы): ")
if v == "да":
    while True:
        a = randint(1,1000)
        b = randint(1,1000)
        print(f"У вас будет {timE} сек. на ответ")
        start = time.time()
        answer = int(input(f"Сколько будет {a} + {b}: "))
        end = time.time()
        if answer == a + b and end - start <= timE:
            print("Правильно!!!")
            score += 50
            timE -= 3
        else:
            print("Неправильный ответ или не успели по времени")
            print(f"Вы заработали {score} очков")
            if score > highscore:
                print(f"Поздравляем, ваш новый рекорд - {score}")
                with open("highscore.txt", "w", encoding="utf-8") as file:
                    file.write(str(score))
            with open("history.txt", "a", encoding="utf-8") as file:
                file.write(f"{datetime.now().replace(microsecond=0)} - {str(score)}\n")
            choise = input("Вы хотите сыграть еще раз(да/нет): ")
            while choise != "нет" and choise != "да":
                print("Вы ввели некорректные данные")
                choise = input("Вы хотите сыграть еще раз(да/нет): ")
            if choise == "нет":
                break
            elif choise == "да":
                timE = 90
                score = 0
