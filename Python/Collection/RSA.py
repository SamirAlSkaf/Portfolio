import sympy

def generate_keys():
    p = 61  # Primzahlen
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # Öffentlicher Schlüssel
    d = mod_inverse(e, phi)
    return n, e, d

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plaintext, e, n):
    return pow(plaintext, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Hauptfunktion
if __name__ == "__main__":
    n, e, d = generate_keys()
    message = 42  # Nachricht als Zahl
    encrypted = encrypt(message, e, n)
    print("Verschlüsselt:", encrypted)
    decrypted = decrypt(encrypted, d, n)
    print("Entschlüsselt:", decrypted)
