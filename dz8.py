def  number_sequence(start, end, even=True):
    for i in range(start, end+1):
        if even == True and i % 2 == 0:
            yield i
        if even == False and i % 2 != 0:
            yield i
try:
    start = int(input())
    end = int(input())
    even = input()
    if even == "True":
        even = True
    elif even == "False":
        even = False
    result = number_sequence(start, end, even)
    print(*result)
except ValueError:
    print("Вводите целые числа или True или False")

