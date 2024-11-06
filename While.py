#
## By MrAbdukarim 11/5/2024
#
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
#         print(num)
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
# while len(numbers) < 5:
#     num = int(input("Raqam kiriting: "))
#     numbers.append(num)
#     numbers.sort()
#
# print("Kiritilgan raqamlar listi:", numbers)
#
# # 4-vazifa
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# max_element = x[0]
# i = 1
#
# while i < len(x):
#     if x[i] > max_element:
#         max_element = x[i]
#     i += 1
#
# print("Eng katta element:", max_element)
#
# # 5-vazifa
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# max_element = x[0]
# max_index = 0
# i = 1
#
# while i < len(x):
#     if x[i] > max_element:
#         max_element = x[i]
#         max_index = i
#     i += 1
#
# print("Eng katta element indexi:", max_index)
#
# # 6-vazifa
# num = input("Son kiriting: ")
# summa = 0
#
# while summa < len(num):
#     summa += 1
#
# print("Xonalar soni:", summa)
#
# # 7-vazifa
# x = [1, 2, 0, 14, 5, -6]
# max_element = x[0]
# min_element = x[0]
# summa = 1
#
# while summa < len(x):
#     if x[summa] > max_element:
#         max_element = x[summa]
#     if x[summa] < min_element:
#         min_element = x[summa]
#     summa += 1
#
# print(f"Eng katta element: {max_element}, Eng kichik element: {min_element}")
