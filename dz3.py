# 1
# a = int(input())
# b = int(input())
# if a > b:
#     a, b = b, a
# sum = 0
# while a <= b:
#     sum += a
#     a += 1
# print(sum)
# 2
# a = abs(int(input()))
# b = abs(int(input()))
# if b > a:
#     a, b = b, a
# k = b
# while k <= b:
#     if b % k == 0 and a % k == 0:
#         break
#     k -= 1
# print(k)
# 3
# a = int(input())
# k = 1
# while k <= a:
#     if a % k == 0:
#         print(k, end=" ")
#     k += 1
# 4
# a = int(input())
# k = 10
# s = 0
# while a != 0:
#     a//=10
#     s += 1
# print(s)
# 5
# a = 1
# zero = 0
# plus = 0
# minus = 0
# chet = 0
# nechet = 0
# while a <= 10:
#     a += 1
#     b = int(input())
#     if b == 0:
#         zero += 1
#     if b > 0:
#         plus += 1
#     if b < 0:
#         minus += 1
#     if b%2 != 0:
#         nechet += 1
#     if b%2 == 0:
#         chet += 1
# print(zero)
# print(plus)
# print(minus)
# print(nechet)
# print(chet)
