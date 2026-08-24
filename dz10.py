def max_string(x,n):
        n -= 1
        o = max(x[n])
        l = x[n].index(o)
        print(f"Максимум в {n+1} строке - {o} с индексом {l}")
def min_string(x,n):
    n -= 1
    o = min(x[n])
    l = x[n].index(o)
    print(f"Минимум в {n+1} строке - {o} с индексом {l}")
def middle_value_and_sum_string(x,n,m):
    n -= 1
    summ = sum(x[n])
    print(f"Сумма всех элементов {n+1} строки - {summ}")
    print(f"Среднее арефметическое в {n+1} строке - {summ/m}")
def max_colomn(x,n,m):
    maxx = [x[0][m-1], 0]
    for i in range(1,n):
        if x[i][m-1] > maxx[0]:
            maxx = [x[i][m-1], i]
        print(f"Максимум в {m} столбце - {maxx[0]} с индексом {maxx[1]}")
def min_colomn(x,n,m):
    minn = [x[0][m-1], 0]
    for i in range(1, n):
        if x[i][m-1] < minn[0]:
            minn = [x[i][m-1], i]
        print(f"Минимум в {m} столбце - {minn[0]} с индексом {minn[1]}")
def middle_value_and_sum_colomn(x,n,m):
    summ = 0
    for i in range(n):
        summ += x[i][m-1]
    print(f"Сумма всех элементов {i+1} столбца - {summ}")
    print(f"Среднее арефметическое в {i+1} столбце - {summ/n}")
def find_max(x,n,m):
    maxx = [x[0][0], 0, 0]
    for i in range(n):
        for j in range(m):
            if x[i][j] > maxx[0]:
                maxx = [x[i][j], i, j]
    print(f"Наибольшее значение - {maxx[0]} в {maxx[1]} строке и {maxx[2]} столбце")
def find_min(x,n,m):
    minn = [x[0][0], 0, 0]
    for i in range(n):
        for j in range(m):
            if x[i][j] < minn[0]:
                minn = [x[i][j], i, j]
    print(f"Наименьшее значение - {minn[0]} в {minn[1]} строке и {minn[2]} столбце")
def middle_value_and_sum(x,n,m):
    summ = 0
    for i in range(n):
        for j in range(m):
            summ += x[i][j]
    print(f"Сумма - {summ}")
    print(f"Среднее арефметическое - {summ/(m*n)}")

