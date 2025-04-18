def gcd(a, b): # Ước chung lớn nhất
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b): # Ước chung lớn nhất mở rộng 
    if b == 0:
        return (1, 0, a)
    else:
        x1, y1, d = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (x, y, d)
    
def modinv(e, phi): # Tìm số nghịch đảo của e mod phi
    x, y, g = extended_gcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse")
    else:
        return x % phi

def modexp(base, exponent, mod): # Tính lũy thừa modulo
    result = 1
    base %= mod
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result

