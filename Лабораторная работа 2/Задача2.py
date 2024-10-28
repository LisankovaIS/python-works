salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов



dolg = 0
while months > 0:
    dolg = dolg + (salary - spend)
    months -= 1
    spend = spend + spend*increase
months = 10
money_capital = 0 - dolg
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f'{money_capital:.0f}')
