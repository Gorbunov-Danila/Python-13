#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garmonic_mean(*args):
    """
    Вычисление среднего гармонического
    """
    if args:
        values = [float(arg) for arg in args]

        reciprocal_sum = sum(1 / arg for arg in values)
        return len(args) / reciprocal_sum
    
    else: 
        return None


def main():
    """
    Главная функция программы.
    """
    print(garmonic_mean(2, 4, 8, 16, 32))
    print(garmonic_mean(4, 5, 6, 1))
    print(garmonic_mean(5, 6, 7))
    print(garmonic_mean())

if __name__ == "__main__":
    main()