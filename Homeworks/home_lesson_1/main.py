import math

"""1. Ikki sonning yig‘indisini aniqlaydigan dastur:"""
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# print("Yig‘indi:", a + b)


"""2. Ikki sonning ko‘paytmasini aniqlaydigan dastur:"""
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# print("Ko‘paytma:", a * b)


"""3. Sonni 7 ga bo‘lishdan qoldiqni topish dasturi:"""
# n = int(input("Sonni kiriting: "))
# print("7 ga bo‘lishdan qoldiq:", n % 7)


"""4. Ikki xonali sonni teskari aylantiradigan dastur:"""
# n = int(input("Ikki xonali sonni kiriting: "))
# print("Teskari son:", int(str(n)[::-1]))


# def reverse_number(number):
#     if 10 <= number <= 99:
#         reversed_number = (number % 10) * 10 + (number // 10)
#         return reversed_number
#     else:
#         return "Iltimos, ikki xonali son kiriting."
#
#
# number = int(input("Ikki xonali son kiriting: "))
# result = reverse_number(number)
# print(f"Teskari son: {result}")


"""5. B uzunlikdagi kesmani A uzunlikdagi kesmaga necha marta joylashtirish mumkin:"""
# A = float(input("A kesmaning uzunligini kiriting: "))
# B = float(input("B kesmaning uzunligini kiriting: "))
# print("Joylashish soni:", A // B)


"""6. Kiritilgan ismga salom beradigan dastur:"""
# ism = input("Ismingizni kiriting: ")
# print(f"Salom, {ism}")


"""7. So‘z boshiga va oxiriga “a” harfini qo‘shadigan dastur:"""
# soz = input("So‘zni kiriting: ")
# print(f"a{soz}a")


"""8. Berilgan so‘zni teskarisini aytadigan dastur:"""
# soz = input("So‘zni kiriting: ")
# print(f"{soz}siz")


"""9. Binodagi jami stollar sonini topish dasturi:"""
# A = int(input("Bino soni: "))
# B = int(input("Qavat soni: "))
# C = int(input("Xona soni: "))
# D = int(input("Stol soni: "))
# jami_stollar = A * B * C * D
# print(f"Jami stollar soni: {jami_stollar}")


"""10. Sonning kvadratini aniqlaydigan dastur:"""
# n = int(input("Sonni kiriting: "))
# print("Sonning kvadrati:", n ** 2)


# def calculate_square(num):
#     return num * num
#
#
# user_input = input("Sonni kiriting: ")
# number = float(user_input)
# square_result = calculate_square(number)
# print(f"{number} sonining kvadrati: {square_result}")


"""11. Kvadratning perimetri va yuzini aniqlaydigan dastur:"""
# a = float(input("Kvadratning tomonini kiriting: "))
# P = 4 * a
# S = a * a
# print(f"Perimetri: {P}, Yuzi: {S}")


"""12. Aylananing diametri va uzunligini topish dasturi:"""
# R = float(input("Radiusni kiriting: "))
# D = 2 * R
# # S = 3.141592653589793 * R ** 2
# # L = 2 * 3.141592653589793 * R
# S = math.pi * R ** 2
# L = 2 * math.pi * R
# print(f"Diametri: {D}, Yuzasi: {S}, Aylana uzunligi: {L}")


"""13. Burchakni radianga aylantiradigan dastur:"""
# gradus = float(input("Gradusni kiriting: "))
# radian = math.radians(gradus)
# print(f"Radianlar: {radian}")

# degrees = float(input("Burchakni gradusda kiriting: "))
# radians = degrees * (math.pi / 180)
# print(f"{degrees} gradus = {radians} radian")


"""14. Metrlarda berilgan uzunlikni santimetr, millimetr va kilometrga aylantirish dasturi:"""
# L = float(input("Uzunlikni metrda kiriting: "))
# print(f"Santimetr: {L * 100}, Millimetr: {L * 1000}, Kilometr: {L / 1000}")


"""15. Uch xonali sonning oxirgi raqamini 1 ga o‘zgartiradigan dastur:"""
# n = int(input("Uch xonali sonni kiriting: "))
# n = (n // 10) * 10 + 1
# print("Natija:", n)


"""16. Ikki o‘zgaruvchining qiymatlarini uchinchi o‘zgaruvchi ishlatmasdan almashtirish dasturi:"""
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# a, b = b, a
# print(f"Endi a = {a}, b = {b}")

"""17. Uch o‘zgaruvchini qiymatlarini aylantirib almashtirish dasturi:"""
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# c = int(input("c ni kiriting: "))
# a, b, c = b, c, a
# print(f"a = {a}, b = {b}, c = {c}")

"""18. Uchta nuqta bo‘yicha AB, AC va BC kesmalarning uzunligini topish dasturi:"""
# A = float(input("A nuqtasining koordinatasini kiriting: "))
# B = float(input("B nuqtasining koordinatasini kiriting: "))
# C = float(input("C nuqtasining koordinatasini kiriting: "))
# AB = abs(A - B)
# AC = abs(A - C)
# BC = abs(B - C)
# print(f"AB uzunligi: {AB}, AC uzunligi: {AC}, BC uzunligi: {BC}")
