#!/usr/bin/env python
"""
Python script to check validity of credit card numbers
Author : PythonCircle.Com
Read more : https://www.pythoncircle.com/post/485/python-script-8-validating-credit-card-number-luhns-algorithm/
"""

import sys


def usage():
    """printing a message"""
    msg = """
        
        usage:
        python3 credit_card_validator credit_card_number
        
        example:
        python3 credit_card_validator 34678253793
        
    """
    print(msg)


def get_cc_number():
    """returns the first command line argument

    Returns:
        str
    """
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    return sys.argv[1]


def sum_digits(digit):
    """counting the sum of values

    Args:
        digit (int): the accepted value for calculating the amount

    Returns:
        int
    """
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):
    """checking the correctness of the card number

    Args:
        cc_num (str): credit card number

    Returns:
        bool
    """
    
    cc_num = cc_num[::-1]
    cc_num = [int(x) for x in cc_num]
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]    
    sum_of_digits = sum(doubled_second_digit_list)    
    return sum_of_digits % 10 == 0


if __name__ == "__main__":
    print(validate(get_cc_number()))
