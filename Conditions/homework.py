#
## By MrAbdukarim 11/4/2024
#

# 1-vazifa
grade = int(input("Sinfingizni kiriting(1-11): "))
score = int(input("Bahoyingizni kiriting(0-100): "))

if 1 <= grade <= 11:
    if grade >= 5:
        if score > 90:
            print(f'Siz {grade}-sinfsiz va ballingiz {score}/100. Sizga mukofot beriladi.')
        elif score > 70:
            print(f"Siz {grade}-sinfsiz va ballingiz {score}/100. Sizga ma'qullangan belgisi qo'yiladi.")
        else:
            print(f'Siz {grade}-sinfsiz va ballingiz {score}/100. Sizning natijangiz qoniqarsiz.')
    if grade < 5:
        if score > 85:
            print(f'Siz {grade}-sinfsiz va ballingiz {score}/100. Sizga mukofot beriladi.')
        elif score > 60:
            print(f"Siz {grade}-sinfsiz va ballingiz {score}/100. Sizga ma'qullangan belgisi qo'yiladi.")
        else:
            print(f'Siz {grade}-sinfsiz va ballingiz {score}/100. Sizning natijangiz qoniqarsiz.')
else:
    print("Xatolik bor!")

# 2-vazifa
car_year = int(input("Avtomobilni yilini kiriting: "))
driver_age = int(input("Yoshingizni kiriting: "))

if car_year >= 2020:
    cost = 500 if driver_age > 25 else 700
elif car_year >= 2015:
    cost = 600 if driver_age > 25 else 800
else:
    cost = 700 if driver_age > 25 else 900

print(f"Avtomobilingiz yili {car_year}.\n Sug'urta narxi: {cost}$")

# 3-vazifa
experience = int(input("Xodim tajribasini kiriting: "))
level = input("Darajasini kiriting(yuqori, o'rta va past): ")

if experience > 10:
    if level == "yuqori" or "Yuqori":
        bonus = 20
    elif level == "o'rta" or "O'rta":
        bonus = 15
    else:
        bonus = 10

elif experience > 5:
    if level == "yuqori" or "Yuqori":
        bonus = 15
    else:
        bonus = 10
else:
    bonus = 5

print(f"Xodimning tajribasi {experience} yil va darajasi {level}.\nBonus: {bonus}%")
# 4-vazifa
balance = int(input("Balansingizni kiriting($): "))
card_type = input("Karta turini kiriting (premium, standard va boshqa): ")

if balance > 10000:
    if card_type == "premium" or "Premium":
        limit = 5000
    elif card_type == "standard" or "Standard":
        limit = 3000
    else:
        limit = 2000
elif balance > 5000:
    if card_type == "premium" or "Premium":
        limit = 2500
    else:
        limit = 1500
else:
    limit = 500

print(f"Balansingiz: ${balance} va karta turi {card_type}.\nYechib olish limiti: {limit}$")

# 5-vazifa
fruit_type = input("Meva turini kiriting: ")
kg = int(input("Miqdorni kiriting: "))

if fruit_type == "olma":
    bonus = 15 if kg > 10 else 10
elif fruit_type == "banan":
    bonus = 12 if kg > 5 else 8
else:
    bonus = 10 if kg > 8 else 5

print(f"Meva turi {fruit_type} va miqdor {kg} kg.\nChegirma: {bonus}%")

# 6-vazifa
rating = int(input("Reytingingizni kiriting: "))
experience = int(input("Tajribangizni kiriting: "))

if rating > 2000:
    level = "Ekspert" if experience > 5 else "Advanced"
elif rating > 1500:
    level = "Advanced" if experience > 3 else "Intermediate"
else:
    level = "Intermediate" if experience > 1 else "Beginner"

print(f"Reytingingiz {rating} va tajribangiz {experience} yil.\nDarajangiz: {level}")

# 7-vazifa
speed = int(input("Tezlikni kiriting: "))
date = int(input("Muddatni kiriting (oy): "))

if speed > 100:
    price = 50 if date > 12 else 60
elif speed > 50:
    price = 40 if date > 6 else 45
else:
    price = 30

print(f"Tezlik {speed} Mbps va muddati {date} oy.\nNarx: ${price}")

# 8-vazifa
score = int(input("O'rtacha bahoni kiriting: "))
subjects_sum = int(input("Qatnashgan fanlar sonini kiriting: "))

if score > 85:
    stipendiya = "100%" if subjects_sum > 5 else "75%"
elif score > 70:
    stipendiya = "50%" if subjects_sum > 3 else "25%"
else:
    stipendiya = "Stipendiya berilmaydi"

print(f"O'rtacha baho {score} va fanlar soni {subjects_sum}.\nStipendiya: {stipendiya}")
