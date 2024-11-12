# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
#
# sum_a = 0
# i = 1
# while i < a:
#     if a % i == 0:
#         sum_a += i
#     i += 1
#
# sum_b = 0
# j = 1
# while j < b:
#     if b % j == 0:
#         sum_b += j
#     j += 1
#
# if sum_a == b and sum_b == a:
#     print("a va b do'st sonlar.")
# else:
#     print("a va b do'st sonlar emas.")


def check_sequence(lst):
    if len(lst) < 2:
        return True

    is_increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    is_decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

    if is_increasing or is_decreasing:
        return True

    peak_found = False
    valley_found = False

    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1]:
            if peak_found or valley_found:
                return False
            peak_found = True
        elif lst[i - 1] > lst[i] < lst[i + 1]:
            if peak_found or valley_found:
                return False
            valley_found = True

    return peak_found and not valley_found


my_list = [1, 4, 6, 14, 21, 18, 12, -2]  # True
my_list2 = [2, 4, 50, 49, 61]  # False
my_list3 = [90, 89, 31, 12]  # True
my_list4 = [12, 14, 50, 61, 17]  # True
my_list5 = [-100, 60, 9, 2, 1, 67, 78, 89]  # False


print(check_sequence(my_list))
print(check_sequence(my_list2))
print(check_sequence(my_list3))
print(check_sequence(my_list4))
print(check_sequence(my_list5))


print("""



""")

# 1. Juda qisqa va juda uzun listlar
print(check_sequence([1]))  # True, bitta elementli list
print(check_sequence([1, 2]))  # True, ikkita elementli list o‘suvchi
print(check_sequence([2, 1]))  # True, ikkita elementli list kamayuvchi

# 2. Faqat musbat va faqat manfiy sonlardan iborat listlar
print(check_sequence([-5, -3, -1, 0, 2, 4]))  # True, o‘suvchi
print(check_sequence([-1, -2, -3, -4, -5]))  # True, kamayuvchi

# 3. Bir xil qiymatlar bilan list
print(check_sequence([5, 5, 5, 5]))  # False, bir xil qiymat

# 4. Sathma-sath o‘suvchi yoki kamayuvchi ketma-ketliklar
print(check_sequence([1, 1, 2, 2, 3, 3]))  # False, qattiq o‘suvchi emas
print(check_sequence([3, 3, 2, 2, 1, 1]))  # False, qattiq kamayuvchi emas

# 5. Bir nechta cho‘qqi yoki vodiy bo‘lsa
print(check_sequence([1, 3, 2, 4, 2, 5]))  # False, bir nechta cho‘qqi va vodiy mavjud

# Oddiy holatlar uchun yana testlar
print(check_sequence([0, 1, 2, 3, 4]))  # True, o‘suvchi
print(check_sequence([5, 4, 3, 2, 1]))  # True, kamayuvchi
print(check_sequence([1, 3, 2]))  # True, bitta cho‘qqi bor
print(check_sequence([3, 1, 2]))  # False, bitta vodiy bor