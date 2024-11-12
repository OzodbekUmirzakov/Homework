"""1. List berilgan listning ichida biz qidirgan element bor yoki yoqligni tekshirirng bor bo'lsa True aks
      holda False chiqaring
"""

# lst = [1, 2, 3, 4, 5]
# element = 3
# i = 0
# found = False
#
# while i < len(lst):
#     if lst[i] == element:
#         found = True
#     i += 1
#
# print(found)


"""2. Barcha 3 - xonali sonlar ichida raqamlari yi'gindisi 5 dan katta va 8 dan kichik bo'lganlarini ekranga chiqaring
"""

# num = 100
#
# while num < 1000:
#     yuzlar = num // 100
#     onlar = (num // 10) % 10
#     birliklar = num % 10
#
#     sum_digits = yuzlar + onlar + birliklar
#
#     if 5 < sum_digits < 8:
#         print(num)
#
#     num += 1


"""3. Ekrandan son kiritilsa shu son necha xonali ekangini aniqlang"""

# num = int(input("Son kiriting: "))
# count = 0
#
# if num == 0:
#     count = 1
# else:
#     if num < 0:
#         num = -num
#     while num != 0:
#         num //= 10
#         count += 1
#
# print("Xonalar soni:", count)


"""4. Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni yig'indisini chiqaring"""

# n = int(input("Nechta son kiritasiz? = "))
# i = 0
# total = 0
#
# while i < n:
#     num = int(input(f"{i + 1} - Sonni kiriting: "))
#     total += num
#     i += 1
#
# print(f"Yig'indisi: {total}")


"""5. Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shu sonlarni kattasini chiqaring"""

# n = int(input("Nechta son kiritasiz? = "))
# i = 0
# max_num = None
#
# while i < n:
#     num = int(input("Sonni kiriting: "))
#     if max_num is None or num > max_num:
#         max_num = num
#     i += 1
#
# print("Eng katta son:", max_num)


"""6. Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni kichigini chiqaring"""

# n = int(input("Nechta son kiritasiz? = "))
# i = 0
# min_num = None
#
# while i < n:
#     num = int(input("Sonni kiriting: "))
#     if min_num is None or num < min_num:
#         min_num = num
#     i += 1
#
# print("Eng kichik son:", min_num)


"""7. List yarating hosil bolgan listning har bir elementiga 2 ni ko'paytirib ekranga chiqaring"""

# lst = [000, 0, 1, -2, 3, 4, 5]
# i = 0
#
# while i < len(lst):
#     print(lst[i] * 2)
#     i += 1


"""8. Mukammal son yoki Mukammal son emasligini tekshiring mukammal sonlar o'zidan tashqari bo'luvchilarini 
      yig'indisi o'ziga teng
      Masalan : 28 -> 1,2,4,7,14 shu sonlarning yigindisi 28 ga teng
"""

# num = int(input("Son kiriting: "))
# i = 1
# sum_divisors = 0
#
# while i < num:
#     if num % i == 0:
#         sum_divisors += i
#     i += 1
#
# if sum_divisors == num:
#     print("Mukammal son")
# else:
#     print("Mukammal son emas")


"""9. Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa darajasi aks holda darajasi emas kabi so'zlarni chiqaring"""

# num = int(input("Son kiriting: "))
# power_of_2 = 1
#
# while power_of_2 < num:
#     power_of_2 *= 2
#
# if power_of_2 == num:
#     print("2 ning darajasi")
# else:
#     print("2 ning darajasi emas")


"""10. Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa nechanchi darajasi ekanligini aks holda darajasi 
emas kabi so'zlarni chiqaring
"""

# num = int(input("Son kiriting: "))
# power_of_2 = 1
# degree = 0
#
# while power_of_2 < num:
#     power_of_2 *= 2
#     degree += 1
#
# if power_of_2 == num:
#     print(f"2 ning {degree}-darajasi")
# else:
#     print("2 ning darajasi emas")


"""11. Ekrandan son kiritiladi shu sonning faktorialini chiqaring"""

# num = int(input("Son kiriting: "))
# factorial = 1
# i = 1
#
# while i <= num:
#     factorial *= i
#     i += 1
#
# print("Faktorial:", factorial)


"""12. List berilgan x = [1,23,10,45,-41,56,78,13] shu listning juft va toq elementlarini 2 ta alohida listga yuklang
       juft = [10,56, 78]
       toq = [1,23,45,-41,13]
"""

# x = [1, 23, 10, 45, -41, 56, 78, 13]
# juft = []
# toq = []
# i = 0
#
# while i < len(x):
#     if x[i] % 2 == 0:
#         juft.append(x[i])
#     else:
#         toq.append(x[i])
#     i += 1
#
# print("Juft:", juft)
# print("Toq:", toq)


"""13. Ekrandan biror son kiritilsa shunga mos holda karra jadvalini chiqaring
       son = 5
       5 x 1 = 5
       5 x 2 = 10
       5 x 3 = 15
       ..........
"""

# num = int(input("Son kiriting: "))
# i = 1
#
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


"""14. List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] 
       berilgan list elementlari ichidan eng uzun so'zni toping va uni ekranga chiqaring
"""

# cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
# i = 0
# longest_word = ""
#
# while i < len(cars):
#     if len(cars[i]) > len(longest_word):
#         longest_word = cars[i]
#     i += 1
#
# print(f"Eng uzun so'z: {longest_word}")


"""15. List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] 
       berilgan list elementlari ichidan a harfi bilan tugaydiganlarni ekranga chiqaring
       Masalan : Tayota, Mazda, Lada
"""

# cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
# i = 0
#
# while i < len(cars):
#     if cars[i][-1] == "a":  # cars[i].endswith("a"):
#         print(cars[i])
#     i += 1
