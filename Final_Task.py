data = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3}]

def total_revenue(purchases):
    """
    :param purchases: Входные данные (data)
    :return: Общая выручка (цена * количество для всех записей).
    Вывод: Общая выручка: 23.5
    """
    result = []
    for product in purchases:
        result.append(product.get('price') * product.get('quantity'))
    return f'Общая выручка: {sum(result)}'

def items_by_category(purchases):
    """
    :param purchases: Входные данные (data)
    :return: Словарь -> {Категории: Список уникальных товаров в этой категории}
    Вывод: Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
    """
    result = {}
    for p_data in purchases:
        if p_data['category'] not in result.keys():
            result[p_data['category']] = [p_data['item']]
        else:
            result[p_data['category']].append(p_data['item'])
    return f'Товары по категориям: {result}'

def expensive_purchases(purchases, min_price):
    """
    :param purchases: Входные данные (data)
    :param min_price: Минимальная цена
    :return: Все покупки, где цена товара больше или равна min_price
    Вывод, если min_price = 1.0:
    Покупки дороже 1.0:
    [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10},
    {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2},
    {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 15}]
    """
    result = []
    for part_data in purchases:
        if part_data['price'] >= min_price:
            result.append(part_data)
    return f'Покупки дороже {min_price}: {result}'

def average_price_by_category(purchases):
    """
    :param purchases: Входные данные (data)
    :return: Средняя цена товаров по каждой категории
    Вывод: Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}
    """
    result = {}
    for part_data in purchases:
        if part_data['category'] not in result:
            result[part_data['category']] = [part_data['price']]
        else:
            result[part_data['category']].append(part_data['price'])
    for part_2_data in result:
        result [part_2_data] = sum(result[part_2_data]) / len(result[part_2_data])

    return f'Средняя цена по категориям: {result}'

def most_frequent_category(purchases):
    """
    :param purchases: Входные данные (data)
    :return: Категории, в которой куплено больше всего единиц товаров (учитывайте поле quantity)
    Вывод:
    Категория с наибольшим количеством проданных товаров: fruit
    """
    result_part_one = {}
    for part_data in purchases:
        if part_data['category'] not in result_part_one:
            result_part_one[part_data['category']] = [part_data['quantity']]
        else:
            result_part_one[part_data['category']].append(part_data['quantity'])
    for part_2_data in result_part_one:
        result_part_one[part_2_data] = sum(result_part_one[part_2_data])
    max_quantity = max(result_part_one.values())
    result_part_two = []
    for part_3_data in result_part_one:
        if result_part_one[part_3_data] == max_quantity:
            result_part_two.append(part_3_data)
    if len(result_part_two) > 1:
        return f'Категории с наибольшим количеством проданных товаров: {", ".join(result_part_two)}'
    else:
        return f'Категория с наибольшим количеством проданных товаров: {result_part_two[0]}'

print(total_revenue(data))
print(items_by_category(data))
print(expensive_purchases(data, 1.0))
print(average_price_by_category(data))
print(most_frequent_category(data))
