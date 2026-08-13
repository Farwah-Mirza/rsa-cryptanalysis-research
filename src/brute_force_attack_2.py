"""
Date: 07/16/2025

Basic encryption-decryption code with level 1 security (2 large primes)
    Changed brute force, instead of looping through all possible messages m,
        attack attempts all factors of n
    Hoping that this version of the attack will return clearer data with respect
        to relationship betwee run time and RSA varibles
    Uses code from run time data collection
"""

import math
import time
import secrets

#Miller-Rabin Primality Test: generates large primes
def prime_check(n, i = 5): 
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    s = 0
    r = n - 1
    while r % 2 == 0:
        r //= 2
        s += 1
    for _ in range(i):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, r, n)

        if x != 1 and x != n - 1:
            for _ in range(s -1):
                x = pow(x, 2, n)

                if x == 1:
                    return False
                if x == n - 1: 
                    break
            else:
                return False
    return True

def prime_candidate(bits):
    q = secrets.randbits(bits)
    q |= (1 << (bits - 1))
    q |= 1
    return q
#Generate a large prime
def generate_prime(bits = 64):
    while True:
        candidate = prime_candidate(bits)
        if prime_check(candidate, 128):
            return candidate
print("The computer is generating a large prime number (p)...")
p = generate_prime()
print("This is the large prime (p):", p)
print()

print("The computer is generating a large prime number (q)...")
q = generate_prime()
print("This is the large prime (q):", q)


#RSA Algorithm
m = secrets.randbelow(q - 1) + 1
n = p * q
phi = (p - 1)*(q - 1) #this value is kept private
print("This is our private phi(N) value:", phi)
for e in range(2, phi): 
    if math.gcd(e, phi) == 1:
        break
d = pow(e, -1, phi) #this is the private key
print("This is our public e value", e)
print("This is our private d value:", d)

#Ecryption
encrypt_m = pow(m, e, n) #encoded ciphertext    

#Decrypion
decrypt_m = pow(m, d, n)

#Brute Force Attck Function
def rsa_brute_force_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None, None

#Brute Force Attack Implementation
print()
print("Let's conduct a brute force attack...")

start_time = time.time()
p, q = rsa_brute_force_factor(n)

if p and q:
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("mm: The message", m, "took", time_elapsed, "seconds to crack!")
else:
    print("Failed to factor n.")  