"""1. A va B butun musbat sonlari berilgan (A > B). A uzunlikdagi kesmada maksimal darajada B kesma joylashtirilgan.
A kesmaning bo'sh qismini aniqlovchi dastur.
"""

# A = int(input("A sonini kiriting (A > B): "))
# B = int(input("B sonini kiriting: "))
#
# qolgan_qism = A
# while qolgan_qism >= B:
#     qolgan_qism -= B
#
# print("Kesmaning bo'sh qismi:", qolgan_qism)


"""2. A va B butun musbat sonlari berilgan (A > B). 
A uzunlikdagi kesmada B kesmadan necha marta joylashtirish mumkinligini aniqlovchi dastur.
"""

# A = int(input("A sonini kiriting (A > B): "))
# B = int(input("B sonini kiriting: "))
#
# count = 0
# qolgan_qism = A
# while qolgan_qism >= B:
#     qolgan_qism -= B
#     count += 1
#
# print("Joylashtirilgan kesmalar soni:", count)


"""3. N va K butun musbat sonlari berilgan. N sonini K songa bo'lgandagi qoldiqni topuvchi dastur."""

# N = int(input("N sonini kiriting: "))
# K = int(input("K sonini kiriting: "))
#
# qolgan_qism = N
# while qolgan_qism >= K:
#     qolgan_qism -= K
#
# print("Qoldiq:", qolgan_qism)


"""4. n butun soni berilgan (n > 0). Agar n soni 3 ning darajasi bo'lsa "3 ning darajasi", 
aks holda "3 ning darajasi emas" natijasini chiqaruvchi dastur.
"""

# n = int(input("n sonini kiriting (n > 0): "))
#
# while n % 3 == 0:
#     n //= 3
#
# if n == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")


"""5. 2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan (n > 0). n = 2^k ni aniqlovchi dastur."""

# n = int(input("n sonini kiriting (n > 0): "))
#
# while n % 2 == 0:
#     n //= 2
#
# if n == 1:
#     print("2 ning darajasi")
# else:
#     print("2 ning darajasi emas")


"""6. n natural soni berilgan |(n > 0). n! = n * (n - 2) * (n - 4) ...| ifodasi hisoblovchi dastur."""

# n = int(input("n sonini kiriting (n > 0): "))
#
# result = 1
# current = n
# while current > 0:
#     result *= current
#     current -= 2
#
# print("Natija:", result)


"""7. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lgan eng kichik butun k sonini topuvchi dastur."""

# n = int(input("n sonini kiriting (n > 0): "))
#
# k = 1
# while k * k <= n:
#     k += 1
#
# print("Kvadrati n dan katta eng kichik k:", k)


"""8. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lmagan eng katta butun k sonini topuvchi dastur."""

# n = int(input("n sonini kiriting (n > 0): "))
#
# k = 1
# while (k + 1) * (k + 1) <= n:
#     k += 1
#
# print("Kvadrati n dan katta bo'lmagan eng katta k:", k)


"""9. n natural soni berilgan (n > 1). 3^k > n shartini qanoatlantiruvchi eng kichik butun k sonini topuvchi dastur."""

# n = int(input("n sonini kiriting (n > 1): "))
#
# k = 0
# while 3 ** k <= n:
#     k += 1
#
# print("Shartni qanoatlantiruvchi eng kichik k:", k)


"""10. n natural soni berilgan (n > 1). k! > n shartini qanoatlantiruvchi eng kichik k sonini topuvchi dastur."""

# n = int(input("n sonini kiriting (n > 1): "))
#
# k = 1
# factorial = 1
# while factorial <= n:
#     k += 1
#     factorial *= k
#
# print("Shartni qanoatlantiruvchi eng kichik k:", k)


"""11. n natural soni berilgan (n > 1). (1 + 2 + 3 + ... + k) >= n 
shart bajariladigan eng kichik k sonini topuvchi dastur.
"""

# n = int(input("n sonini kiriting (n > 1): "))
#
# k = 0
# summa = 0
# while summa < n:
#     k += 1
#     summa += k
#
# print("Shartni qanoatlantiruvchi eng kichik k:", k)


"""12. n natural soni berilgan (n > 1). (1 + 2 + 3 + ... + k) <= n 
shart bajariladigan eng katta k sonini topuvchi dastur.
"""

# n = int(input("n sonini kiriting (n > 1): "))
#
# k = 0
# summa = 0
# while summa + k + 1 <= n:
#     k += 1
#     summa += k
#
# print("Shartni qanoatlantiruvchi eng katta k:", k)


"""13. a soni berilgan (a > 1). (1 + 1/2 + 1/3 + ... + 1/k) > a 
shart bajariladigan eng kichik k sonini topuvchi dastur.
"""

# a = float(input("a sonini kiriting (a > 1): "))
#
# k = 1
# summa = 0
# while summa <= a:
#     summa += 1 / k
#     k += 1
#
# print("Shartni qanoatlantiruvchi eng kichik k:", k - 1)


"""14. a soni berilgan (a > 1). (1 + 1/2 + 1/3 + ... + 1/k) <= a 
shart bajariladigan eng katta k sonini topuvchi dastur.
"""

# a = float(input("a sonini kiriting (a > 1): "))
#
# k = 1
# summa = 0
# while summa + 1 / (k + 1) <= a:
#     summa += 1 / k
#     k += 1
#
# print("Shartni qanoatlantiruvchi eng katta k:", k)
# print("Yig'indi:", summa)
