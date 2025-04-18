from bignum_lib import *
import math
import random

def is_prime(n): # Kiểm tra số nguyên tố
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def generate_prime(bits=16): # Tạo số nguyên tố ngẫu nhiên
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_keypair(bits=16):
    # Tạo cặp khóa công khai và khóa bí mật
    # p = 61
    # q = 59
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q: # Đảm bảo p và q khác nhau
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))


def encrypt(pk, plaintext): # Mã hóa thông điệp
    key, n = pk
    cipher = [modexp(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext): # Giải mã thông điệp
    key, n = pk
    plain = [chr(modexp(char, key, n)) for char in ciphertext]
    return ''.join(plain)
