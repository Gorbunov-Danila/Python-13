def find_sum_between_negatives(*args):
    """
    Находит сумму аргументов между первым и вторым отрицательными аргументами.
    Возвращает None, если передан пустой список аргументов.
    """
    if not args:
        return None

    first_negative_index = None
    second_negative_index = None

    for i, arg in enumerate(args):
        if arg < 0:
            if first_negative_index is None:
                first_negative_index = i
            else:
                second_negative_index = i
                break

    if first_negative_index is None or second_negative_index is None:
        return None

    sum_between_negatives = sum(args[first_negative_index + 1:second_negative_index])

    return sum_between_negatives


# Пример использования
if __name__ == "__main__":
    result = find_sum_between_negatives(1, 2, -3, 4, 5, -6, 7, 8, -9)
    print(f"Сумма аргументов между первым и вторым отрицательными: {result}")
