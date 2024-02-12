#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_total_cost(**products):
    """
    Вычисляет итоговую сумму покупок с учетом налога и скидки.
    Принимает на вход несколько продуктов в формате "название_продукта=цена".
    """
    tax_rate = 0.1  # 10% налог
    discount_rate = 0.05  # 5% скидка

    total_cost = 0

    for product, price in products.items():
        total_cost += price

    # Применяем налог
    total_cost_with_tax = total_cost * (1 + tax_rate)

    # Применяем скидку
    total_cost_with_discount = total_cost_with_tax * (1 - discount_rate)

    return total_cost_with_discount


# Пример использования
if __name__ == "__main__":
    # Покупки в формате "название_продукта=цена"
    result = calculate_total_cost(apple=1.0, banana=0.5, orange=1.2, bread=2.0)

    print(f"Итоговая сумма с учетом налога и скидки: {result}")
