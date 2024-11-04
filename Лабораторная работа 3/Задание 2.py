# TODO Напишите функцию find_common_participants

def find_common_participants(one_str, two_str, z = ','):
    one_str = one_str.split(z)
    two_str = two_str.split(z)
    allspisok = list(set(one_str).intersection(two_str))
    allspisok.sort()
    return allspisok

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
