#!bin/python
import sympy

def isTwoSidedPrime(num):
    return isLeftTruncablePrime(num) and isRightTruncablePrime(num)

def isLeftTruncablePrime(num):
    if (len(num) > 1):
        return sympy.isprime(int(num)) and isLeftTruncablePrime(num[1:])
    else:
        return sympy.isprime(int(num))

def isRightTruncablePrime(num):
    if (len(num) > 1):
        return sympy.isprime(int(num)) and isRightTruncablePrime(num[:len(num)-1])
    else:
        return sympy.isprime(int(num))

