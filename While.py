#
## By MrAbdukarim 11/5/2024
#
#
# # 1-vazifa
# num = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))
#
# while not num == 0:
#     num2 = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))
#     if num > 0:
#         num += num2
#         print(num)
#     if num2 == 0:
#         break
# print(num)
#
# # 2-vazifa
# num_a = int(input("A soni kiriting: "))
# num_b = int(input("B soni kiriting: "))
# summa = 0
#
# if num_a > num_b:
#     num_a, num_b = num_b, num_a
#
# while num_a <= num_b:
#     summa += num_a
#     num_a += 1
# print(summa)
#
# # 3-vazifa
# numbers = []
#
# while True:
#     num = input("Raqam kiriting: ")
#     if num.isdigit():
#         numbers.append(num)
#         numbers.sort()
#         print("Listga muvofiqiyatli kiritildi:", numbers)
#
#     if not num.isdigit():
#         print("Xatolik bor!\n Kiritilgan raqamlar listi:", numbers)
#         break
#
# # 4-vazifa
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# max_element = x[0]
# i = 0
#
# while not i == len(x):
#     if max_element < x[i]:
#         max_element = x[i]
#     i += 1
# print(max_element)
#
# # 5-vazifa
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# max_element = x[0]
# i = 0
#
# while not i == len(x):
#     if max_element < x[i]:
#         max_element = x[i]
#     i += 1
# print(x.index(max_element))
#
# # 6-vazifa
# num = input("Sonni kiriting: ")
#
# summa = 0
#
# while not summa == len(num):
#     if num.isdigit():
#         summa += 1
#     else:
#         print(f"Xatolik bor! \n {summa}")
#         break
# print(f"Xonalar soni: {summa}")
#
# # 7-vazifa
# x = [1, 2, 0, 14, 5, -6]
# max_element = x[0]
# min_element = x[0]
# i = 0
#
# while not i == len(x):
#     if max_element < x[i]:
#         max_element = x[i]
#     if min_element > x[i]:
#         min_element = x[i]
#     i += 1
# print(max_element, min_element)
#
# # 8-vazifa
# x = [-2, 31, 104, 51, 19, 7]
# max_element = x[0]
# min_element = x[0]
# i = 0
#
# while not i == len(x):
#     if max_element < x[i]:
#         max_element = x[i]
#
#     if min_element > x[i]:
#         min_element = x[i]
#     i += 1
#
# # box = max_element
# # x.index(max_element) = min_element
# # x.index(min_element) = max_element
#
# max_index = x.index(max_element)
# min_index = x.index(min_element)
#
# box = x[max_index]
# x[max_index] = x[min_index]
# x[min_index] = box
#
# print(x)

# # 9-vazifa
# x = [-2, 31, 104, 51, 19, 7]
# num = int(input("Son kiriting: "))
# i = 0
#
# while not i == len(x):
#     if num == x[i]:
#         print("Element bor")
#         break
#     i += 1
#
# else:
#     print("Element yo'q")

# A = int(input("A sonni kiriting: "))
# B = int(input("B sonni kiriting: "))
#
# result = 0
#
# while B == 0:
#     result = A % B
#
# print(result)
