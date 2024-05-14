# Проверка вхождения подстроки
# str_= input()
# is_substr = "Строка" in str_
# print ("В строке есть слово Строка?", is_substr)

# Условие првоерки целого числа
# number = int(input())
# condition_1 = number % 2 == 0
# condition_2 = number % 3 == 0
#
# if condition_1 and condition_2:
#     print("Число кратно 2 и 3")
# else:
#     print ("Число не кратно 2 и 3")

# Условие определения месяца
# print ("Введите месяц")
# month = int(input())
# good_cond = month in [12,1,2]
# if good_cond:
#     print ("Winter")

#Определение утра
# print ("Введите час")
# hour = int(input())
# good_condition = 6 <= hour < 12
# if good_condition:
#     print ("Morning")

#-----------------------------------------------
#Tasks 7
# Условие определения месяца modified
# print ("Введите номер месяца")
# month = int(input())
# wint_cond = month in [12,1,2]
# spring_cond = month in [3,4,5]
# summer_cond = month in [6,7,8]
# autumn_cond = month in [9,10,11]
# if wint_cond:
#     print ("Winter")
# elif spring_cond:
#     print ("Spring")
# elif summer_cond:
#     print ("Summer")
# elif autumn_cond:
#     print ("Autumn")
# else:
#     print ("Некоректный номер месяца")

#Проверка логики оформления заказа и применения скидки в интернет магазине
# logged = input ("Пользователь вошёл в систему? Да/Нет")
# item_cart = input ("У пользователя есть товары в корзине? Да/Нет")
# shipping_adress = input ("У пользователя указан адрес доставки? Да/Нет")
# total_purchase = int(input ("На какую сумму находятся товары в корзине?"))
# first_purchase = input ("Это первая покупка пользователя? Да/Нет")
#
# if logged and item_cart and shipping_adress == "Да":
#     print ("Все критерии для оформления выполнены. Заказ может быть оформлен")
#     if (total_purchase > 1000) or (first_purchase == "Да"):
#         print ("К заказу применена скидка")
# else:
#     print ("Критерии не выполнены. Заказ не может быть оформлен. Пожалуйста, проверьте информацию")

# Проверка чисел
# number = int(input("Введите число"))
# if 1 <= number <= 100:
#     print ("Число в указаном диапазоне")
#     if number in [7,13,21]:
#         print ("Это - счастливое число")
#     else:
#         print ("Не повезло")
# else:
#     print ("Неправильно указано число")