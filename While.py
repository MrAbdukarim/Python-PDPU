#
## By MrAbdukarim 11/5/2024
#

# 1-vazifa
num = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))

while not num == 0:
    num2 = int(input("Raqam kiriting (0 kiritilganda tugaydi): "))
    if num > 0:
        num += num2
        print(num)
    if num2 == 0:
        break
print(num)

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

# 3-vazifa
numbers = []

while True:
    num = input("Raqam kiriting: ")
    if num.isdigit():
        numbers.append(num)
        numbers.sort()
        print("Listga muvofiqiyatli kiritildi:", numbers)

    if not num.isdigit():
        print("Xatolik bor!\n Kiritilgan raqamlar listi:", numbers)
        break

# 4-vazifa
x = [1, 2, 3, 14, 5, 6, 6, 7]
max_element = x[0]
i = 0

while not i == len(x):
    if max_element < x[i]:
        max_element = x[i]
    i += 1
print(max_element)

# 5-vazifa
x = [1, 2, 3, 14, 5, 6, 6, 7]
max_element = x[0]
i = 0

while not i == len(x):
    if max_element < x[i]:
        max_element = x[i]

    i += 1
print(x.index(max_element))
