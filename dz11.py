# Задача 1
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# print(max(a, b, c, d))

# Задача 2
# a = int(input())
# b = int(input())
# start = max(a, b)
# end = min(a, b)
# for i in range(start, end - 1, -1):
#     print(i)

# Задача 3
# n = int(input())
# num = 5
# for i in range(n):
#     for j in range(n):
#         print(num, end=" ")
#         num = num + 1
#     print()

# Задача 4
# s = input()
# if "A" <= s <= "Z":
#     print("Да")
# else:
#     print("Нет")

# Задача 5
# spisok = []
# for i in range(8):
#     spisok.append(i * 3)
# print(spisok)

# Задача 6
# import random
# rows = int(input())
# cols = int(input())
# a = int(input())
# b = int(input())
# if a > b:
#     a, b = b, a
# matrix = []
# total = 0
# count = 0
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         val = random.randint(a, b)
#         row.append(val)
#         total = total + val
#         count = count + 1
#     matrix.append(row)
#     print(row)
# print(total / count)

# Задача 7
# i_min = matrix[0][0]
# i_max = matrix[0][0]
# for row in matrix:
#     for val in row:
#         if val < i_min:
#             i_min = val
#         if val > i_max:
#             i_max = val
# print("Минимум:", i_min)
# print("Максимум:", i_max)

# Задача 8
# def find_num(lst, x):
#     for item in lst:
#         if item == x:
#             return True
#     return False

# Задача 9
# def get_odd(lst):
#     res = []
#     for x in lst:
#         if x % 2 != 0:
#             res.append(x)
#     return res

# Задача 10
# def get_col(matrix, idx):
#     res = []
#     for row in matrix:
#         res.append(row[idx])
#     return res

# Задача 11
# def get_numbers(text):
#     res = []
#     words = text.split()
#     for w in words:
#         w = w.replace(",", "").replace(".", "")
#         if w.isdigit():
#             res.append(int(w))
#     return res

# Задача 12
# base = []
# while True:
#     print("1-создать, 2-вывести класс, 3-удалить, 4-оценка, 5-инфо, 0-выход")
#     cmd = input("Команда: ")
#     if cmd == "0":
#         break
#     elif cmd == "1":
#         name = input("Имя: ")
#         cl = input("Класс: ")
#         base.append({"имя": name, "класс": cl, "оценки": []})
#     elif cmd == "2":
#         cl = input("Какой класс вывести: ")
#         for s in base:
#             if s["класс"] == cl:
#                 print(s["имя"])
#     elif cmd == "3":
#         name = input("Кого удалить: ")
#         for s in base:
#             if s["имя"] == name:
#                 base.remove(s)
#     elif cmd == "4":
#         name = input("Кому оценку: ")
#         num = int(input("Оценка: "))
#         for s in base:
#             if s["имя"] == name:
#                 s["оценки"].append(num)
#     elif cmd == "5":
#         name = input("Кого показать: ")
#         for s in base:
#             if s["имя"] == name:
#                 print("Имя:", s["имя"], "Класс:", s["класс"], "Оценки:", s["оценки"])
