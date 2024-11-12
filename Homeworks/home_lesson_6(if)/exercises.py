"""1. Butun son berilgan. Agar son musbat bo'lsa, 1 ga oshiriladi.
      Aks holda o'zgartirilmaydi.
"""


# x = int(input("Sonni kiriting: "))
#
# if x > 0:
#     x += 1
#
# print("Natija:", x)


"""2. Butun son berilgan. Agar son musbat bo'lsa, 1 ga oshiriladi.
      Aks holda 2 ga kamaytiriladi.
"""

# x = int(input("Sonni kiriting: "))
#
# if x > 0:
#     x += 1
# else:
#     x -= 2
#
# print("Natija:", x)


"""3. Butun son berilgan. Agar son musbat bo'lsa, 1 ga oshiriladi,
      agar manfiy bo'lsa 2 ga kamaytiriladi, agar 0 bo'lsa 10 o'rnatiladi.
"""

# x = int(input("Sonni kiriting: "))
#
# if x > 0:
#     x += 1
# elif x < 0:
#     x -= 2
# else:
#     x = 10
#
# print("Natija:", x)


"""4. Uchta butun son berilgan. Musbat sonlar sonini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# count = 0
# if x > 0:
#     count += 1
# if y > 0:
#     count += 1
# if z > 0:
#     count += 1
#
# print("Musbat sonlar soni:", count)


"""5. Uchta butun son berilgan. Musbat va manfiy sonlar sonini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# musbat = 0
# manfiy = 0
#
# if x > 0:
#     musbat += 1
# if y > 0:
#     musbat += 1
# if z > 0:
#     musbat += 1
#
# if x < 0:
#     manfiy += 1
# if y < 0:
#     manfiy += 1
# if z < 0:
#     manfiy += 1
#
# print("Musbat sonlar soni:", musbat)
# print("Manfiy sonlar soni:", manfiy)


"""6. Ikkita butun son berilgan. Kattasini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
#
# if x > y:
#     print("Katta son:", x)
# else:
#     print("Katta son:", y)


"""7. Ikkita butun son berilgan. Kichik sonning tartib raqamini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
#
# if x < y:
#     print("Kichik sonning tartib raqami: 1")
# else:
#     print("Kichik sonning tartib raqami: 2")


"""8. Ikkita butun son berilgan. Avval kattasi, keyin kichigi chiqariladi."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
#
# if x > y:
#     print("Katta son:", x)
#     print("Kichik son:", y)
# else:
#     print("Katta son:", y)
#     print("Kichik son:", x)


"""9. A va B sonlari berilgan. A son kichik, B son katta bo'lishi kerak."""

# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))
#
# if A > B:
#     A, B = B, A
#
# print("A:", A, "B:", B)


"""10. A va B sonlari berilgan. Agar teng bo'lmasa, A va B o'zgaruvchilari
       yig'indisiga tenglashtiriladi. Teng bo'lsa, 0 ga tenglashtiriladi.
"""

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# if A != B:
#     A = B = A + B
# else:
#     A = B = 0
#
# print("A:", A, "B:", B)


"""11. A va B sonlari berilgan. Agar teng bo'lmasa kattasini o'rnatish,
       aks holda 0 ni o'rnatish kerak.
"""

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# if A != B:
#     if A > B:
#         B = A
#     else:
#         A = B
# else:
#     A = B = 0
#
# print("A:", A, "B:", B)


"""12. Uchta butun son berilgan. Eng kichik sonni aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# if x > y:
#     x = y
# if x > z:
#     x = z
#
# print("Eng kichik son:", x)


"""13. Uchta butun son berilgan. O'rtacha (katta va kichik son orasidagi) sonni aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# if (y < x < z) + (z < x < y):
#     middle = x
# elif (x < y < z) + (z < y < x):
#     middle = y
# else:
#     middle = z
#
# print("Ortadagi son:", middle)


"""14. Uchta son berilgan. Ularni avval kichigini, keyin kattasini chiqaruvchi dastur."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# if x > y:
#     x, y = y, x
# if x > z:
#     x, z = z, x
# if y > z:
#     y, z = z, y
#
# print("Kichik son:", x)
# print("Katta son:", z)


"""15. Uchta son berilgan. Yig'indisi eng katta bo'lgan ikkita sonni chiqarish kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# if x + y >= x + z and x + y >= y + z:
#     print(f"Eng katta yig'indiga ega sonlar: {x} va {y}")
# elif x + z >= x + y and x + z >= y + z:
#     print(f"Eng katta yig'indiga ega sonlar: {x} va {z}")
# else:
#     print(f"Eng katta yig'indiga ega sonlar: {y} va {z}")


"""16. A, B, C haqiqiy sonlari berilgan. Agar sonlar o'sish tartibida berilgan bo'lsa, ularni ikki marta oshirish,
       aks holda ishorasini o'zgartirish kerak.
"""

# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))
# C = float(input("C sonini kiriting: "))
#
# if A < B < C:
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
#
# print("A:", A, "B:", B, "C:", C)


"""17. A, B, C haqiqiy sonlari berilgan. Agar kamayish tartibida berilgan bo'lsa, ularni ikki marta oshirish,
       aks holda ishorasini o'zgartirish kerak.
"""

# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))
# C = float(input("C sonini kiriting: "))
#
# if A > B > C:
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
#
# print("A:", A, "B:", B, "C:", C)


"""18. Uchta butun son berilgan. Ikkitasi o'zaro teng, qolganining tartib raqamini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
#
# if x == y:
#     print("Tartib raqami:", 3)
# elif x == z:
#     print("Tartib raqami:", 2)
# else:
#     print("Tartib raqami:", 1)


"""19. To'rt butun son berilgan. Uchta o'zaro teng, qolganining tartib raqamini aniqlash kerak."""

# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
# w = int(input("4-sonni kiriting: "))
#
# if x == y == z:
#     print("Tartib raqami:", 4)
# elif x == y == w:
#     print("Tartib raqami:", 3)
# elif x == z == w:
#     print("Tartib raqami:", 2)
# else:
#     print("Tartib raqami:", 1)


"""20. Sonlar o'qida uchta A, B, C nuqtalar berilgan. 
       A nuqtaga eng yaqin nuqtani va ular orasidagi masofani topish kerak.
"""

# A = float(input("A nuqtani kiriting: "))
# B = float(input("B nuqtani kiriting: "))
# C = float(input("C nuqtani kiriting: "))
#
# masofa_B = abs(A - B)
# masofa_C = abs(A - C)
#
# if masofa_B < masofa_C:
#     print("Eng yaqin nuqta: B, masofa:", masofa_B)
# else:
#     print("Eng yaqin nuqta: C, masofa:", masofa_C)


"""21. Koordinatalar tekisligida butun son berilgan. Agar nuqta boshida bo'lsa, 0 chiqsin.
       Agar OX yoki OY o'qida joylashgan bo'lsa, mos ravishda 1 yoki 2 chiqsin.
       O'qda joylashmagan bo'lsa, 3 chiqsin.
"""

# x = int(input("X koordinatasini kiriting: "))
# y = int(input("Y koordinatasini kiriting: "))
#
# if x == 0 and y == 0:
#     print(0)
# elif x == 0:
#     print(1)
# elif y == 0:
#     print(2)
# else:
#     print(3)


"""22. OX va OY koordinata o'qlarida joylashmagan nuqta berilgan. 
       Nuqta joylashgan koordinata choragini aniqlash kerak.
"""

# x = int(input("X koordinatasini kiriting: "))
# y = int(input("Y koordinatasini kiriting: "))
#
# if x > 0 and y > 0:
#     print("1-chorak")
# elif x < 0 and y > 0:
#     print("2-chorak")
# elif x < 0 and y < 0:
#     print("3-chorak")
# elif x > 0 and y < 0:
#     print("4-chorak")


"""23. Koordinata o'qlariga parallel ravishda to'rtburchakning uchta uchi berilgan, to'rtinchisini aniqlash kerak."""

# x1 = int(input("1-uchning X koordinatasi: "))
# y1 = int(input("1-uchning Y koordinatasi: "))
# x2 = int(input("2-uchning X koordinatasi: "))
# y2 = int(input("2-uchning Y koordinatasi: "))
# x3 = int(input("3-uchning X koordinatasi: "))
# y3 = int(input("3-uchning Y koordinatasi: "))
#
# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1
#
# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1
#
# print(f"To'rtinchi uchning koordinatalari: ({x4}, {y4})")
