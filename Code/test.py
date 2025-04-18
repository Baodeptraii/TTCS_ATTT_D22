from rsa import *
plaintext = "Hello, I'm B22DCAT034"
# p = 61
# q = 59
public, private = generate_keypair()
print("Khóa công khai:", public)
print("Khóa bí mật:", private)

cipher = encrypt(public, plaintext)
print("Mã hóa:", cipher)

decrypted = decrypt(private, cipher)
print("Giải mã:", decrypted)
