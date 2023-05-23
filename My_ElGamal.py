# This Python file uses the following encoding: windows-1251

from typing import Tuple, List
from random import randint
from math import gcd
from util import binary_pow, get_prime_number_in_range, get_coprime_in_range, get_random_message, modular_inv


def my_hash(string: str, p: int) -> int:
    # Находит дайджест строки string
    #
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])
    return sum % p


def get_primitive_root(p: int) -> int:
    #  Находит первообразноый корень по модулю p
    #
    # if p == 2:
    #     return 1
    # p1 = 2
    # p2 = (p - 1) // p1
    # while True:
    #     g = randint(2, p - 1)
    #     if not (binary_pow(g, (p - 1) // p1, p) == 1):
    #         if not binary_pow(g, (p - 1) // p2, p) == 1:
    #             return g
    res = get_primitive_roots(p)
    return res[randint(1, len(res) - 1)]


def get_primitive_roots(modulo: int) -> List[int]:
    # Находит все первообразные корни числа modulo
    #
    roots = []
    required_set = set(
        num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) %
                         modulo for powers in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots


def get_keys_ElGamal(A: int, B: int) -> Tuple[int, int, int, int]:
    # Генерирует открытый и приватный кдючи для ЭЦП Эль-Гамаля
    #
    # Выбор простого числа p
    p = get_prime_number_in_range(A, B)
    # Выбор целое число g - первообразный корень p, g < p
    g = get_primitive_root(p)
    while g >=p:
        g = get_primitive_root(p)
    # Выбор случайного целого числа x такого, что 1 < x < p-1
    x = get_prime_number_in_range(1, p - 1)
    # y = g^x (mod p)
    y = binary_pow(g, x, p)
    return y, p, g, x


def ds_ElGamal(m: str, p: int, g: int, x: int) -> Tuple[int, int]:
    # Создает ЦП Эль-Гамаля сообщения m
    #
    h = my_hash(m, p)
    k = get_coprime_in_range(2, p - 1, p - 1)
    r = binary_pow(g, k, p)
    u = binary_pow((h - x * r), 1, p - 1)
    k_inv = modular_inv(k, p - 1)
    s = binary_pow((u * k_inv), 1, p - 1)
    return r, s


def ds_ElGamal_outp(m: str, p: int, g: int, x: int) -> str:
    # Создает ЦП Эль-Гамаля сообщения m
    #
    outp = []
    outp.append(f'Создание подписи <r, s> для: m = {m}, p = {p}, g = {g}, x = {x}\n')
    h = my_hash(m, p)
    outp.append(f'h = h(m) = h({m}) = {h}\n')
    k = get_coprime_in_range(2, p - 1, p - 1)
    outp.append(f'1 < k < p - 1 \n1 < k < {p-1} \nk = {k}\n')
    r = binary_pow(g, k, p)
    outp.append(f'r = g^k (mod p) = {g}^{k} (mod {p}) = {r}\n')
    u = binary_pow((h - x * r), 1, p - 1)
    outp.append(f'u = (h - x * r) (mod p-1) = ({h} - {x} * {r}) (mod {p-1}) = {u}\n')
    k_inv = modular_inv(k, p - 1)
    outp.append(f'k^-1 = {k_inv}\n')
    s = binary_pow((u * k_inv), 1, p - 1)
    outp.append(f's = k^-1 * u (mod p-1) = {k_inv} * {u} (mod {p-1}) = {s}\n')
    outp.append(f"Подпись: <{r},{s}>\n")
    # outp.reverse()
    res = "".join(outp)
    return res


def check_ds_ElGamal(m: str, r: int, s: int, y: int, g: int, p: int) -> bool:
    # Проверяет ЦП Эль-Гамаля сообщения m
    #
    if ((r < 0 or r > p) or (s < 0 or s > p - 1)):
        return False
    h = my_hash(m, p)
    left = binary_pow(binary_pow(y, r, p) * binary_pow(r, s, p), 1, p)
    right = binary_pow(g, h, p)
    if (left == right):
        return True
    else:
        return False


def check_ds_ElGamal_outp(m: str, r: int, s: int,
                          y: int, g: int, p: int) -> str:
    # Проверяет ЦП Эль-Гамаля сообщения m
    #
    outp2 = []
    outp2.append(f"Проверка подписи <{r}, {s}> для: m = {m}, p = {p}, g = {g}, y = {y}\n")
    if (r < 0 or r > p):
        outp2.append(f"Число r = {r} некорректно.\n")
        res = "".join(outp2)
        return res
    elif(s < 0 or s > p - 1):
        outp2.append(f"Число s = {s} некорректно.\n")
        res = "".join(outp2)
        return res

    h = my_hash(m, p)
    outp2.append(f'h = h(m) = h({m}) = {h}\n')
    left = binary_pow(binary_pow(y, r, p) * binary_pow(r, s, p), 1, p)
    outp2.append(f'y^r * r^s (mod p) = {y}^{r} * {r}^{s} (mod {p}) = {left} \n')
    right = binary_pow(g, h, p)
    outp2.append(f'g^h (mod p) = {g}^{h} (mod {p}) = {right}\n')
    if (left == right):
        outp2.append(f'{left} = {right}\n')
        outp2.append('Подпись подлинна.\n')
        res = "".join(outp2)
        return res
    else:
        outp2.append(f'{left} != {right}\n')
        outp2.append('Подпись подделана.\n')
        res = "".join(outp2)
        return res
    
def get_val_tsk_1_1_1():
    p_a = randint(1000, 1100)
    p_b = p_a + randint(300, 500)
    return p_a, p_b

def get_val_tsk_1_1_2():
    return get_prime_number_in_range(20, 300)

def get_val_tsk_1_1_3():
    p = get_prime_number_in_range(700, 900)
    g = get_primitive_root(p)
    x = get_prime_number_in_range(1, p - 1)
    return p, g, x

def get_val_tsk_1_2():
    p = get_prime_number_in_range(10, 100)
    g = get_primitive_root(p)
    x = get_prime_number_in_range(1, p - 1)
    m = get_random_message(6)
    return p, g, x, m

def get_val_tsk_1_3():
    y, p, g, x = get_keys_ElGamal(10, 100)
    m = get_random_message(6)
    r, s = ds_ElGamal(m, p, g, x)
    return m, p, g, y, r, s