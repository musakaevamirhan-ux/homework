# 1
# size = int(input())
# for i in range(size):
#     for j in range(size):
#         if j >= i:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# 2
# size = int(input())
# for i in range(size):
#     for j in range(size):
#         if j <= i:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# 3
# size = int(input())
# for i in range(size):
#     for j in range(size):
#         if i<=j<size-i:
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     print()
# 4
# size = int(input())
# for i in range(size):
#     if i >= size // 2:
#         for j in range(size):
#             if size - i - 1<=j<=i:
#                 print("* ",end=" ")
#             else:
#                 print("  ",end=" ")
#     else:
#         print("  ")
#         continue
#     print()
# 5
# size = int(input())
# for i in range(size):
#         if i >= size // 2:
#             for j in range(size):
#                 if size - i - 1<=j<=i:
#                     print("* ",end=" ")
#                 else:
#                     print("  ",end=" ")
#         else:
#             for j in range(size):
#                 if i <= j < size - i:
#                     print("* ",end=" ")
#                 else:
#                     print("  ",end=" ")
#         print()
# 6
# size = int(input())
# for i in range(size):
#         if i <= size // 2:
#             for j in range(size):
#                 if j <= i or j >= size - i-1:
#                     print("* ", end=" ")
#                 else:
#                     print("  ", end=" ")
#         else:
#             for j in range(size):
#                 if j <= size - i - 1 or j >= i:
#                     print("* ", end=" ")
#                 else:
#                     print("  ", end=" ")
#         print()
# 7
# size = int(input())
# for i in range(size):
#         if i <= size // 2:
#             for j in range(size):
#                 if j <= size // 2:
#                     if j <= i or j >= size - i-1:
#                         print("* ", end=" ")
#                     else:
#                         print("  ", end=" ")
#                 else:
#                     print("  ", end=" ")
#                     continue
#         else:
#             for j in range(size):
#                 if j <= size // 2:
#                     if j <= size - i - 1 or j >= i:
#                         print("* ", end=" ")
#                     else:
#                         print("  ", end=" ")
#                 else:
#                     print("  ", end=" ")
#                     continue
#         print()
# 8
# size = int(input())
# for i in range(size):
#         if i <= size // 2:
#             for j in range(size):
#                 if j >= size // 2:
#                     if j <= i or j >= size - i-1:
#                         print("* ", end=" ")
#                     else:
#                         print("  ", end=" ")
#                 else:
#                     print("  ", end=" ")
#                     continue
#         else:
#             for j in range(size):
#                 if j >= size // 2:
#                     if j <= size - i - 1 or j >= i:
#                         print("* ", end=" ")
#                     else:
#                         print("  ", end=" ")
#                 else:
#                     print("  ", end=" ")
#                     continue
#         print()
# 9
# size = int(input())
# for i in range(size):
#     for j in range(size):
#         if j < size - i:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# 10
# size = int(input())
# for i in range(size):
#     for j in range(size):
#         if j >= size - i - 1:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

