#uyishi
#1
son = 5
son1 = 10
print(son+son1)
print(son-son1)
print(son*son1)
print(son/son1)
#2
ism  = input("Ismingizni kiriting: ")
yosh = input("Yilingizni kiriting: ")
print(f"Sizning ismingiz {ism}, Yoshingiz {yosh} dasiz.")
#3
x = int(input("Bo‘linuvchi faqat butun ni kiriting: "))
y = int(input("Bo‘luvchi faqat butun ni kiriting: "))

if y != 0:
    butun, qoldiq = divmod(x, y)
    print(f"Butun qism : {butun}")
    print(f"Qoldiq     : {qoldiq}")
else:
    print("0 ga bo‘lish mumkin emas!")
#4
r  = float(input("Radiusni kiriting: "))
pi = 3.14

yuza        = pi * r ** 2
aylana_uzun = 2 * pi * r

print(f"Doira yuza        : {yuza}")
print(f"Aylana uzunligi   : {aylana_uzun}")
#5
n = float(input("Sonni kiriting: "))

print(f"Kvadrat : {n ** 2}")
print(f"Kub     : {n ** 3}")