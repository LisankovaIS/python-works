import json #импортируем код из модуля json
def schet() -> float:
    spisok = "input.json" # переменная spisok принимает значения input.json

    with open(spisok) as i:
        znachenia = json.load(i) #в переменную загружается значение i в формате JSON

    summa = sum([tsifra["score"] * tsifra["weight"] for tsifra in znachenia]) #счет суммы произведений
    return round(summa, 3) #печатаем сумму, округлив до 3х знаков пасле запятой

print(schet())
