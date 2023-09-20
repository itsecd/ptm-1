# -*- coding: utf-8 -*-
#
# Blockchain parser
# Copyright (c) 2015-2023 Denis Leonov <466611@gmail.com>
#
# Данный код имеет несколько нарушений стиля PEP 8:

# \/ Имена переменных: Имена переменных и функций должны быть в snake_case (снейк-регистре), то есть разделяться символами подчеркивания _, а не в camelCase (смешанный регистр).

# \/ Пропущенные пустые строки: В некоторых местах кода не хватает пустых строк для лучшей читаемости.

# \/ Избыточные точки с запятой: В Python точки с запятой в конце строк обычно не используются, за исключением случаев, когда необходимо разместить несколько выражений в одной строке.

# \/ Длинные строки: Некоторые строки кода слишком длинные, что затрудняет их чтение. Рекомендуется разбивать длинные строки на более короткие.

# \/ Неиспользуемые переменные: В коде есть переменные, которые объявляются, но не используются (например, переменная nameRes).

# \/ Документация: В коде отсутствует документация (комментарии или docstrings) к функциям и переменным.


import os
import datetime
import hashlib

def reverse(input_str):
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    length = len(input_str)
    if (length % 2) != 0:
        return None
    else:
        result = ''
        length = length // 2
        for i in range(length):
            t = input_str[i * 2] + input_str[i * 2 + 1]
            result = t + result
            t = ''
        return result

def merkle_root(lst):
    """
    Calculates the Merkle Root of a list of hashes.
    
    Args:
        lst (list): A list of hash values.
        
    Returns:
        str: The Merkle Root hash value.
    """
    sha256d = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
    hash_pair = lambda x, y: sha256d(x[::-1] + y[::-1])[::-1]
    
    if len(lst) == 1:
        return lst[0]
    if len(lst) % 2 == 1:
        lst.append(lst[-1])
        
    return merkle_root([hash_pair(x, y) for x, y in zip(*[iter(lst)]*2)])

def read_bytes(file, n, byte_order='L'):
    """
    Reads and converts bytes from a file.
    
    Args:
        file: The file object to read from.
        n (int): The number of bytes to read.
        byte_order (str): Byte order ('L' for little-endian, 'B' for big-endian).
        
    Returns:
        str: The hexadecimal representation of the read bytes.
    """
    data = file.read(n)
    if byte_order == 'L':
        data = data[::-1]
    data = data.hex().upper()
    return data

def read_varint(file):
    """
    Read a variable-length integer from the given file and return it as an uppercase hexadecimal string.

    Args:
        file (io.BufferedIOBase): An open binary file.
        
    Returns:
        str: The variable length integer as an uppercase hexadecimal string.
    """
    b = file.read(1)
    b_int = int(b.hex(), 16)
    c = 0
    data = ''

    if b_int < 253:
        c = 1
        data = b.hex().upper()
    if b_int == 253:
        c = 3
    if b_int == 254:
        c = 5
    if b_int == 255:
        c = 9

    for j in range(1, c):
        b = file.read(1)
        b = b.hex().upper()
        data = b + data
    return data

dir_a = './blocks/'  # Directory where blk*.dat files are stored
dir_b = './result/'  # Directory where to save parsing results

f_list = os.listdir(dir_a)
f_list = [x for x in f_list if (x.endswith('.dat') and x.startswith('blk'))]
f_list.sort()

for i in f_list:
    name_src = i
    name_res = name_src.replace('.dat', '.txt')
    res_list = []
    a = 0
    t = dir_a + name_src
    res_list.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
    print('Start ' + t + ' in ' + str(datetime.datetime.now()))

    f = open(t, 'rb')
    tmp_hex = ''
    f_size = os.path.getsize(t)
    while f.tell() != f_size:
        tmp_hex = read_bytes(f, 4)
        res_list.append('Magic number = ' + tmp_hex)
        tmp_hex = read_bytes(f, 4)
        res_list.append('Block size = ' + tmp_hex)
        tmp_pos3 = f.tell()
        tmp_hex = read_bytes(f, 80, 'B')
        tmp_hex = bytes.fromhex(tmp_hex)
        tmp_hex = hashlib.new('sha256', tmp_hex).digest()
        tmp_hex = hashlib.new('sha256', tmp_hex).digest()
        tmp_hex = tmp_hex[::-1]
        tmp_hex = tmp_hex.hex().upper()
        res_list.append('SHA256 hash of the current block hash = ' + tmp_hex)
        f.seek(tmp_pos3, 0)
        tmp_hex = read_bytes(f, 4)
        res_list.append('Version number = ' + tmp_hex)
        tmp_hex = read_bytes(f, 32)
        res_list.append('SHA256 hash of the previous block hash = ' + tmp_hex)
        tmp_hex = read_bytes(f, 32)
        res_list.append('MerkleRoot hash = ' + tmp_hex)
        merkle_root = tmp_hex
        tmp_hex = read_bytes(f, 4)
        res_list.append('Time stamp = ' + tmp_hex)
        tmp_hex = read_bytes(f, 4)
        res_list.append('Difficulty = ' + tmp_hex)
        tmp_hex = read_bytes(f, 4)
        res_list.append('Random number = ' + tmp_hex)
        tmp_hex = read_varint(f)
        tx_count = int(tmp_hex, 16)
        res_list.append('Transactions count = ' + str(tx_count))
        res_list.append('')
        tmp_hex = ''
        raw_tx = ''
        tx_hashes = []
        for k in range(tx_count):
            tmp_hex = read_bytes(f, 4)
            res_list.append('TX version number = ' + tmp_hex)
            raw_tx = reverse(tmp_hex)
            tmp_hex = ''
            witness = False
            b = f.read(1)
            tmp_b = b.hex().upper()
            b_int = int(b.hex(), 16)
            if b_int == 0:
                tmp_b = ''
                f.seek(1, 1)
                c = 0
                c = f.read(1)
                b_int = int(c.hex(), 16)
                tmp_b = c.hex().upper()
                witness = True
            c = 0
            if b_int < 253:
                c = 1
                tmp_hex = hex(b_int)[2:].upper().zfill(2)
                tmp_b = ''
            if b_int == 253:
                c = 3
            if b_int == 254:
                c = 5
            if b_int == 255:
                c = 9
            for j in range(1, c):
                b = f.read(1)
                b = b.hex().upper()
                tmp_hex = b + tmp_hex
            in_count = int(tmp_hex, 16)
            res_list.append('Inputs count = ' + tmp_hex)
            tmp_hex = tmp_hex + tmp_b
            raw_tx = raw_tx + reverse(tmp_hex)
            for m in range(in_count):
                tmp_hex = read_bytes(f, 32)
                res_list.append('TX from hash = ' + tmp_hex)
                raw_tx = raw_tx + reverse(tmp_hex)
                tmp_hex = read_bytes(f, 4)
                res_list.append('N output = ' + tmp_hex)
                raw_tx = raw_tx + reverse(tmp_hex)
                tmp_hex = ''
                b = f.read(1)
                tmp_b = b.hex().upper()
                b_int = int(b.hex(), 16)
                c = 0
                if b_int < 253:
                    c = 1
                    tmp_hex = b.hex().upper()
                    tmp_b = ''

                if b_int == 253:
                    c = 3
                if b_int == 254:
                    c = 5
                if b_int == 255:
                    c = 9
                for j in range(1, c):
                    b = f.read(1)
                    b = b.hex().upper()
                    tmp_hex = b + tmp_hex

                script_length = int(tmp_hex, 16)
                tmp_hex = tmp_hex + tmp_b
                raw_tx = raw_tx + reverse(tmp_hex)
                tmp_hex = read_bytes(f, script_length, 'B')
                res_list.append('Value = ' + tmp_hex)
                res_list.append('Output script = ' + tmp_hex)
                raw_tx = raw_tx + tmp_hex
                tmp_hex = ''

    if witness == True:
        for m in range(in_count):
            tmp_hex = read_varint(f)
            witness_length = int(tmp_hex, 16)
            for j in range(witness_length):
                tmp_hex = read_varint(f)
                witness_item_length = int(tmp_hex, 16)
                tmp_hex = read_bytes(f, witness_item_length)
                res_list.append('Witness ' + str(m) + ' ' + str(j) + ' ' + str(witness_item_length) + ' ' + tmp_hex)
                tmp_hex = ''
            witness = False
            tmp_hex = read_bytes(f, 4)
            res_list.append('Lock time = ' + tmp_hex)
            raw_tx = raw_tx + reverse(tmp_hex)
            tmp_hex = raw_tx
            tmp_hex = bytes.fromhex(tmp_hex)
            tmp_hex = hashlib.new('sha256', tmp_hex).digest()
            tmp_hex = hashlib.new('sha256', tmp_hex).digest()
            tmp_hex = tmp_hex[::-1]
            tmp_hex = tmp_hex.hex().upper()
            res_list.append('TX hash = ' + tmp_hex)
            tx_hashes.append(tmp_hex)
            res_list.append('')
            tmp_hex = ''
            raw_tx = ''

        a += 1
        tx_hashes = [bytes.fromhex(h) for h in tx_hashes]
        tmp_hex = merkle_root(tx_hashes).hex().upper()
        if tmp_hex != merkle_root:
            print('Merkle roots do not match! >', MerkleRoot, tmp_hex)
        f.close()
        f = open(dir_b + name_res, 'w')
        for j in res_list:
            f.write(j + '\n')
        f.close()
