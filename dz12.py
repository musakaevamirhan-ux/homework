base = []
while True:
    print("1-добавить студента, 2-вывести класс, 3-удалить студента, 4-добавить оценку, 5-изменить оценку, 6-удалить оценку, 7-инфо, 8-создать класс из 4 студентов по 4 оценки, 0-выход")
    cmd = input("Команда: ")
    if cmd == "0":
        break
    elif cmd == "1":
        name = input("Имя: ")
        cl = input("Класс: ")
        base.append({"имя": name, "класс": cl, "оценки": []})
    elif cmd == "2":
        cl = input("Какой класс вывести: ")
        for s in base:
            if s["класс"] == cl:
                print(s["имя"])
    elif cmd == "3":
        name = input("Кого удалить: ")
        for s in base:
            if s["имя"] == name:
                base.remove(s)
    elif cmd == "4":
        name = input("Кому оценку: ")
        num = int(input("Оценка: "))
        for s in base:
            if s["имя"] == name:
                s["оценки"].append(num)
    elif cmd == "5":
        name = input("Кому изменить оценку: ")
        for s in base:
            if s["имя"] == name:
                print("Текущие оценки:", s["оценки"])
                idx = int(input("Индекс оценки для изменения (с 0): "))
                new_val = int(input("Новое значение: "))
                s["оценки"][idx] = new_val
    elif cmd == "6":
        name = input("Кому удалить оценку: ")
        for s in base:
            if s["имя"] == name:
                print("Текущие оценки:", s["оценки"])
                idx = int(input("Индекс оценки для удаления (с 0): "))
                s["оценки"].pop(idx)
    elif cmd == "7":
        name = input("Кого показать: ")
        for s in base:
            if s["имя"] == name:
                print("Имя:", s["имя"], "Класс:", s["класс"], "Оценки:", s["оценки"])
    elif cmd == "8":
        clname = input("Введите название класса: ")
        for i in range(4):
            name = input("Введите имя студента: ")
            marks = [int(m) for m in input("Введите 4 оценки через пробел: ").split()]
            base.append({"имя": name, "класс": clname, "оценки": marks})
