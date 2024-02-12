#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_mean(*args):
    """
    Вычисление среднего геометрического
    """
    if args:
        values = [float(arg) for arg in args]

        value = 1

        for arg in values:
            value *= arg
        return value ** (1 / len(values))
    
    else: 
        return None


def main():
    """
    Главная функция программы.
    """
    print(geometric_mean(3, 5, 9, 4))
    print(geometric_mean(5, 25, 16))
    print(geometric_mean(3, 7, 9, 17, 2))
    print(geometric_mean())


if __name__ == "__main__":
    main()