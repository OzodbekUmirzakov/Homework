"""Integer 1: Santimetrlarni metrlarga aylantirish"""

# sm = int(input("Uzunlikni santimetrda kiriting: "))
# metr = sm / 100  # 1 metr = 100 santimetr
# print(f"Uzunlik metrda: {metr}")


"""Integer 2: Kilogrammlarni tonnalarga aylantirish"""

# kg = int(input("Og'irlikni kilogrammda kiriting: "))
# tonna = kg / 1000  # 1 tonna = 1000 kilogramm
# print(f"Og'irlik tonnalarda: {tonna}")


"""Integer 3: Baytlarni kilobaytlarga aylantirish"""

# bayt = int(input("Fayl hajmini baytlarda kiriting: "))
# kilobayt = bayt // 1024  # 1 Kilobayt = 1024 bayt
# print(f"Fayl hajmi kilobaytlarda: {kilobayt}")


"""Integer 4: A va B kesmalarini joylashtirish"""

# A = int(input("A kesmani kiriting (katta): "))
# B = int(input("B kesmani kiriting (kichik): "))
# joylashish = A // B
# print(f"B kesmasi A kesmasiga {joylashish} marta joylashadi")


"""Integer 5: A va B kesmalarini joylashmasini hisoblash"""

# A = int(input("A kesmani kiriting (katta): "))
# B = int(input("B kesmani kiriting (kichik): "))
# qoldiq = A % B
# print(f"Qoldiq qismning uzunligi: {qoldiq}")


"""Integer 6: Ikki xonali sonning raqamlar yig'indisini aniqlash"""

# son = int(input("Ikki xonali son kiriting: "))
# onlar = son // 10
# birliklar = son % 10
# yigindi = onlar + birliklar
# print(f"Raqamlar yig'indisi: {yigindi}")


"""Integer 7: Ikki xonali sonni teskari qilish"""

# son = int(input("Ikki xonali son kiriting: "))  # 54
# onlar = son // 10
# birliklar = son % 10
# teskari = birliklar * 10 + onlar  # teskari = 4 * 10 + 5 = 45
# print(f"Teskari son: {teskari}")


"""Integer 8: Uch xonali sonning yuzlar xonasidagi raqami"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# print(f"Yuzlar xonasidagi raqam: {yuzlar}")


"""Integer 9: Uch xonali sonning yuzlar xonasidagi raqami"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# print(f"Yuzlar xonasidagi raqam: {yuzlar}")


"""Integer 10: Birliklar xonasidagi raqamni so‘ng o‘nliklar bilan almashtirish"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# onliklar = (son % 100) // 10
# birliklar = son % 10
# teskari = yuzlar * 100 + birliklar * 10 + onliklar
# print(f"Birlik va o'nlik raqamlari almashtirilgandan keyingi son: {teskari}")


"""Integer 11: Uch xonali sonning raqamlar yig‘indisini aniqlash"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# onlar = (son % 100) // 10
# birliklar = son % 10
# yigindi = yuzlar + onlar + birliklar
# print(f"Raqamlar yig‘indisi: {yigindi}")


"""Integer 12: Raqamlarni teskari tartibda yozish"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# onlar = (son % 100) // 10
# birliklar = son % 10
# teskari = birliklar * 100 + onlar * 10 + yuzlar
# print(f"Sonning teskari yozuvi: {teskari}")


"""Integer 13: Chapdan birinchi raqamni o‘chirib yozish"""

# son = int(input("Uch xonali son kiriting: "))
#
# yuzlar = son // 100
# onliklar = (son % 100) // 10
# birliklar = son % 10
#
# yangi_son = onliklar * 100 + birliklar * 10 + yuzlar
#
# print(f"Chapdan birinchi raqam o‘chirib yozilgan son: {yangi_son}")


"""Integer 14: O‘ngdan birinchi raqamni o‘chirib yozish"""

# son = int(input("Uch xonali son kiriting: "))
#
# yuzlar = son // 100
# onliklar = (son % 100) // 10
# birliklar = son % 10
#
# yangi_son = birliklar * 100 + yuzlar * 10 + onliklar
#
# print(f"O‘ngdan birinchi raqam o‘chirib yozilgan son: {yangi_son}")


"""Integer 15: O‘nliklar va yuzliklar almashtirish"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# onliklar = (son % 100) // 10
# birliklar = son % 10
# almashtirilgan = onliklar * 100 + yuzlar * 10 + birliklar
# print(f"O‘nliklar va yuzliklar almashtirilgan son: {almashtirilgan}")


"""Integer 16: O‘nliklar va birliklar almashtirish"""

# son = int(input("Uch xonali son kiriting: "))
# yuzlar = son // 100
# onliklar = (son % 100) // 10
# birliklar = son % 10
# almashtirilgan = yuzlar * 100 + birliklar * 10 + onliklar
# print(f"O‘nliklar va birliklar almashtirilgan son: {almashtirilgan}")


"""Integer 17: 999 dan katta bo‘lgan sonni butun qismga aylantirish"""

# son = int(input("999 dan katta son kiriting: "))
# butun = son // 1000
# print(f"Butun qism: {butun}")


"""Integer 18: 999 dan katta bo‘lgan sonni qoldiq qismga aylantirish"""

# son = int(input("999 dan katta son kiriting: "))
# qoldiq = son % 1000
# print(f"Qoldiq qism: {qoldiq}")


"""Integer 19: Kun boshidan boshlab o‘tgan minutlarni hisoblash"""

# sekund = int(input("Kun boshidan o‘tgan sekundni kiriting: "))
# minut = sekund // 60
# print(f"O‘tgan minutlar: {minut}")


"""Integer 20: Kun boshidan boshlab o‘tgan soatlarni hisoblash"""

# sekund = int(input("Kun boshidan o‘tgan sekundni kiriting: "))
# soat = sekund // 3600
# print(f"O‘tgan soatlar: {soat}")


"""Integer 21: Kun boshidan boshlab o‘tgan soat va minutlarni hisoblash"""

# sekund = int(input("Kun boshidan o‘tgan sekundni kiriting: "))
# soat = sekund // 3600
# minut = (sekund % 3600) // 60
# print(f"O‘tgan soatlar: {soat}, Minutlar: {minut}")


"""Integer 22: Kun boshidan boshlab o‘tgan soat, minut va sekundlarni hisoblash"""

# sekund = int(input("Kun boshidan o‘tgan sekundni kiriting: "))
# soat = sekund // 3600
# minut = (sekund % 3600) // 60
# qoldiq_sekund = sekund % 60
# print(f"O‘tgan soat: {soat}, Minut: {minut}, Sekund: {qoldiq_sekund}")


"""Integer 23: Kun boshidan boshlab o‘tgan soat, minut va sekundlarni hisoblash"""

# sekund = int(input("Kun boshidan o‘tgan sekundni kiriting: "))
# soat = sekund // 3600
# minut = (sekund % 3600) // 60
# qoldiq_sekund = sekund % 60
# print(f"O‘tgan soat: {soat}, Minut: {minut}, Sekund: {qoldiq_sekund}")
