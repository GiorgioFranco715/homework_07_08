#Завдання 2(b):
# def introdusing(user_name,user_age):
#         try:
#             if 130 < user_age or user_age < 0:
#                 raise ValueError("You noted incorectly age")
#
#             introdusing = (f"Hello,{user_name}!Your age is {user_age}.")
#             return introdusing
#         except ValueError as err:
#             print(f"Error:{err}.Try again")

#Завдання 2(a):
# def introdusing(user_name, user_age):
#     introdusing = (f"Hello,{user_name}!Your age is {user_age}.")
#     return introdusing

#Завдання 4(а):
# def sort_list():
#     positive_list = []
#     negative_list = []
#
#
#     for item in new_list:
#         if item > 0:
#             positive_list.append(item)
#         else:
#             negative_list.append(item)
#     return positive_list,negative_list

#Завдання 4(b):
# def sort_list():
#     positive_list = []
#     negative_list = []
#
#     for item in new_list:
#         if item > 0:
#             positive_list.append(item)
#         else:
#             negative_list.append(item)
#     if not negative_list:
#                 sum_numbers = sum(positive_list)
#                 return sum_numbers
#     else:
#                 return positive_list,negative_list






# if __name__ == "__main__":
#      print("Zdorov")

     #Завдання 1
     #Напишіть програму, яка запитує у користувача ім'я та вік.
     #Після отримання даних програма повинна виводити привітання у форматі: "Привіт, {ім'я}! Твій вік — {вік}".
     #Обробіть виняток, що виникає при введенні некоректного віку (вік < 0 або вік > 130), і виведіть повідомлення про помилку.

     #Task solution:
     # while True:
     #    try:
     #        user_name = input("What is your name:")
     #        user_age = int(input("How old are you:"))
     #        if 130 < user_age or user_age < 0:
     #            raise ValueError("You noted incorectly age")
     #
     #
     #
     #        introdusing = (f"Hello,{user_name}!Your age is {user_age}.")
     #        print(introdusing)
     #        break
     #    except ValueError as err:
     #        print(f"Error:{err}.Try again")





     #Завдання 2
     #Реалізуйте перше завдання через функцію.
     #Функція повинна приймати ім'я і вік як параметри і повертати відформатований рядок
     #Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
     #a)Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
     #b)Друга версія обробляє виняток усередині функції.


     # user_name = input("What is your name:")
     # user_age = int(input("How old are you:"))
     #
     # #Task solution:
     # try:
     #    if 130 < user_age or user_age < 0:
     #        raise ValueError("You noted incorectly age")
     # except ValueError as err:
     #    print(f"Error:{err}.Try again")
     # print(introdusing(user_name,user_age))



     #Завдання 3
     #Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних (число більше нуля) чисел.
     #Числа необхідно накопичувати у списку. Після отримання всіх значень програма повинна проаналізувати дані.
     #У разі виявлення від'ємного значення програма має згенерувати виняток.
     #Якщо всі значення у списку позитивні, програма має повернути на екран суму всіх чисел списку.
     #Згенерований виняток має бути оброблений кодом програми.

     #Task solution:
     # new_list = []
     # while True:
     #     user_numbers = int(input("Введіть числа (для завершення процесу введіть 0):"))
     #     if user_numbers == 0:
     #            break
     #     new_list.append(user_numbers)
     #
     # positive_list = []
     # negative_list = []
     #
     # for item in new_list:
     #    if item > 0:
     #        positive_list.append(item)
     #    else:
     #        negative_list.append(item)
     # if not negative_list:
     #     sum_numbers = sum(positive_list)
     #     print(sum_numbers)
     # else:
     #    print(negative_list)
     #    print(positive_list)


     #Завдання 4
     #Реалізуйте третє завдання через функцію.
     #Функція повинна приймати список як аргумент і повертати суму елементів списку.
     #Перевірка коректності отриманих даних повинна бути всередині функції.
     #Створіть дві версії реалізації функції:
     # a)Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
     # b)Друга версія обробляє виняток усередині функції.

     #User date:
     # new_list = []
     # while True:
     #     user_numbers = int(input("Введіть числа (для завершення процесу введіть 0):"))
     #     if user_numbers == 0:
     #            break
     #     new_list.append(user_numbers)

     #Task solution(a):
     # results = sort_list()
     #
     #
     #
     # if not results[1]:
     #     sum_numbers = sum(results[0])
     #     print(sum_numbers)
     # else:
     #     print(results[1])
     #     print(results[0])

     #Task solution(b):
     # print(sort_list())