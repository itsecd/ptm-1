from math import sqrt, erfc
from scipy.special import gammainc


def frequency_bit_test(bit_sequence):
    sum = 0
    for i in bit_sequence:
        if i == "1":
            sum += 1
        else:
            sum -= 1
    s = sum/sqrt(len(bit_sequence))
    p = erfc(s/sqrt(2))
    return p


def identical_consecutive_bit_test(bit_sequence):
    unit_sum = 0
    for i in bit_sequence:
        if i == "1":
            unit_sum += 1
    unit_share = unit_sum/len(bit_sequence)
    if abs(unit_share - 0.5) < 1/sqrt(len(bit_sequence)):
        v = 0
        for i in range(len(bit_sequence)-1):
            if bit_sequence[i] != bit_sequence[i+1]:
                v += 1
        p = erfc(abs(v-2*len(bit_sequence)*unit_share*(1-unit_share))/(2*sqrt(2*len(bit_sequence))*unit_share*(1-unit_share)))
    else:
        p = 0
    return p


def unit_long_sequence_test(bit_sequence):
    pi0 = 0.2148
    pi1 = 0.3672
    pi2 = 0.2305
    pi3 = 0.1875
    blocks = [bit_sequence[i:i + 8] for i in range(0, len(bit_sequence), 8)]
    sequences = [0]*16
    for i in range(16):
        unit_sequence = 0
        tmp = 0
        for bit in blocks[i]:
            if bit == "1":
                unit_sequence += 1
            else:
                if unit_sequence > tmp:
                    tmp = unit_sequence
                    unit_sequence = 0
        if tmp > unit_sequence:
            unit_sequence = tmp
        sequences[i] = unit_sequence
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    for unit_sequence in sequences:
        if unit_sequence <= 1:
            v1 += 1
        else:
            if unit_sequence == 2:
                v2 += 1
            else:
                if unit_sequence == 3:
                    v3 += 1
                else:
                    if unit_sequence >= 4:
                        v4 += 1
    x2 = (v1 - 16*pi0)**2/(16*pi0) + (v2 - 16*pi1)**2/(16*pi1) + (v3 - 16*pi2)**2/(16*pi2) + (v4 - 16*pi3)**2/(16*pi3)
    p = gammainc(1.5, x2/2)
    return p


if __name__ == '__main__':
    bit_sequence = "00101110111111110000101100101000011110011001010011000000101001010101110100100100011111000110011101001000110010111100111111110011"
    print (frequency_bit_test(bit_sequence))
    print (identical_consecutive_bit_test(bit_sequence))
    print(unit_long_sequence_test(bit_sequence))