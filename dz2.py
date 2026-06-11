# 1
# age = int(input())
# if 0<=age<=2:
#     print("ребенок")
# elif 12<=age<=18:
#     print("подросток")
# elif age>=60:
#     print("пенсионер")
# elif 18<=age<=60:
#     print("взрослый")
# 2
# num = int(input())
# if num == 1:
#     print("!")
# elif num == 2:
#     print("@")
# elif num == 3:
#     print("#")
# elif num == 4:
#     print("$")
# elif num == 5:
#     print("%")
# elif num == 6:
#     print("^")
# elif num == 7:
#     print("&")
# elif num == 8:
#     print("*")
# elif num == 9:
#     print("(")
# elif num == 0:
#     print(")")
# 3
# num = input()
# if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
#     print("YES")
# else:
#     print("NO")
# 4
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")
# 5
# num = input()
# if num == num[::-1]:
#     print("YES")
# else:
#     print("NO")
# 6
# cnt = int(input())
# currency = input()
# if currency == "EUR":
#     print(cnt*0.87)
# elif currency == "UAN":
#     print(cnt*44.37)
# elif currency == "AZN":
#     print(cnt*1.70)
# 7
# cost = int(input())
# if 200<=cost<=300:
#     print(cost*0.97)
# elif 300<=cost<=500:
#     print(cost*0.95)
# if cost>=500:
#     print(cost*0.93)
# 8
# c = int(input())
# p = int(input())
# if p/4 >= c:
#     print("YES")
# else:
#     print("NO")
# 9
# cnt = 0
# question1 = input("Какого цвета трава?"
#                   "1. Красная"
#                   "2. Синяя"
#                   "3. Зеленая")
# question2 = input("Сколько будет 2+2?"
#                   "1. 3"
#                   "2. 4"
#                   "3. 5")
# question3 = input("Что такое Евразия?"
#                   "1. Город"
#                   "2. Страна"
#                   "3. Материк")
# if question1 == "Зеленая":
#     cnt += 2
# if question2 == "4":
#     cnt += 2
# if question1 == "Материк":
#     cnt += 2
# print(cnt)
# 10
# day = int(input("Введите день: "))
# month = int(input("Введите месяц: "))
# year = int(input("Введите год: "))
# visokos = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# if month == 2:
#     if visokos:
#         days_in_month = 29
#     else:
#         days_in_month = 28
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days_in_month = 30
# else:
#     days_in_month = 31
# if day < days_in_month:
#     day += 1
# else:
#     day = 1
#     if month < 12:
#         month += 1
#     else:
#         month = 1
#         year += 1
# print(f"Следующая дата: {day}.{month}.{year}")






