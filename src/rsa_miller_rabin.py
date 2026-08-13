"""
Date: 06/09/2025

Updates the Miller-Rabin code with varibale corrections, added comments
Used to collect run time data
"""

import math
import time
import secrets

#Miller-Rabin Primality Test

print("The computer is generating a large prime number (p)...")
print()


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
print("The computer is generating a large prime number (q)...")
prime_generation_start = time.time()
print()
q = generate_prime()
print("This is the large prime (q):", q)
print()

print("The computer is generating a large prime number (p)...")
print()
p = generate_prime()
print("This is the large prime (p):", p)

prime_generation_end = time.time()
prime_generation_time = prime_generation_end - prime_generation_start
print("It took", prime_generation_time, "seconds to generate q.")

#RSA Algorithm
#p = int(input("Enter a prime number p: "))

m = secrets.randbelow(q)
print("This is our secret message (m):", m)

if m >= q:
    print("Your message must be less than q!")
else:
    n = p * q
    print(" ")
    #print("Public value n (product of primes):", n)
    k = (p - 1)*(q - 1) #this value is kept private
    print("This is the private value k:", k)
    for e in range(2, k): 
        if math.gcd(e, k) == 1:
            print("Public value e (exponent):", e)
            break
d = pow(e, -1, k) #this is the private key

#Ecryption
c = pow(m, e, n) #encoded ciphertext
print() 
#print("This is the encoded message:", c)
print()

#Decrypion
decoded_message = pow(c, d, n)
#print("This is the decoded message:", decoded_message)
print()

#Brute Force Attack
print("Let's conduct a brute force attack...")
start_time = time.time()
for guess in range (n):
    if pow(guess, e, n) == c:
        print("The hacker says the original message is", guess)
        break
print()
end_time = time.time()
time_elapsed = end_time - start_time
print("It took", time_elapsed, "seconds to crack the code!")


            
