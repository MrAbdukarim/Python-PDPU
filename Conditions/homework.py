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