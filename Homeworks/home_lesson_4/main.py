"""Task 1: Tuple yaratish va elementlarga murojaat qilish
    1. Quyidagi tuple'ni yarating: fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi').
    2. Tuple'dagi birinchi va oxirgi elementlarni chiqaring.
    3. Tuple'dagi uchinchi elementni toping.
"""

# fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')
#
# print(f"Birinchi element: {fruits[0]}")
# print(f"Oxirgi element: {fruits[-1]}")
# print(f"Uchinchi element: {fruits[2]}")


"""Task 2: Tuple elementlarini hisoblash
    1. Quyidagi tuple'ni yarating: numbers = (1, 2, 3, 4, 2, 5, 6, 2).
    2. Tuple'da nechta 2 borligini toping.
    3. Tuple'dagi 5 qaysi indeksda ekanini aniqlang.
"""

# numbers = (1, 2, 3, 4, 2, 5, 6, 2)
#
# count_of_twos = numbers.count(2)
# print(f"Nechta 2 bor: {count_of_twos}")
#
# index_of_five = numbers.index(5)
# print(f"5 ning indeksi: {index_of_five}")


"""Task 3: Tuple'dan ro'yxatga aylantirish
    1. Quyidagi tuple'ni yarating: colors = ('red', 'green', 'blue').
    2. Uni ro'yxatga aylantiring va unga yangi element qo'shing: 'yellow'.
    3. Ro'yxatni qaytadan tuple'ga o'zgartiring.
"""

# colors = ('red', 'green', 'blue')
#
# colors_list = list(colors)
# colors_list.append('yellow')
#
# print(f"Yangi ro'yxat: {colors_list}")
#
# colors = tuple(colors_list)
#
# print(f"Yangi tuple: {colors}")


"""Task 4: Tuple'ni teskari qilish
    1. Quyidagi tuple'ni yarating: letters = ('a', 'b', 'c', 'd', 'e').
    2. Tuple'dagi elementlarni teskari qilib chiqaring.
"""

# letters = ('a', 'b', 'c', 'd', 'e')
#
# reversed_letters = letters[::-1]
#
# print(f"Teskari tuple: {reversed_letters}")


"""Task 5: Tuple ichidagi tuple
    1. Quyidagi tuple'ni yarating: nested_tuple = (1, 2, (3, 4, 5), 6, 7).
    2. Ichkaridagi tuple'dagi ikkinchi elementni chiqaring.
    3. Tuple'dagi barcha elementlarni chiqaradigan sikl yozing.
"""

# nested_tuple = (1, 2, (3, 4, 5), 6, 7)
#
# second_element = nested_tuple[2][1]
#
# print(f"Ichkaridagi tuple'dagi ikkinchi element: {second_element}")
#
# print(nested_tuple[0])
# print(nested_tuple[1])
# print(nested_tuple[2])
# print(nested_tuple[3])
# print(nested_tuple[4])
# print(nested_tuple[2][0])
# print(nested_tuple[2][1])
# print(nested_tuple[2][2])


"""Task 6: Tuple va ro'yxat bilan ishlash
    1. Quyidagi tuple'ni yarating: my_tuple = (10, 20, 30, 40, 50).
    2. Tuple'ni ro'yxatga o'zgartiring va 60 raqamini qo'shing.
    3. Ro'yxatni yana tuple'ga o'zgartiring va natijani ekranga chiqaring.
"""

# my_tuple = (10, 20, 30, 40, 50)
#
# my_list = list(my_tuple)
# my_list.append(60)
# my_tuple = tuple(my_list)
#
# print(f"Yangi tuple: {my_tuple}")


"""Task 7: Tuple birlashtirish
    1. Ikkita tuple yarating: tuple1 = (1, 2, 3) va tuple2 = (4, 5, 6).
    2. Ikkala tuple'ni birlashtirib yangi tuple hosil qiling.
"""

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
#
# new_tuple = tuple1 + tuple2
#
# print(f"Birlashtirilgan tuple: {new_tuple}")


"""Task 1: List yaratish va elementlar bilan ishlash
    1. Quyidagi listni yarating: numbers = [10, 20, 30, 40, 50].
    2. Listdagi birinchi elementni 100 ga o'zgartiring.
    3. Listning oxiriga 60 ni qo'shing.
    4. Listning uzunligini aniqlang va ekranga chiqaring.
"""

# numbers = [10, 20, 30, 40, 50]
#
# numbers[0] = 100
# numbers.append(60)
# length = len(numbers)
#
# print(length)


"""Task 2: Listdagi elementlarni qo'shish va tahrirlash
    1. Quyidagi listni yarating: fruits = ['apple', 'banana', 'cherry'].
    2. Listga orange va kiwi mevalarini qo'shing.
    3. banana ni mango ga o'zgartiring.
    4. Listdagi barcha mevalarni alfabetik tartibda joylang.
"""

# fruits = ['apple', 'banana', 'cherry']
#
# fruits.extend(['orange', 'kiwi'])
# fruits[1] = 'mango'
# fruits.sort()
#
# print(fruits)


"""Task 3: Listning indekslari bilan ishlash
    1. Quyidagi listni yarating: students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina'].
    2. Zarina qaysi indeksda ekanini toping.
    3. Listdagi birinchi va oxirgi elementlarni chiqaring.
"""

# students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina']
#
# index_zarina = students.index('Zarina')
# first_student = students[0]
# last_student = students[-1]
#
# print(f"Zarina {index_zarina}-indeksda \n", first_student, last_student)


"""Task 4: Tuple yaratish va tahlil qilish
    1. Quyidagi tuple'ni yarating: my_tuple = (5, 10, 15, 20, 25).
    2. Tuple'dagi uchinchi elementni chiqaring.
    3. Tuple'da nechta element borligini aniqlang.
"""

# my_tuple = (5, 10, 15, 20, 25)
#
# third_element = my_tuple[2]
# tuple_length = len(my_tuple)
#
# print(third_element)
# print(tuple_length)


"""Task 5: Tuple va list orasidagi farqlar
    1. Quyidagi tuple va listni yarating:
    my_tuple = (1, 2, 3)
    my_list = [1, 2, 3]
    2. Listga 4 raqamini qo'shing, lekin tuple'ga qo'shib bo'lmasligini tushuntiring.
    3. List va tuple o'rtasidagi asosiy farqlarni tushuntirib bering.
"""

# my_tuple = (1, 2, 3)
# my_list = [1, 2, 3]
#
# my_list.append(4)
#
# print(my_list)


"""Task 6: List va tuple orasida konvertatsiya qilish
    1. Quyidagi tuple'ni yarating: colors = ('red', 'green', 'blue').
    2. Tuple'ni ro'yxatga o'zgartiring va unga yangi rang yellow ni qo'shing.
    3. Ro'yxatni yana tuple'ga o'zgartiring va natijani chiqaring.
"""

# colors = ('red', 'green', 'blue')
#
# colors_list = list(colors)
# colors_list.append('yellow')
# new_colors_tuple = tuple(colors_list)
#
# print(new_colors_tuple)


"""Task 7: Elementlarni qo'shish va teskari qilish
    1. Quyidagi listni yarating: numbers = [5, 10, 15, 20, 25].
    2. Listga 30 raqamini qo'shing va listdagi elementlarni teskari tartibda joylang.
    3. Shuningdek, tuple yaratib, uni ham teskari qilib chiqaring: my_tuple = (10, 20, 30, 40).
"""

# numbers = [5, 10, 15, 20, 25]
#
# numbers.append(30)
# numbers.reverse()
# my_tuple = (10, 20, 30, 40)
# reversed_tuple = my_tuple[::-1]
#
# print(numbers)
# print(reversed_tuple)


"""Task 8: List va tupledagi umumiy amal
    1. Quyidagi tuple va listni yarating:
    num_list = [10, 20, 30, 40]
    num_tuple = (50, 60, 70, 80)
    2. Ikkisini birlashtirib yangi ro'yxat yarating.
    3.Yaratilgan ro'yxatdan eng katta va eng kichik qiymatni toping.
"""

# num_list = [10, 20, 30, 40]
# num_tuple = (50, 60, 70, 80)
#
# combined_list = num_list + list(num_tuple)
# max_value = max(combined_list)
# min_value = min(combined_list)
#
# print(max_value, min_value)


"""Task 9: Tuple ichida tuple bilan ishlash
    1. Quyidagi tuple'ni yarating: nested_tuple = (1, 2, (3, 4, 5), 6, 7).
    2. Ichkaridagi tuple'dagi elementlarni ekranga chiqaring.
    3. Tuple'dagi barcha elementlarni sikl orqali chiqarib bering.
"""

# nested_tuple = (1, 2, (3, 4, 5), 6, 7)
#
# print(nested_tuple[2])


"""Task 10: Listdagi sonlarni ko'paytirish
    1. Quyidagi listni yarating: numbers = [2, 4, 6, 8, 10].
    2. Har bir elementni 2 ga ko'paytiring va yangi ro'yxat hosil qiling.
"""

# numbers = [2, 4, 6, 8, 10]
#
# multiplied_numbers = [numbers[0] * 2, numbers[1] * 2, numbers[2] * 2, numbers[3] * 2, numbers[4] * 2]
#
# print(multiplied_numbers)


"""Task 11: Listdan elementni olib tashlash
    1. Quyidagi listni yarating: my_list = ['apple', 'banana', 'cherry', 'date', 'fig'].
    2. Listdan cherry ni olib tashlang.
    3. Listdan oxirgi elementni olib tashlang va natijani chiqaring.
"""

# my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
#
# my_list.remove('cherry')
# my_list.pop()
#
# print(my_list)


"""Task 12: Listda elementlarni tartiblash
    1. Quyidagi listni yarating: ages = [34, 23, 45, 27, 56, 18].
    2. Listdagi elementlarni o'sish tartibida joylang.
    3. Keyin, listdagi elementlarni kamayish tartibida joylang.
"""

# ages = [34, 23, 45, 27, 56, 18]
#
# ages.sort()
# print(ages)
#
# ages.sort(reverse=True)
# print(ages)


"""Task 13: Listdagi takroriy elementlarni olib tashlash
    1. Quyidagi listni yarating: numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7].
    2. Listdagi takroriy elementlarni olib tashlang va yangi list yarating.
    3. Yangi listni ekranga chiqaring.
"""

# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
#
# unique_numbers = list(set(numbers))
#
# print(unique_numbers)


"""Task 14: Tuple'dagi eng katta va eng kichik qiymatlarni topish
    1. Quyidagi tuple'ni yarating: numbers = (10, 50, 25, 5, 100, 75).
    2. Tuple'dagi eng katta va eng kichik qiymatlarni toping.
"""

# numbers = (10, 50, 25, 5, 100, 75)
#
# max_value = max(numbers)
# min_value = min(numbers)
#
# print(f"Eng katta: {max_value}, Eng kichik: {min_value}")


"""Task 15: List elementlarini juftliklarga bo'lish
    1. Quyidagi listni yarating: my_list = [10, 20, 30, 40, 50, 60].
    2. Listdagi elementlarni har ikkitadan juftlik qilib chiqaradigan kod yozing. Natija quyidagicha bo'lishi kerak: 
    [(10, 20), (30, 40), (50, 60)].
"""

# my_list = [10, 20, 30, 40, 50, 60]
#
# pairs = [(my_list[0], my_list[1]), (my_list[2], my_list[3]), (my_list[4], my_list[5])]
#
# print(pairs)


"""Task 16: Tuple'ni slicing (kesish) orqali ishlatish
    Quyidagi tuple'ni yarating: alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g').
    Tuple'dan faqat birinchi uchta elementni kesib oling va yangi tuple yarating.
    Oxirgi uchta elementni kesib oling va chiqaring.
"""

# alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
#
# first_three = alphabet[:3]
# print(first_three)
#
# last_three = alphabet[-3:]
# print(last_three)


"""Task 17: Listni for sikli orqali chiqarish
    1. Quyidagi listni yarating: names = ['Ali', 'Olim', 'Zarina', 'Jasur'].
    2. for sikli yordamida har bir ismdan keyin " - talaba" so'zini qo'shib chiqaring. Masalan: Ali - talaba.
"""

# names = ['Ali', 'Olim', 'Zarina', 'Jasur']
#
# ali_output = names[0] + " - talaba"
# olimp_output = names[1] + " - talaba"
# zarina_output = names[2] + " - talaba"
# jasur_output = names[3] + " - talaba"
#
# print(ali_output)
# print(olimp_output)
# print(zarina_output)
# print(jasur_output)


"""Task 18: Tuple'ni for sikli orqali chiqarish
    1. Quyidagi tuple'ni yarating: temperatures = (22, 25, 28, 30, 27, 23).
    2. Tuple'dagi har bir harorat qiymatini ekranga chiqaring.
"""

# temperatures = (22, 25, 28, 30, 27, 23)
#
# temp1 = temperatures[0]
# temp2 = temperatures[1]
# temp3 = temperatures[2]
# temp4 = temperatures[3]
# temp5 = temperatures[4]
# temp6 = temperatures[5]
#
# print(temp1)
# print(temp2)
# print(temp3)
# print(temp4)
# print(temp5)
# print(temp6)


"""Task 19: Listdagi sonlarni topib yig'ish
    1. Quyidagi listni yarating: my_list = [1, 5, 'banana', 10, 'apple', 20].
    2. Faqat raqamlar yig'indisini toping va natijani chiqaring.
"""

# my_list = [1, 5, 'banana', 10, 'apple', 20]
#
# total = 0
# total += my_list[0]  # 1
# total += my_list[1]  # 5
# total += my_list[3]  # 10
# total += my_list[5]  # 20
#
# print(total)  # Natija: 36


"""Task 20: Tuple va listda elementlarni almashtirish
    1. Quyidagi listni yarating: my_list = [10, 20, 30].
    2. Quyidagi tuple'ni yarating: my_tuple = (40, 50, 60).
    3. Birinchi elementlarini almashtiring. Yani my_list[0] va my_tuple[0] qiymatlarini bir-biriga almashtiring 
    va natijani chiqaring.
"""

# my_list = [10, 20, 30]
# my_tuple = (40, 50, 60)
#
# temp = my_list[0]  # 10
# my_list[0] = my_tuple[0]  # my_list[0] ga 40 ni qo'shamiz
# my_tuple = (temp,) + my_tuple[1:]  # (10, 50, 60) ga aylantiramiz
#
# print(my_list)  # Natija: [40, 20, 30]
# print(my_tuple)  # Natija: (10, 50, 60)







