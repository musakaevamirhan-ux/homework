students = {}
while True:
    comandd = input('''add - добавить студента
remove -  удалить студента
list - просмотреть список студентов
exit - взавершить программу
''')
    print("--------------------")
    if comandd == "list":
        if students:
            for key,value in students.items():
                print(f"Интересы {key}: {",".join(value)}")
            print("--------------------")
        else:
            print("Список студентов пуст")
            print("--------------------")
    elif comandd == "exit":
        break
    elif comandd == "add":
        name = input("Введите имя и фамилию студента в родительном падеже через пробел: ")
        activities = set(input("Введите интересы студента через пробел: ").split())
        students[name] = activities
        print("Студент успешно добавлен")
        print("--------------------")
    elif comandd == "remove":
        name = input("Введите имя и фамилию студента в родительном падеже через пробел: ")
        if name in students:
            students.pop(name)
            print("Студент успешно удален")
            print("--------------------")
        else:
            print("Такого студента нет")
            print("--------------------")