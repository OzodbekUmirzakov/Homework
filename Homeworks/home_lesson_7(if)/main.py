"""1. Bola voyaga yetga yoki yetmaganligni tekshiradiga dastur tuzing
      agar voyaga yetga bo'lsa "voyaga yetga" ask holda "voyaga yetmagan"
      so'zini ekranga chiqaring
"""

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh >= 18:
#     print("Voyaga yetgan")
# else:
#     print("Voyaga yetmagan")


"""2.  Talaba olgan bahosini tekshiring dastur tuzing agr talaba 5 baho olgan bo'lsa
 a'lo, agar 4 baho olgan bo'lsa yaxshi, agar 3 baho olgan bo'lsa qoniqarli
 agar 2 baho olgan bo'lsa qoniqarsiz degan so'zlarni ekranga chiqaring
"""

# baho = int(input("Olgan bahongizni kiriting (2-5): "))
#
# if baho == 5:
#     print("A'lo")
# elif baho == 4:
#     print("Yaxshi")
# elif baho == 3:
#     print("Qoniqarli")
# elif baho == 2:
#     print("Qoniqarsiz")
# else:
#     print("Noto'g'ri baho kiritildi")


"""3. Oy raqanimi ekrandan kiritilsa shunga mos fasilni ekranga cjiqaring
 maslana: 12, 1 yoki 2 raqam kiritilsa Qish fasili deb chiqaring
"""

# oy = int(input("Oy raqamini kiriting (1-12): "))
#
# if oy in [12, 1, 2]:
#     print("Qish fasli")
# elif oy in [3, 4, 5]:
#     print("Bahor fasli")
# elif oy in [6, 7, 8]:
#     print("Yoz fasli")
# elif oy in [9, 10, 11]:
#     print("Kuz fasli")
# else:
#     print("Noto'g'ri oy raqami")


"""4. Havoning harorati haqiqiy sonda kiritilsa unga mos holda 30 dan katta bo'lsa
 "havo issiq", agar 30 < 20 > 15 "havo iliq" aks holda 15 dan kichik bolsa "havo sovuq"
 kabi so'zlarni chiqaring
"""

# harorat = float(input("Havoning haroratini kiriting: "))
#
# if harorat > 30:
#     print("Havo issiq")
# elif 20 <= harorat <= 30:
#     print("Havo iliq")
# else:
#     print("Havo sovuq")


"""5. Hujjatning amal qilish muddati kiritiladi butun sonda agar hujjat amal qilish muddati
5 kundan o'tib ketgagn bo'lsa "hujjat amal qilish muddati tugadi" aks holda "hujjat amal qilish muddati tugagan" 
kabi so'zlarni chiqaring
"""

# muddat = int(input("Hujjat amal qilish muddatini kiriting (kunlarda): "))
#
# if muddat > 5:
#     print("Hujjat amal qilish muddati tugadi")
# else:
#     print("Hujjat amal qilish muddati tugagan")


"""6. To'lov usuli matn sharkida kiritiladi naqt yoki kartada agar naqt deb kiritilsa
summa kiritishni so'raydi agar karta deb kiritilsa parol kiriing deb so'rasin
"""

# tolov_usuli = input("To'lov usulini kiriting (naqd/karta): ").lower()
#
# if tolov_usuli == "naqd":
#     summa = float(input("Summani kiriting: "))
#     print("Naqd to'lov uchun summa kiritildi:", summa)
# elif tolov_usuli == "karta":
#     parol = input("Parolni kiriting: ")
#     print("Karta uchun parol kiritildi")
# else:
#     print("Noto'g'ri to'lov usuli")


"""7. Baho baholash: Foydalanuvchidan bahoni so'rang va 90 dan yuqori bo'lsa "A", 80-89 "B", 70-79 "C", 60-69 "D", 
60 dan past bo'lsa "F" deb chiqarish.
"""

# baho = int(input("Bahoni kiriting: "))
#
# if baho >= 90:
#     print("A")
# elif 80 <= baho <= 89:
#     print("B")
# elif 70 <= baho <= 79:
#     print("C")
# elif 60 <= baho <= 69:
#     print("D")
# else:
#     print("F")


"""8. Yoshni tekshirish: Foydalanuvchining yoshini so'rang va agar 18 dan katta bo'lsa "Kattalar", 
aks holda "Bolalar" deb chiqarish.
"""

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh > 18:
#     print("Kattalar")
# else:
#     print("Bolalar")


"""9. Kiyinish qoidalari: Foydalanuvchidan ob-havo haqida so'rab, agar yomg'ir yoki qor bo'lsa, 
"Ko'ylak kiyma" deb chiqarish.
"""

# ob_havo = input("Ob-havo qanday (yomg'ir/qor/quruq): ").lower()
#
# if ob_havo in ["yomg'ir", "qor"]:
#     print("Ko'ylak kiyma")
# else:
#     print("Mos kiyimlarni tanlang")


"""10. To'lov turini tanlash: Foydalanuvchidan to'lov turini (naqd, kartochka) so'rab, har biriga alohida xabar berish.
"""

# tolov_turi = input("To'lov turini kiriting (naqd/kartochka): ").lower()
#
# if tolov_turi == "naqd":
#     print("Siz naqd to'lovni tanladingiz")
# elif tolov_turi == "kartochka":
#     print("Siz kartochka to'lovini tanladingiz")
# else:
#     print("Noto'g'ri to'lov turi")


"""11. Sertifikat olish: Foydalanuvchi 70% dan yuqori baho olsa, "Sertifikat olishingiz mumkin" deb chiqarish."""

# baho = int(input("Bahoni kiriting: "))
#
# if baho > 70:
#     print("Sertifikat olishingiz mumkin")
# else:
#     print("Sertifikat ololmaysiz")


"""12. Yil faslini aniqlash: Foydalanuvchidan oy raqamini so'rang va yil faslini aniqlash (qish, bahor, yoz, kuz)."""

# oy = int(input("Oy raqamini kiriting (1-12): "))
#
# if oy in [12, 1, 2]:
#     print("Qish fasli")
# elif oy in [3, 4, 5]:
#     print("Bahor fasli")
# elif oy in [6, 7, 8]:
#     print("Yoz fasli")
# elif oy in [9, 10, 11]:
#     print("Kuz fasli")
# else:
#     print("Noto'g'ri oy raqami")


"""13. Umumiy o'quv natijasi: Foydalanuvchidan 3 ta bahoni olib, ularning o'rtacha qiymatini hisoblang va "Yaxshi", 
"O'rtacha", "Yomon" deb baholang.
"""

# baho1 = int(input("1-bahoni kiriting: "))
# baho2 = int(input("2-bahoni kiriting: "))
# baho3 = int(input("3-bahoni kiriting: "))
#
# ortalama = (baho1 + baho2 + baho3) / 3
#
# if ortalama >= 70:
#     print("Yaxshi")
# elif 50 <= ortalama < 70:
#     print("O'rtacha")
# else:
#     print("Yomon")


"""14. Qaror qabul qilish: Foydalanuvchiga xohlagan taomni tanlasa, "Tayyorlashga kirishamiz" deb chiqarish."""

# taom = input("Xohlagan taomingizni kiriting: ")
# print("Tayyorlashga kirishamiz")


"""15. Avtomobil yoshi: Foydalanuvchidan avtomobilning yoshi va yurgan masofasini so'rang va 
agar yoshi 10 dan katta bo'lsa, "Ehtiyot qismlarni tekshiring" deb chiqarish.
"""

# yosh = int(input("Avtomobilning yoshini kiriting: "))
# masofa = int(input("Avtomobilning yurgan masofasini kiriting (km): "))
#
# if yosh > 10:
#     print("Ehtiyot qismlarni tekshiring")
# else:
#     print("Avtomobil yaxshi holatda")


"""16. Sovg'a tanlash: Foydalanuvchidan yoshi va jinsi (erkak/ayol) so'ralib, unga mos sovg'a tavsiya etish."""

# yosh = int(input("Yoshingizni kiriting: "))
# jins = input("Jinsingizni kiriting (erkak/ayol): ").lower()
#
# if jins == "erkak":
#     if yosh < 18:
#         print("O'yinchoq avtomobil tavsiya etamiz")
#     else:
#         print("Qo'l soat tavsiya etamiz")
# elif jins == "ayol":
#     if yosh < 18:
#         print("O'yinchoq qo'g'irchoq tavsiya etamiz")
#     else:
#         print("Zargarlik buyumlari tavsiya etamiz")
# else:
#     print("Noto'g'ri jins kiritildi")


"""17. Reyting tizimi: Agar foydalanuvchining balini 100 dan yuqori bo'lsa, "Reytingni yangilang" deb chiqarish."""

# ball = int(input("Balingizni kiriting: "))
#
# if ball > 100:
#     print("Reytingni yangilang")
# else:
#     print("Reyting barqaror")


"""18. Vaqtni tekshirish: Foydalanuvchidan vaqtni so'rang va agar tun bo'lsa "Xayrli tun", 
kunduzi bo'lsa "Xayrli kun" deb chiqarish.
"""

# vaqt = int(input("Soat nechchi bo'lganini kiriting (0-23): "))
#
# if 0 <= vaqt < 6 or 21 <= vaqt <= 23:
#     print("Xayrli tun")
# elif 6 <= vaqt < 21:
#     print("Xayrli kun")
# else:
#     print("Noto'g'ri vaqt kiritildi")


"""19. Parol kuchini tekshirish: Foydalanuvchidan parolni so'rang va agar u 8 ta belgidan kam bo'lsa, 
"Parolni kuchaytiring" deb chiqarish.
"""

# parol = input("Parolni kiriting: ")
#
# if len(parol) < 8:
#     print("Parolni kuchaytiring")
# else:
#     print("Parol kuchli")


"""20. Kredit tayyorgarligi: Foydalanuvchining daromadi va qarzini so'rab, agar daromadi qarzidan yuqori bo'lsa 
"Kredit olish mumkin" deb chiqarish.
"""

# daromad = float(input("Oylik daromadingizni kiriting: "))
# qarz = float(input("Qarzingizni kiriting: "))
#
# if daromad > qarz:
#     print("Kredit olish mumkin")
# else:
#     print("Kredit olish mumkin emas")


"""21. Sport turini tanlash: Foydalanuvchidan yoshini so'rab, unga mos sport turini tavsiya etish."""

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh < 10:
#     print("Bolalar gimnastikasi tavsiya etiladi")
# elif 10 <= yosh < 18:
#     print("Yengil atletika yoki futbol tavsiya etiladi")
# elif 18 <= yosh < 30:
#     print("Jang san'ati yoki suzish tavsiya etiladi")
# else:
#     print("Yoga yoki suzish tavsiya etiladi")


"""22. Sog'liqni tekshirish: Foydalanuvchidan vazn va bo'yini so'rab, BMI ni hisoblang va sog'liq holatini baholang."""

# vazn = float(input("Vazningizni kiriting (kg): "))
# boy = float(input("Bo'yingizni kiriting (m): "))
#
# bmi = vazn / (boy ** 2)
#
# if bmi < 18.5:
#     print("Sizning BMI: ", round(bmi, 2), "- Ozg'inlik")
# elif 18.5 <= bmi < 24.9:
#     print("Sizning BMI: ", round(bmi, 2), "- Normal")
# elif 25 <= bmi < 29.9:
#     print("Sizning BMI: ", round(bmi, 2), "- Ortiqcha vazn")
# else:
#     print("Sizning BMI: ", round(bmi, 2), "- Semizlik")


"""23. Yozgi ta'til rejalari: Foydalanuvchidan yozgi ta'til rejalarini so'rab, agar rejasi bo'lsa 
"Yozda sayohatga chiqamiz" deb chiqarish.
"""

# reja = input("Yozgi ta'til rejalaringiz bormi? (ha/yo'q): ").lower()
#
# if reja == "ha":
#     print("Yozda sayohatga chiqamiz")
# else:
#     print("Yozda uyda qolamiz")


"""24. Bajarilgan ishlar: Foydalanuvchidan bajarilgan ishlar sonini so'rab, agar 5 tadan ko'p bo'lsa 
"Yaxshi natija" deb chiqarish.
"""

# ish_soni = int(input("Bajarilgan ishlar sonini kiriting: "))
#
# if ish_soni > 5:
#     print("Yaxshi natija")
# else:
#     print("Ko'proq harakat qiling")


"""25. Mashhur kitoblar: Foydalanuvchidan kitob nomini so'rab, agar bu kitob mashhur bo'lsa 
"Buni o'qiganman" deb chiqarish.
"""

# kitob = input("O'qigan kitob nomini kiriting: ").lower()
# mashhur_kitoblar = ["alchemist", "harry potter", "to kill a mockingbird", "1984"]
#
# if kitob in mashhur_kitoblar:
#     print("Buni o'qiganman")
# else:
#     print("Bu kitobni hali o'qimaganman")


"""26. Futbol jamoasini tanlash: Foydalanuvchidan sevimli futbol jamoasini so'rab, agar jamoa yutgan bo'lsa 
"Tabriklaymiz!" deb chiqarish.
"""

# jamoa = input("Sevimli futbol jamoangizni kiriting: ").lower()
# yutgan_jamoalar = ["real madrid", "barcelona", "manchester city"]
#
# if jamoa in yutgan_jamoalar:
#     print("Tabriklaymiz!")
# else:
#     print("Yaxshi harakat qilishsin!")


"""27. Savdo muvozanati: Foydalanuvchidan xarajat va daromadni so'rab, agar xarajat daromaddan past bo'lsa 
"Foyda" deb chiqarish.
"""

# xarajat = float(input("Xarajatingizni kiriting: "))
# daromad = float(input("Daromadingizni kiriting: "))
#
# if xarajat < daromad:
#     print("Foyda")
# else:
#     print("Zarar")


"""28. Ish qidirish: Foydalanuvchidan ish tajribasini so'rab, agar 2 yildan kam bo'lsa 
"Yosh mutaxassis" deb chiqarish.
"""

# tajriba = int(input("Ish tajribangizni yillarda kiriting: "))
#
# if tajriba < 2:
#     print("Yosh mutaxassis")
# else:
#     print("Tajriba yetarli")


"""29. Ishni baholash: Foydalanuvchidan ish natijasini so'rab, "Qoniqarli", "Yaxshi", "Mukammal" deb baholash."""

# natija = input("Ish natijasini baholang (qoniqarli/yaxshi/mukammal): ").lower()
#
# if natija == "qoniqarli":
#     print("Ish natijasi qoniqarli")
# elif natija == "yaxshi":
#     print("Ish natijasi yaxshi")
# elif natija == "mukammal":
#     print("Ish natijasi mukammal")
# else:
#     print("Noto'g'ri baho")


"""30. Bojxona qoidalari: Foydalanuvchidan xorijdan olib kelgan mahsulotni so'rab, agar qiymati 100$ dan yuqori bo'lsa, 
"Boj to'lashingiz kerak" deb chiqarish."""

# qiymat = float(input("Olib kelgan mahsulot qiymatini kiriting ($): "))
#
# if qiymat > 100:
#     print("Boj to'lashingiz kerak")
# else:
#     print("Boj to'lashingiz shart emas")


"""31. Uchuvchi talablari: Foydalanuvchidan uchish uchun yoshi va vaznini so'rab, agar talablarga mos kelmasa 
"Uchish mumkin emas" deb chiqarish.
"""

# yosh = int(input("Yoshingizni kiriting: "))
# vazn = float(input("Vazningizni kiriting (kg): "))
#
# if yosh < 18 or vazn < 50 or vazn > 100:
#     print("Uchish mumkin emas")
# else:
#     print("Uchish mumkin")


"""32. Iqlim sharoiti: Foydalanuvchidan haroratni so'rab, agar 0 dan past bo'lsa "Qishda qizish" deb chiqarish."""

# harorat = float(input("Haroratni kiriting (°C): "))
#
# if harorat < 0:
#     print("Qishda qizish")
# else:
#     print("Ob-havo mos")


"""33. Maktabga tayyorgarlik: Foydalanuvchidan maktabga kirishi uchun tayyorgarlik darajasini so'rab, 
agar yetarli bo'lmasa "Ko'proq o'qish kerak" deb chiqarish.
"""

# tayyorgarlik = input("Maktabga tayyorgarlik darajangizni kiriting (yaxshi/etarli/emayotgan): ").lower()
#
# if tayyorgarlik != "yaxshi":
#     print("Ko'proq o'qish kerak")
# else:
#     print("Tayyorgarlik yetarli")


"""34. Savdo so'rovlarini tekshirish: Foydalanuvchidan so'rovlarni so'rab, agar talab yuqori bo'lsa 
"Savdo muvaffaqiyatli" deb chiqarish.
"""

# talab = input("Savdo so'rovlarini kiriting (yuqori/past): ").lower()
#
# if talab == "yuqori":
#     print("Savdo muvaffaqiyatli")
# else:
#     print("Savdo sust")


"""35. Dars tayyorgarligi: Foydalanuvchidan dars tayyorgarligi darajasini so'rab, agar yetarli bo'lmasa 
"Boshqa darslar oling" deb chiqarish.
"""

# tayyorgarlik = input("Dars tayyorgarligingizni kiriting (yaxshi/etarli/emayotgan): ").lower()
#
# if tayyorgarlik != "yaxshi":
#     print("Boshqa darslar oling")
# else:
#     print("Dars tayyorgarligi yetarli")


"""36. Dostlar ro'yxati: Foydalanuvchidan dostlar sonini so'rab, agar 5 tadan kam bo'lsa 
"Dostlar orttirishingiz mumkin" deb chiqarish.
"""

# dostlar_soni = int(input("Do'stlaringiz sonini kiriting: "))
#
# if dostlar_soni < 5:
#     print("Do'stlar orttirishingiz mumkin")
# else:
#     print("Yetarli do'stlaringiz bor")


"""37. Musbat yoki Manfiy Son: Foydalanuvchi kiritgan son musbat yoki manfiy ekanligini aniqlang. 
Agar nol kiritilsa, “Bu nol” deb yozing.
"""

# son = float(input("Son kiriting: "))
#
# if son > 0:
#     print("Bu musbat son")
# elif son < 0:
#     print("Bu manfiy son")
# else:
#     print("Bu nol")


"""38. Juft yoki Toq Son: Foydalanuvchidan son kiritishni so'rang va bu son juft yoki toq ekanligini aniqlang."""

# son = int(input("Son kiriting: "))
#
# if son % 2 == 0:
#     print("Bu juft son")
# else:
#     print("Bu toq son")


"""39. Yoshni Guruhlash: Foydalanuvchidan yoshini so'rang va u 0-12 yosh bolalar, 
13-19 yoshlar va 20 dan katta kattalar guruhiga kirishini aniqlang.
"""

# yosh = int(input("Yoshingizni kiriting: "))
#
# if 0 <= yosh <= 12:
#     print("Siz bolalar guruhidasiz")
# elif 13 <= yosh <= 19:
#     print("Siz o'smirlar guruhidasiz")
# elif yosh >= 20:
#     print("Siz kattalar guruhidasiz")
# else:
#     print("Noto'g'ri yosh")


"""40. Bahoni Tekshirish: Foydalanuvchidan bahoni so'rang va bahoni A, B, C, D yoki F ga to'g'ri kelishini aniqlang."""

# baho = int(input("Bahoni kiriting: "))
#
# if 90 <= baho <= 100:
#     print("Sizning baho: A")
# elif 80 <= baho < 90:
#     print("Sizning baho: B")
# elif 70 <= baho < 80:
#     print("Sizning baho: C")
# elif 60 <= baho < 70:
#     print("Sizning baho: D")
# else:
#     print("Sizning baho: F")


"""41. Mavsumni Aniqlash: Foydalanuvchidan oy raqamini so'rang va bu oy qishda, bahorda, yozda yoki 
kuzda ekanligini aniqlang.
"""

# oy = int(input("Oy raqamini kiriting (1-12): "))
#
# if oy in [12, 1, 2]:
#     print("Qish fasli")
# elif oy in [3, 4, 5]:
#     print("Bahor fasli")
# elif oy in [6, 7, 8]:
#     print("Yoz fasli")
# elif oy in [9, 10, 11]:
#     print("Kuz fasli")
# else:
#     print("Noto'g'ri oy raqami")


"""42. Ikki Sonni Taqqoslash: Foydalanuvchidan ikkita sonni so'rang va ularni qaysi biri katta, kichik yoki 
tengligini aniqlang.
"""

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# if son1 > son2:
#     print("Birinchi son kattaroq")
# elif son1 < son2:
#     print("Ikkinchi son kattaroq")
# else:
#     print("Ikkala son teng")


"""43. Parolni Tekshirish: Foydalanuvchidan parolni so'rang va parol to'g'ri yoki noto'g'ri ekanligini aniqlang."""

# togri_parol = "12345"
# parol = input("Parolni kiriting: ")
#
# if parol == togri_parol:
#     print("Parol to'g'ri")
# else:
#     print("Parol noto'g'ri")


"""44. Harfning Turini Aniqlash: Foydalanuvchidan bir harfni so'rang va bu katta yoki kichik harf ekanligini aniqlang.
"""

# harf = input("Harf kiriting: ")
#
# if harf.isupper():
#     print("Bu katta harf")
# elif harf.islower():
#     print("Bu kichik harf")
# else:
#     print("Bu harf emas yoki noto'g'ri kiritildi")


"""45. Havo Haroratini Aniqlash: Foydalanuvchidan havo haroratini so'rang va u juda issiq, iliq, sovuq yoki 
juda sovuq ekanligini aniqlang.
"""

# harorat = float(input("Havo haroratini kiriting: "))
#
# if harorat > 35:
#     print("Juda issiq")
# elif 20 <= harorat <= 35:
#     print("Iliq")
# elif 0 <= harorat < 20:
#     print("Sovuq")
# else:
#     print("Juda sovuq")


"""46. Mamlakatni Aniqlash: Foydalanuvchidan mamlakatini so'rang va agar u O'zbekiston bo'lsa, 
“Siz O'zbekistondasiz” deb yozing.
"""

# mamlakat = input("Mamlakatingizni kiriting: ").lower()
#
# if mamlakat == "o'zbekiston":
#     print("Siz O'zbekistondasiz")
# else:
#     print("Siz boshqa mamlakatdasiz")


"""47. Balandlikni Aniqlash: Foydalanuvchidan balandligini so'rang va u qisqa, o'rtacha yoki baland ekanligini aniqlang.
"""

# balandlik = float(input("Balandlikni kiriting (sm): "))
#
# if balandlik < 150:
#     print("Qisqa")
# elif 150 <= balandlik <= 180:
#     print("O'rtacha")
# else:
#     print("Baland")


"""48. Kitob Narxini Tekshirish: Foydalanuvchidan kitob narxini so'rang va narxni arzon, o'rtacha yoki 
qimmat ekanligini aniqlang.
"""

# narx = float(input("Kitob narxini kiriting: "))
#
# if narx < 50:
#     print("Arzon")
# elif 50 <= narx <= 150:
#     print("O'rtacha")
# else:
#     print("Qimmat")


"""49. Sport Darajasini Aniqlash: Foydalanuvchidan sport darajasini so'rang va u yangi, o'rta yoki 
tajribali sportchi ekanligini aniqlang.
"""

# daraja = input("Sport darajangizni kiriting (yangi/o'rta/tajribali): ").lower()
#
# if daraja == "yangi":
#     print("Yangi sportchi")
# elif daraja == "o'rta":
#     print("O'rta darajali sportchi")
# elif daraja == "tajribali":
#     print("Tajribali sportchi")
# else:
#     print("Noto'g'ri daraja")


"""50. Sog'liqni Tekshirish: Foydalanuvchidan belgilari haqida ma'lumot oling va 
sog'liq holatini aniqlang (masalan, isitma, yo'tal).
"""

# isitma = input("Isitma bormi? (ha/yo'q): ").lower()
# yotal = input("Yo'tal bormi? (ha/yo'q): ").lower()
#
# if isitma == "ha" or yotal == "ha":
#     print("Sog'liqni tekshirish kerak")
# else:
#     print("Sog'liq holati yaxshi")


"""51. Kreditni Tasdiqlash: Foydalanuvchidan kredit balini so'rang va u kredit olish uchun mos kelishini aniqlang."""

# bal = int(input("Kredit balingizni kiriting: "))
#
# if bal >= 700:
#     print("Kredit olish uchun mos")
# else:
#     print("Kredit olish uchun mos emas")


"""52. Kafedagi Buyurtma: Foydalanuvchidan kafeda buyurtma (kofe, choy, sharbat) so'rang va 
buyurtma tayyorlanishini xabar bering.
"""

# buyurtma = input("Kafedagi buyurtmani kiriting (kofe/choy/sharbat): ").lower()
#
# if buyurtma in ["kofe", "choy", "sharbat"]:
#     print(f"{buyurtma.capitalize()} tayyorlanmoqda")
# else:
#     print("Bunday buyurtma mavjud emas")


"""53. Tezlikni Aniqlash: Foydalanuvchidan avtomobil tezligini so'rang va u tezlikni oshirdimi yoki 
normal ekanligini aniqlang.
"""

# tezlik = int(input("Avtomobil tezligini kiriting (km/soat): "))
#
# if tezlik > 60:
#     print("Tezlik oshirildi")
# else:
#     print("Tezlik normal")


"""54. Tatilni Aniqlash: Foydalanuvchidan ta'til vaqtini so'rang va yoz yoki qish ta'tili ekanligini aniqlang."""

# tatil_oy = int(input("Ta'til oy raqamini kiriting (1-12): "))
#
# if tatil_oy in [6, 7, 8]:
#     print("Yozgi ta'til")
# elif tatil_oy in [12, 1, 2]:
#     print("Qishki ta'til")
# else:
#     print("Bu ta'til vaqti emas")


"""55. Maktab Bahosi: Foydalanuvchidan maktab bahosini so'rang va u yuqori, o'rtacha yoki 
past baho ekanligini aniqlang.
"""

# baho = int(input("Maktab bahosini kiriting: "))
#
# if baho >= 4:
#     print("Yuqori baho")
# elif baho == 3:
#     print("O'rtacha baho")
# else:
#     print("Past baho")


"""56. Raqamni Aniqlash: Foydalanuvchidan raqam kiritishni so'rang va kiritilgan qiymat raqam ekanligini aniqlang."""

# raqam = input("Raqam kiriting: ")
#
# if raqam.isdigit():
#     print("Bu raqam")
# else:
#     print("Bu raqam emas")
