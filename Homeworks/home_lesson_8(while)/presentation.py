"""1. Foydalanuvchidan raqam so'rang va uni yig'indiga qo'shib boring. 0 kiritilganda, yig'indini chiqarin."""

# yigindi = 0
# while True:
#     son = int(input("Raqam kiriting (0 kiritganda to'xtaydi): "))
#     if son == 0:
#         break
#     elif son > 0:
#         yigindi += son
#
# print("Yig'indi:", yigindi)


"""2. A dan B gacha bo’lgan sonlarni yig’indisini ekranga chiqaring."""

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# yigindi = 0
# i = A
# while i <= B:
#     yigindi += i
#     i += 1
#
# print(f"{A} dan {B} gacha bo'lgan sonlarning yig'indisi:", yigindi)


"""3. Foydalanuvchi ekrandan bir nechta raqamlarni ketma – ket kiritadi va ularni listga qo’shing 
va listni ekranga chiqaring."""

# raqamlar = []
# raqam = int(input("Raqam kiriting (to'xtash uchun 0 ni kiriting): "))
#
# while raqam != 0:
#     raqamlar.append(raqam)
#     raqam = int(input("Raqam kiriting (to'xtash uchun 0 ni kiriting): "))
#
# print("Kiritilgan raqamlar ro'yxati:", raqamlar)


"""4. x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan listning eng katta elementini toping."""
"""5. x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan listning eng katta elementi nechanchi indexda ekanligini chiqaring."""

# x = [1, 2, 3, 14, 5, 6, 6, 7]
# max_element = x[0]
# index = 0
#
# i = 1
# while i < len(x):
#     if x[i] > max_element:
#         max_element = x[i]
#         index = i
#     i += 1
#
# print("Berilgan listning eng katta elementi:", max_element)
# print("Berilgan listning eng katta elementi", max_element, "indexda:", index)


"""6. Ekrandan kiritilgan biror sonning necha xonali ekanligini aniqlang."""

# son = int(input("Biror son kiriting: "))
#
# xonalar = 0
# temp = son
#
# if temp < 0:
#     temp *= -1
#
# while temp != 0:
#     temp //= 10
#     xonalar += 1
#
# print(f"Kiritilhan son {son}, ning xonalar soni: {xonalar}")


"""7. x = [1, 2, 0, 14, 5, -6] berilgan list ning katta elemanti va kichik elementini toping """

# x = [1, 2, 0, 14, 5, -6]
#
# max_element = x[0]
# min_element = x[0]
# i = 1
# while i < len(x):
#     if x[i] > max_element:
#         max_element = x[i]
#     if x[i] < min_element:
#         min_element = x[i]
#     i += 1
# print("Berilgan listning eng katta elementi:", max_element)
# print("Berilgan listning eng kichik elementi:", min_element)


"""8. x = [-2, 31, 104, 51, 19, 7] berilgan listning katta elementini va kichik elementlarini o’rnini almashting 
va hosil bo'lgan listni ekranga chiqaring."""

# x = [-2, 31, 104, 51, 19, 7]
#
# max_index = 0
# min_index = 0
# i = 1
# while i < len(x):
#     if x[i] > x[max_index]:
#         max_index = i
#     if x[i] < x[min_index]:
#         min_index = i
#     i += 1
#
# # O'rin almashtirish
# x[max_index], x[min_index] = x[min_index], x[max_index]
# print("Katta va kichik elementlar o'rni almashtirilgan list:", x)


"""9. List yaratiladi va ekrandan son kiritiladi, kiritilgan son listning ichida bor bo’lsa "Element bor" aks holda 
"Element yo’q" kabi so’zlarni chiqaring."""

# raqamlar = [5, 10, 15, 20, 25]
# son = int(input("Qidiriladigan sonni kiriting: "))
#
# i = 0
# element_bor = False
# while i < len(raqamlar):
#     if raqamlar[i] == son:
#         element_bor = True
#         break
#     i += 1
#
# if element_bor:
#     print("Element bor")
# else:
#     print("Element yo'q")


"""10. While operatoridan foydalanib berilgan A va B sonlarning EKUBini chiqaring."""

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# a, b = A, B
#
# while b != 0:
#     a, b = b, a % b
#
# print(f"{A} va {B} sonlarining EKUBi:", a)

"""11. While operatoridan foydalanib berilgan A va B sonlarning EKUKini chiqaring."""

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# a, b = A, B
#
# while b != 0:
#     a, b = b, a % b
# ekub = a
# ekuk = (A * B) // ekub
#
# print(f"{A} va {B} sonlarining EKUKi:", ekuk)


# ////////////////////////////////////////////////////////////////////////////////////////
# def check_sequence(lst):
#     peak_found = False
#     valley_found = False
#
#     for i in range(1, len(lst) - 1):
#         if lst[i - 1] < lst[i] > lst[i + 1]:
#             if peak_found or valley_found:
#                 return False
#             peak_found = True
#         elif lst[i - 1] > lst[i] < lst[i + 1]:
#             if peak_found or valley_found:
#                 return False
#             valley_found = True
#
#     if peak_found:
#         return True
#     elif valley_found:
#         return False
#     elif all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
#         return True
#     else:
#         return False
#
#
# my_list = [4, 3, 3, 2, 2, 1]
# my_list2 = [2, 4, 50, 49, 61]
# my_list3 = [90, 89, 31, 12]
# my_list4 = [12, 14, 50, 61, 17]
# my_list5 = [-100, 60, 9, 2, 1, 67, 78, 89]
#
# print(check_sequence(my_list))
# print(check_sequence(my_list2))
# print(check_sequence(my_list3))
# print(check_sequence(my_list4))
# print(check_sequence(my_list5))
#
# print("""
#
#
# """)
#
# # 1. Juda qisqa va juda uzun listlar
# print(check_sequence([1]))  # True, bitta elementli list
# print(check_sequence([1, 2]))  # True, ikkita elementli list o‘suvchi
# print(check_sequence([2, 1]))  # True, ikkita elementli list kamayuvchi
#
# # 2. Faqat musbat va faqat manfiy sonlardan iborat listlar
# print(check_sequence([-5, -3, -1, 0, 2, 4]))  # True, o‘suvchi
# print(check_sequence([-1, -2, -3, -4, -5]))  # True, kamayuvchi
#
# # 3. Bir xil qiymatlar bilan list
# print(check_sequence([5, 5, 5, 5]))  # False, bir xil qiymat
#
# # 4. Sathma-sath o‘suvchi yoki kamayuvchi ketma-ketliklar
# print(check_sequence([1, 1, 2, 2, 3, 3]))  # False, qattiq o‘suvchi emas
# print(check_sequence([3, 3, 2, 2, 1, 1]))  # False, qattiq kamayuvchi emas
#
# # 5. Bir nechta cho‘qqi yoki vodiy bo‘lsa
# print(check_sequence([1, 3, 2, 4, 2, 5]))  # False, bir nechta cho‘qqi va vodiy mavjud
#
# # Oddiy holatlar uchun yana testlar
# print(check_sequence([0, 1, 2, 3, 4]))  # True, o‘suvchi
# print(check_sequence([5, 4, 3, 2, 1]))  # True, kamayuvchi
# print(check_sequence([1, 3, 2]))  # True, bitta cho‘qqi bor
# print(check_sequence([3, 1, 2]))  # False, bitta vodiy bor


