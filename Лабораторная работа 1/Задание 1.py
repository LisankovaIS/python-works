numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
dlen = len(numbers)
numbers [4] = 0
summa = sum(numbers)
numbers [4] = summa/dlen
print("Измененный список:", numbers)
