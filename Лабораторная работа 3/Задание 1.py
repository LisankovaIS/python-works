# TODO Напишите функцию для поиска индекса товара


def find_index(spisok, tovar):
    index = 0
    if tovar in items_list:
        k=0
        while items_list[k] != tovar:
            k+=1
            index+=1
        return index
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
