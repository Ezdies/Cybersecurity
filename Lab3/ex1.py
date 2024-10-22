from sympy import ntheory
import random
from math import gcd

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
    
    while not e > 1 or not phi_n > e or not gcd(e, phi_n) == 1:
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


