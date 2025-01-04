data = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 15}]

def total_revenue(purchases):
    """
    :param purchases:
    :return: total revenue
    """
    result = []
    for product in purchases:
        result.append(product.get('price') * product.get('quantity'))
    return f'Общая выручка: {sum(result)}'

def items_by_category(purchases):
    """
    :param purchases:
    :return: result
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
    :param purchases:
    :param min_price:
    :return:
    """
    result = []
    for d_data in purchases:
        if d_data['price'] >= min_price:
            result.append(d_data)
    return f'Покупки дороже {min_price}: {result}'

def average_price_by_category(purchases):
    result = {}
    for d_data in purchases:
        if d_data['category'] not in result:
            result[d_data['category']] = [d_data['price']]
        else:
            result [d_data['category']].append(d_data['price'])
    for d_2_data in result:
        result [d_2_data] = sum(result[d_2_data]) / len(result[d_2_data])

    return f'Средняя цена по категориям: {result}'

def most_frequent_category(purchases):
    result = {}
    for d_data in purchases:
        if d_data['category'] not in result:
            result[d_data['category']] = [d_data['quantity']]
        else:
            result[d_data['category']].append(d_data['quantity'])
    for d_d_data in result:
        result[d_d_data] = sum(result[d_d_data])
    max_quantity = max(result.values())
    answer = []
    for d_d_data in result:
        if result[d_d_data] == max_quantity:
            answer.append(d_d_data)
    if len(answer) > 1:
        return f'Категории с наибольшим количеством проданных товаров: {", ".join(answer)}'
    else:
        return f'Категория с наибольшим количеством проданных товаров: {answer[0]}'

print(total_revenue(data))
print(items_by_category(data))
print(expensive_purchases(data, 1.0))
print(average_price_by_category(data))
print(most_frequent_category(data))
