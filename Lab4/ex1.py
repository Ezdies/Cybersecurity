from sympy import ntheory
from sympy import mod_inverse
import random
import math

def is_prime(n):
    return ntheory.isprime(n)

def generate_primes(start, end):
    p = 0
    q = 0
    while not is_prime(p):
        p = random.randint(start, end)
    while not is_prime(q) or p == q:
        q = random.randint(start, end)
    return p, q

def generate_keys():
    p, q = generate_primes(10, 20)
    n = p * q
    phi_n = (p-1)*(q-1)
    
    #wybór e, 1 < e < phi_n && gcd(e, phi_n) == 1
    e = 0
    
    while not e > 1 or not phi_n > e or not math.gcd(e, phi_n) == 1:
        e+=1
        
    d = pow(e, -1, phi_n)
    pub = (n, e)
    priv = (n, d)
    
    
    return pub, priv

def encrypt(pub, m):
    n, e = pub
    c = pow(m, e) % n
    return c
    
def decrypt(priv, c):
    n, d = priv
    m = pow(c, d) % n
    return m

def factorize_n(n):
    """Faktoryzacja n przez szukanie dzielników pierwszych mniejszych lub równych sqrt(n)"""
    limit = math.isqrt(n) + 1
    for p in range(2, limit):
        if n % p == 0:
            q = n // p
            return p, q
    return None, None

def decrypt2():
    # Używane wartości
    n_hex = "140115e871b5a6f"
    n = int(n_hex, 16)
    
    e_hex = "10001"
    e = int(e_hex, 16)
    
    m1_hex = "63a584ee99130"
    m2_hex = "cd21c3e55366ee"
    m3_hex = "d528a0b38d218b"
    m4_hex = "10a9dac5fee040d"
    
    # Zamiana z hex na int
    m1 = int(m1_hex, 16)
    m2 = int(m2_hex, 16)
    m3 = int(m3_hex, 16)
    m4 = int(m4_hex, 16)
    
    # Znajdź p i q takie, że n = p * q
    p, q = factorize_n(n)
    
    if not p or not q:
        return "Faktoryzacja nie powiodła się"
    
    # Obliczenie phi(n)
    phi_n = (p - 1) * (q - 1)
    
    # Obliczenie d, odwrotności modularnej e względem phi(n)
    d = mod_inverse(e, phi_n)
    
    # Deszyfrowanie każdego z szyfrogramów
    decrypted_m1 = pow(m1, d, n)
    decrypted_m2 = pow(m2, d, n)
    decrypted_m3 = pow(m3, d, n)
    decrypted_m4 = pow(m4, d, n)
    
    # Zwróć odszyfrowane wartości
    return decrypted_m1.to_bytes((decrypted_m1.bit_length() + 7) // 8, 'big').decode('utf-8'), decrypted_m2.to_bytes((decrypted_m2.bit_length() + 7) // 8, 'big').decode('utf-8'), decrypted_m3.to_bytes((decrypted_m3.bit_length() + 7) // 8, 'big').decode('utf-8'),     decrypted_m4.to_bytes((decrypted_m4.bit_length() + 7) // 8, 'big').decode('utf-8'),


def ex4(n, m1):
    # Faktoryzacja n na czynniki p i q
    p, q = factorize_n(n)
    print(f"Znalezione czynniki: p = {p}, q = {q}")
    if not p or not q:
        print("Faktoryzacja nie powiodła się")
        return

    # Oblicz φ(n)
    phi_n = (p - 1) * (q - 1)

    # Zbierz wszystkie możliwe wartości e, które są względnie pierwsze z φ(n)
    e_list = [e for e in range(2, phi_n) if math.gcd(e, phi_n) == 1]

    # Próbuj odszyfrować m1 dla każdej wartości e
    for e in e_list:
        try:
            # Znajdź d jako odwrotność modularną e mod φ(n)
            d = mod_inverse(e, phi_n)
            # Odszyfruj wiadomość
            m1_dec = pow(m1, d, n)
            # Zamień odszyfrowaną liczbę na tekst
            m1_text = m1_dec.to_bytes((m1_dec.bit_length() + 7) // 8, 'big').decode('utf-8')
            print(f"Odszyfrowano wiadomość: '{m1_text}', dla e = {e}")
            break  # Jeśli udało się odszyfrować, zakończ pętlę
        except ValueError:
            # Ignoruj błędy związane z odwrotnością modularną
            continue
        except UnicodeDecodeError:
            # Ignoruj błędy dekodowania
            continue

        
        
    
      
print(is_prime(2137))
print(generate_primes(10, 20))
print(generate_keys())
pub, priv = generate_keys()
print(f"pub = {pub} priv = {priv}")

m1 = 2
m2 = "a"
c1 = encrypt(pub, m1)
print(f"{m1} encrypted is: {c1}")
d1 = decrypt(priv, c1)
print(f"decrypted = {d1}")

#print(decrypt2())
# Przykładowy moduł n i szyfrogram m1 (musisz mieć rzeczywiste wartości)
n_hex = "140115e871b5a6f"  # przykładowe n w systemie szesnastkowym
m1_hex = "63a584ee99130"   # przykładowy m1 w systemie szesnastkowym

# Konwersja z systemu szesnastkowego na dziesiętny
#Przykładowe małe liczby, żeby szybko je obliczyło (działa na małych, to powinno też działać na większych)
n = 143
m1 = 42

# Wywołanie funkcji ex4
ex4(n, m1)

