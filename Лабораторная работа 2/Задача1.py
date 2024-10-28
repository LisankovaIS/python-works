money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
allmoney = money_capital-spend
months = 0
while allmoney > 0:
    allmoney = allmoney + salary - spend
    spend = spend + spend*increase
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
