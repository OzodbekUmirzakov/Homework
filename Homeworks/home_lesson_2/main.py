"""1. Stringlarni qo‘shish (concatenation):
Foydalanuvchi ismi va familiyasini alohida kiritadi.
Ushbu ismlar stringlar sifatida saqlansin va birlashtirilgan to‘liq ismni ekranga chiqaring."""

# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# toliq_ism = ism + " " + familiya
# print(f"To'liq ismingiz: {toliq_ism}")


"""2. f-stringni qo‘llash:
Foydalanuvchi ismi va yoshi kiritiladi. f-strings yordamida matnni shunday chiqaring: 
"Sizning ismingiz [ism], yoshingiz [yosh].”"""

# ism = input("Ismingizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
# print(f"Sizning ismingiz {ism}, yoshingiz {yosh}.")


"""3. upper(), lower(), title(), capitalize() amallarini qo‘llash:
Foydalanuvchi biror matn kiritadi. Shu matnni quyidagicha ekranga chiqaring: 
katta harflarda, kichik harflarda, sarlavha usulida (title), birinchi harfini katta qilib."""

# matn = input("Biror matn kiriting: ")
# print("Katta harflarda:", matn.upper())
# print("Kichik harflarda:", matn.lower())
# print("Sarlavha usulida:", matn.title())
# print("Birinchi harfi katta:", matn.capitalize())


"""4. trip(), rstrip(), lstrip() amallarini qo‘llash:
Foydalanuvchi bo‘shliqlar bilan boshlangan va tugagan biror matn kiritadi. 
Shu matndan barcha bo‘shliqlarni olib tashlang, 
faqat o‘ng yoki faqat chap tomondagi bo‘shliqlarni olib tashlab natijani ekranga chiqaring."""

# matn = input("Bo‘shliqlar bilan boshlangan yoki tugagan matn kiriting: ")
# print("Barcha bo‘shliqlardan tozalangan:", matn.strip())
# print("Chap tomondagi bo‘shliqlardan tozalangan:", matn.lstrip())
# print("O‘ng tomondagi bo‘shliqlardan tozalangan:", matn.rstrip())


"""5. Inputdan olingan qiymatlar bilan stringlar:
Foydalanuvchidan ismingiz, yoshingiz va sevimli rangingizni so'rang. 
Olingan ma'lumotlar bilan quyidagi formatda matn chiqaring: 
"Salom, [ism]. Siz [yosh] yoshdasiz va sizning sevimli rangingiz [rang].”"""

# ism = input("Ismingizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
# rang = input("Sevimli rangingizni kiriting: ")
# print(f"Salom, {ism}. Siz {yosh} yoshdasiz va sizning sevimli rangingiz {rang}.")


"""6. Bir nechta amallarni birlashtirish:
Foydalanuvchidan ismni kichik harflarda kiritishni so‘rang. 
Keyin ushbu ismni katta harflarda chiqaring va keyin to‘liq formatlangan holda (faqat birinchi harfini katta) qayta yozing."""

# ism = input("Ismingizni kichik harflarda kiriting: ")
# print("Katta harflarda:", ism.upper())
# print("To‘liq formatlangan holda:", ism.capitalize())


"""7. Oddiy arifmetik amallar:
Foydalanuvchidan ikkita son kiritishni so'rang. 
Ushbu sonlar ustida qo'shish, ayirish, ko'paytirish, bo'lish va 
darajaga ko'tarish amallarini bajaring va natijalarni ekranga chiqaring."""

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# print(f"Qo‘shish: {son1} + {son2} = {son1 + son2}")
# print(f"Ayirish: {son1} - {son2} = {son1 - son2}")
# print(f"Ko‘paytirish: {son1} * {son2} = {son1 * son2}")
# print(f"Bo‘lish: {son1} / {son2} = {son1 / son2}")
# print(f"Darajaga ko‘tarish: {son1} ** {son2} = {son1 ** son2}")


"""8. Float bilan amallar:
Foydalanuvchidan ikkita haqiqiy (float) son kiritishni so'rang. 
Ular ustida bo'lish va darajaga ko'tarish amallarini bajaring, natijalarni ekranga chiqaring."""

# son1 = float(input("Birinchi haqiqiy sonni kiriting: "))
# son2 = float(input("Ikkinchi haqiqiy sonni kiriting: "))
#
# print(f"Bo‘lish: {son1} / {son2} = {son1 / son2}")
# print(f"Darajaga ko‘tarish: {son1} ** {son2} = {son1 ** son2}")


"""9. Type() metodi:
Foydalanuvchidan biror ma'lumot kiritishni so'rang. 
Bu kiritilgan qiymatning turini type() yordamida aniqlang va ekranga chiqaring."""

# malumot = input("Biror ma'lumot kiriting: ")
# print(f"Kiritilgan qiymat turi: {type(malumot)}")


"""10. Type casting (cating):
Foydalanuvchidan ikkita son kiritishni so'rang. 
Ularni avval stringga o'girib qo'shing, keyin integerga o'girib qo'shing va natijalarni solishtiring."""

# son1 = input("Birinchi sonni kiriting: ")
# son2 = input("Ikkinchi sonni kiriting: ")
#
# string_qoshish = son1 + son2
# print(f"String sifatida qo'shish: {string_qoshish}")
#
# integer_qoshish = int(son1) + int(son2)
# print(f"Integer sifatida qo'shish: {integer_qoshish}")


"""11. Bool bilan shartlarni tekshirish:
Foydalanuvchidan son kiritishni so'rang va shu son 10 dan katta yoki kichikligini tekshirib,
natijani True yoki False sifatida ekranga chiqaring."""

# son = int(input("Biror son kiriting: "))
# natija = son > 10
# print(f"Son 10 dan kattami? {natija}")


"""12. Arifmetik amallar va type casting:
Foydalanuvchidan ikkita son kiritib, ularni qo'shing, lekin avval sonlardan birini floatga o‘giring va 
keyin natijani integer yoki float qiymat sifatida chiqaring."""

# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# natija = son1 + son2
#
# print(f"Natija float qiymatida: {natija}")
# print(f"Natija integer qiymatida: {int(natija)}")


"""13. Mantiqiy operatsiyalar:
Foydalanuvchidan son kiritib, shu sonning juft yoki toq ekanligini tekshiring va 
natijani True yoki False sifatida chiqaring."""

# son = int(input("Biror son kiriting: "))
# natija = (son % 2 == 0)
# print(f"Son juftmi? {natija}")


"""14. Perimetr va yuzani hisoblash:
Foydalanuvchidan to‘rtburchakning uzunligi va eni kiritilishini so‘rang. 
To‘rtburchakning perimetrini va yuzasini hisoblang."""

# uzunlik = float(input("To‘rtburchakning uzunligini kiriting: "))
# eni = float(input("To‘rtburchakning enini kiriting: "))
#
# perimetr = 2 * (uzunlik + eni)
# yuzasi = uzunlik * eni
#
# print(f"To‘rtburchakning perimetri: {perimetr}")
# print(f"To‘rtburchakning yuzasi: {yuzasi}")


"""15. Aylananing uzunligi va yuzasi:
Foydalanuvchidan aylananing radiusini float shaklda kiritishni so‘rang. 
Aylananing uzunligi va yuzasini hisoblang (π = 3.14 deb oling). """

# radius = float(input("Aylananing radiusini kiriting: "))
# pi = 3.14
#
# uzunlik = 2 * pi * radius
# yuza = pi * (radius ** 2)
#
# print(f"Aylananing uzunligi: {uzunlik}")
# print(f"Aylananing yuzasi: {yuza}")


"""16. Narxlarni solishtirish: 
Foydalanuvchidan ikkita mahsulotning narxini float shaklda kiritishni so‘rang. 
Qaysi mahsulot arzon ekanligini aniqlang."""

# narx1 = float(input("Birinchi mahsulotning narxini kiriting: "))
# narx2 = float(input("Ikkinchi mahsulotning narxini kiriting: "))
#
# narx_qiymati = [
#     "Birinchi mahsulot arzonroq." * (narx1 < narx2),
#     "Ikkinchi mahsulot arzonroq." * (narx1 > narx2),
#     "Ikkala mahsulotning narxi bir xil." * (narx1 == narx2)
# ]
#
# print(narx_qiymati[0] or narx_qiymati[1] or narx_qiymati[2])


"""17. O‘rtacha qiymatni hisoblash: 
Foydalanuvchidan uchta son kiritishni so‘rang va ularning o‘rtacha qiymatini hisoblang."""

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# son3 = float(input("Uchinchi sonni kiriting: "))
#
# ortacha = (son1 + son2 + son3) / 3
#
# print(f"Uchta sonning o‘rtacha qiymati: {ortacha}")


"""18. Sonning kvadrat ildizini topish: 
Foydalanuvchidan musbat son kiritishni so‘rang. Ushbu sonning kvadrat ildizini hisoblang (float turida)."""

# son = float(input("Musbat son kiriting: "))
#
#
# musbat_manfiy = [
#     f"{son} sonining kvadrat ildizi: {son >= 0 and son ** 0.5}"
# ]
#
# # if son >= 0:
# #     kvadrat_ildiz = son ** 0.5
# #     print(f"{son} sonining kvadrat ildizi: {kvadrat_ildiz}")
# # else:
# #     print("Faqat musbat son kiriting.")
#
# print(musbat_manfiy[0] or musbat_manfiy[1])
