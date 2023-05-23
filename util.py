# This Python file uses the following encoding: windows-1251

from typing import Tuple, List
from random import randint, choice
from math import gcd, sqrt


def read_text(FILENAME):
    f = open(FILENAME, 'r', encoding='windows-1251')
    ot = f.read()
    f.close()
    return ot

def read_text_list(filename):
    text = []
    with open(filename, 'r') as f:
        text.append(f.readline())
    return text

def get_random_message(size: int) -> str:
    # Возращает рандомную строку
    m = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
        m.append(choice(alpha))
    res = ""
    res = res.join(m)
    return res
    
def get_prime_numbers_in_range(start: int, finish: int) -> List[int]:
    # Находит все простые числа на заданном промежутке
    primes = [] # Список простых чисел на интервале
    # Список в котором True - число простое, False - число составное
    is_prime = [True] * (finish + 1)
    # 0 и 1 не простые
    is_prime[0] = is_prime[1] = False
    # решето Эратосфена i - число, is_prime_i - простое или нет
    for i, is_prime_i in enumerate(is_prime):
        if is_prime_i:
            # добавляем простое число в список, если оно в интервале
            if i >= start:
                primes.append(i)
            # все числа от i * i до finish с шагом i кратны i
            for j in range(i * i, finish + 1, i):
                is_prime[j] = False
    return primes

def get_prime_number_in_range(start: int, finish: int) -> int:
    # Находит простое числo на промежутке [start, finish]
    res = get_prime_numbers_in_range(start, finish)
    return res[randint(2, len(res) - 1)]

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    # Рассширенный алгоритм Евклида
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t

def binary_pow(a: int, b: int, p: int) -> int:
    # Алгоритм бинарного возведения в степень
    # Если степень равна 0, то результат равен 1
    if b == 0:
        return 1
    # представление d в двоичной ситсеме
    # функция bin() возвращает строку вида '0b1010'
    # поэтому представление в двоичной системе начинается со 2 символа
    d = bin(b)[2:]
    r = len(d) - 1
    # создадим массив a_i
    a_ = [0] * (r + 1)
    # положим a_0 = a
    a_[0] = a
    # вычисляем a_i для i = 1,...,r, r = len(d) - 1
    for i in range(1, r + 1):
        # вычисляем a_i
        a_[i] = (a_[i - 1] ** 2) * (a ** int(d[i]))
        # берем остаток по модулю
        a_[i] %= p
    # возвращаем a_r по модулю для случаев когда d = 1
    return a_[r] % p

def modular_inv(number: int, mod: int) -> int:
    # Находит обратное число по модулю для числа
    # Находим НОД модуля и числа и коэффициенты соотношения Безу
    # используя расширенный алгоритм евклида.
    t, x, y = extended_gcd(number, mod)
    # если НОД не равен 1, то обратного числа нет
    if t != 1:
        raise ValueError('----')
    # для отрицательных чисел нужно прибавить модуль
    return (x % mod + mod) % mod

def get_coprime_in_range(
        start: int, finish: int, number: int) -> int:
    # Находит число на промежутке [start, finish] взаимно простое с number
    for i in range(start, finish):
        if gcd(number, i) == 1:
            return i
    return i

def is_prime(n: int) -> bool:
    # Проверяет, является ли число простым.
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_values(a: int, b: int, p: int) -> bool:
    # Проверяет значения параметров алгоритма
    #
    return gcd(a, p) == 1 and gcd(b, p) == 1 and p != 2 and is_prime(p)

def get_values(number_of_runs: int) -> List[Tuple[int, int, int]]:
    # Функция генерирует значения для проверки времени исполнения.
    # Значения подбираются для соответствия условиям методов.
    values = []
    for _ in range(number_of_runs):
        a, b, p = 0, 0, 0
        # Пока числа не соответствуют условиям метода
        # генерируем новые значения
        while not check_values(a, b, p):
            a, b, p = randint(1, 900), randint(1, 900), randint(1, 900)
        values.append((a, b, p))
    return values