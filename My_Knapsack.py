# This Python file uses the following encoding: windows-1251

import string
import util
import random


bitalph = {"A": "00000", "B": "00001", "C": "00010", "D": "00011", "E": "00100"
             , "F": "00101", "G": "00110", "H": "00111", "I": "01000", "J": "01001"
             , "K": "01010", "L": "01011", "M": "01100", "N": "01101", "O": "01110"
             , "P": "01111", "Q": "10000", "R": "10001", "S": "10010", "T": "10011"
             , "V": "10100", "U": "10101", "W": "10110", "X": "10111", "Y": "11000", "Z": "11001"}


def get_superincr_list():
    l = []
    l.append(random.randint(1,8))
    for i in range(3):
        sum = 0
        for j in l: sum += j 
        t = random.randint(sum+1,10+sum)
        l.append(t) 
    return l


def knapSack_loop(W, S, result):
    n = len(W)
    if n == 0 or S < 0:
        result[0] = 1
        return result
    if S == 0:
        result[0] = 0
        return result
    if (W[n-1] <= S):
        result[n-1]=1
        S = S - W[n-1] 
    else: result[n-1]=0
    w = []
    for i in range(n-1): w.append(W[i]) 
    return knapSack_loop(w, S, result)


def knapSack(W, S):
    n = len(W)
    result = [0 for i in range(n)]
    return knapSack_loop(W, S, result)


def knapSack_loop_out(W, S, result, text):
    n = len(W)
    if n == 0:
        text.append(f'Решение: {result}\n')
        res = "".join(text)
        return res
    if (W[n-1] <= S):
        result[n-1] = 1
        S = S - W[n-1] 
        text.append(f'w_{n-1} = {W[n-1]} <= S = {S}\n')
    else:
        result[n-1] = 0
        text.append(f'w_{n-1} = {W[n-1]} > S = {S}\n')
    text.append(f'x_{n-1} = {result[n-1]}\n')
    w = []
    for i in range(n-1): w.append(W[i]) 
    return knapSack_loop_out(w, S, result, text)


def knapSack_out(W, S):
    text = []
    text.append(f'Задача о рюкзаке:\n')
    n = len(W)
    for i in range(n - 1):
        text.append(f' {W[i]}*x_{i} +')
    text.append(f'{W[n-1]}*x_{n-1} = {S}\n')
    result = [0 for i in range(n)]
    return knapSack_loop_out(W, S, result, text)


# W = [6,8,15,31]
# S = 54
# for i in knapSack(W, S):
#     print(i)


def ks_encrypt(v, m, w, text):
    text = text.translate(str.maketrans({key: None for key in string.punctuation}))
    text = ''.join(text.split()).upper()
    text = [i for i in ''.join([bitalph[i] for i in text])]
    for i in range(len(text)%len(v)): text.append('1')
    temp_text = [''.join([text[i+j] for j in range(len(v))]) for i in range(0,len(text),len(v))]
    numb = [(i*w) % m for i in v]
    crypt = []
    for i in temp_text:
        sum = 0
        for k in range(len(v)):
            sum += int(i[k])*numb[k]
        crypt.append(sum)
    return crypt


def ks_encrypt_outp(v, m, w, text):
    outp_text = []
    text = text.translate(str.maketrans({key: None for key in string.punctuation}))
    text = ''.join(text.split()).upper()
    outp_text.append(f"text = '{text}'\n")
    text = [i for i in ''.join([bitalph[i] for i in text])]
    outp_text.append(f'Заменим текст на двоичный код\n')
    outp_text.append(f"text = {''.join(text)}\n")
    outp_text.append(f'Дописываем 1, если необходимо. Разбиваем на блоки.\n')
    for i in range(len(text)%len(v)): text.append('1')
    temp_text = [''.join([text[i+j] for j in range(len(v))]) for i in range(0,len(text),len(v))]
    outp_text.append(f'text = {temp_text}\n')
    outp_text.append(f'Нахоим последовательность шифрования по формуле v_1 * w (mod m)\n')
    numb = [(i*w) % m for i in v]
    for i in range(len(v)):
        outp_text.append(f'({v[i]} * {w}) (mod {m}) = {numb[i]}\n')
    outp_text.append(f'Последовательность шифрования: {numb}\n')
    crypt = []
    for i in temp_text:
        sum = 0
        for k in range(len(v)):
            sum += int(i[k])*numb[k]
            outp_text.append(f'{i[k]} * {numb[k]}')
            outp_text.append(f' + ')
        crypt.append(sum)
        outp_text[len(outp_text) - 1] = f" = {sum}\n"
    outp_text.append(f'Шифр: {crypt}\n')
    res = "".join(outp_text)
    return res


def ks_decrypt(v, m, w, crypt):
    w_inv = util.modular_inv(w, m)
    numb = [(i*w) % m for i in v]
    temp = [i*w_inv % m for i in numb]
    text_temp = ''
    for i in crypt:
        for j in knapSack(temp, w_inv*i % m): text_temp += str(j)
    text = []
    for i in range(0, len(text_temp) - 5, 5):
        temp = ''
        for k in range(5): temp += text_temp[i+k]
        text.append(temp) 
    res = []
    for z in text:
        keys = [ch for ch, code in bitalph.items() if code == z]
        if keys:
            res.append(keys[0])
    res = ''.join(res)
    return res

# print(ks_decrypt([6, 8, 15, 31], 65, 12,ks_encrypt([6, 8, 15, 31], 65, 12,'on sale.')))

def ks_decrypt_outp(v, m, w, crypt):
    outp_text = []
    w_inv = util.modular_inv(w, m)
    outp_text.append(f'Обратное w по модулю m: w_inv = {w_inv}\n')
    numb = [(i*w) % m for i in v]
    outp_text.append(f'Последовательность шифрования: {numb}\n')
    temp = [i*w_inv % m for i in numb]
    outp_text.append(f'Веса для задачи о рюкзаке: {temp}\n')
    text_temp = ''
    for i in crypt:
        s = w_inv*i % m
        outp_text.append(f'S = {w_inv}*{i} (mod {m}) = {w_inv*i % m}\n')
        out=''
        for j in knapSack(temp, s):
            text_temp += str(j)
            out += str(j)
        outp_text.append(f'Решене для S={s}: {out}\n')
    text=[]
    for i in range(0, len(text_temp)-5, 5):
        temp = ''
        for k in range(5): temp += text_temp[i+k]
        text.append(temp) 
    outp_text.append(f'Восстановим открытый текст, перегруппировав биты в блоки длиной пять бит:\n')
    outp_text.append(f'{text}\n')
    outp_text.append(f'Заменим каждый блок на соотвествующую букву:\n')
    res=[]
    for z in text:
        keys = [ch for ch, code in bitalph.items() if code == z]
        if keys:
            res.append(keys[0])
    outp_text.append(f'{res}\n')
    res = ''.join(res)
    outp_text.append(f"text = '{res}'\n")
    outp_text = "".join(outp_text)
    return outp_text


def get_val_tsk_3_1():
    w = [x ** random.randint(1, 3) for x in range(2, random.randint(5, 6))]
    w.sort()
    s = random.randint(w[2], 100)
    return w, s

def get_val_tsk_3_2():
    w = [x ** random.randint(1,3) for x in range(2, random.randint(5, 6))]
    w.sort()
    m = random.randint(2, 90)
    v = random.randint(2, 40)
    while util.extended_gcd(m, v)[0] != 1:
        m = random.randint(2, 90)
        v = random.randint(2, 40)
    text = util.get_random_message(6)
    return w, m, v, text.upper()


def get_val_tsk_3_3():
    w = [x ** random.randint(1,3) for x in range(2, random.randint(5, 6))]
    w.sort()
    m = random.randint(2, 90)
    v = random.randint(2, 40)
    while util.extended_gcd(m, v)[0] != 1:
        m = random.randint(2, 90)
        v = random.randint(2, 40)
    text = util.get_random_message(6)
    crypt = ks_encrypt(w, m, v, text.upper())
    return w, m, v, crypt