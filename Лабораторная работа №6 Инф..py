# def number(n):
#     if len(n) != 6 and len(n) != 7:
#         print("Неправильный формат номерного знака.")
#         return
#
#     # Проверка на старый формат (три буквы и три цифры)
#
#     if n[:3].isalpha() and n[3:].isdigit():
#         print("Старый формат номера")
#
#         # Проверка на новый формат (четыре цифры и три буквы)
#
#
#     elif n[:4].isdigit() and n[4:].isalpha():
#         print("Новый формат номера")
#
#     else:
#         print("Неправильный формат")
#
# n = input("Введите номерной знак машины: ").upper()
# number(n)



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# s = []
# while True:
#     numbers = int(input(f"Введите элемент массива ", ))
#
#     if numbers == 0:
#         """Проверка на Рост и 0"""
#         if len(s) >= 2:
#             print(max(s))
#             print(min(s))
#         elif len(s) < 2:
#             print("Нам некого сравнивать, необходимо минимум 2!")
#             continue
#         else:
#             break
#
#     if numbers > 0:
#         s.append(numbers)
#     else:
#         print("Рост не может быть отрицательным")
#
# """Проверка на Рост и 0"""
# if len(s) >= 2:
#     print(max(s))
#     print(min(s))
#
# print("Max", max(s))
# print("Min",min(s))
# print(s)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# a = []
# sum = 0
# for i in range(1,101):
#     if i%2==0:
#         a.append(i)
#         sum += i
# print(a)
# print(sum)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# n = int(input("n = "))
# s = [0] * n
# sum = 0
# for i in range(1, n+1):
#     sum += i**2
# print(sum)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# n = int(input("Вводи высоту ёлки: ", ))
# for i in range(1, n+1):
#     sim = 2 * i -1 #Кол-во символов "#"
#     puss = n - i #Кол-во пробелов слева
#     print(' ' * puss + '#' * sim)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# n = float(input("Введите сколько леь вашей собаке? "))
# human = 0
# if n < 0:
#     print("Ошибка! Возраст не может быть отрицательным.")
# elif n <= 2:
#     human = n * 10.5
#     print(f" Введённый вами год собаки эквивалентен - {human} человеческим")
# else:
#     human = 2 * 10.5 + (n - 2) * 4
#     print(f"Введенный вами год эквивалентен {human} человеческим")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import random
# secret = random.randint(1, 10)
# popitka = random.randint(1, 10)
# print("Хорошо, я загадал число. Попробуй его отгадать")
# while 1:
#     print("Попыток у вас: ", popitka )
#     num = int(input("> "))
#     if num == secret:
#         print("Поздравляю! Вы угадали!")
#         print("Хотите сыграть снова?")
#         f = str(input("Введите ответ да или нет: ", ))
#         if f == 'да' or 'Да' or 'ДА':
#             secret = random.randint(1, 10)
#             popitka = random.randint(1, 10)
#             num = int(input("> "))
#         else:
#             break
#     elif popitka == 1:
#         print("Кажется, 'Поле чудес' не ваша игра....")
#         break
#     else:
#         print("Нее, ты не угадал. Попробуй снова")
#         popitka -= 1
#         print(f"У вас осталось попыток{popitka}")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# n = input("Введите ШЕСТИЗНАЧНОЕ число ", )
# # print(f"{n % 1000000 // 100000} {n % 100000 // 10000} {n % 10000 // 1000} {n % 1000 // 100} {n % 100 // 10} {n % 10}")
# if len(n) != 6 or not n.isdigit():
#     print("Некорректный билет")
# elif (int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5])):
#     print("Поздравляю! Ваш билет - счастливый")
#
# else:
#     print("Обычный билет")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import random
# des = 0
# dva = []
# for i in range(1,9):
#     a = random.randint(0,1)
#     dva.append(a)
# print(dva)
# for i in range(len(dva)):
#     if dva[i] == 1:
#         des += dva[i] * 2**i
# print(des)


binary_input = input()
decimal_output = int(binary_input, 2)
print(f"Двоичное число {binary_input} в десятичной системе равно {decimal_output}")

