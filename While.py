#
## By MrAbdukarim 11/5/2024
#
#
# num = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))
# summa = 0
#
# while num > 0:
#     num2 = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))
#     summa += num + num2
#     print("Yig'indi:", summa)
#     if num2 > 0:
#         summa += num2
# else:
#     print(summa)

# 2-vazifa
num_a = int(input("A soni kiriting: "))
num_b = int(input("B soni kiriting: "))
summa = 0

if num_a > num_b:
    num_a, num_b = num_b, num_a

while num_a <= num_b:
    summa += num_a
    num_a += 1
print(summa)
