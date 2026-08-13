"""
Date: 06/13/2025

This code is an attempt to generate primes and run through attack sequences
on its own. We also change the previous sequence so that we are generating
multiple messages. 
"""

import math
import time
import secrets

prime_list = [
    [45259, 57899],
    [37907, 61463],
    [54787, 42061],
    [43577, 53003],
    [62311, 48017],
    [48871, 59263],
    [45949, 59497],
    [60919, 39239]
    ]

for pair in prime_list:
    q = pair[0]
    p = pair[1]

    #RSA Algorithm

    #create 3 messages, one small, one medium, one large
    print("This is our large prime (p):", p)
    print("This is our large prime (q):", q)
    upper_bound = q//3
    m1 = secrets.randbelow(upper_bound - 1) + 1
    print("This is our first secret message (m1):", m1)

    upper_bound = 2*(q//3)
    lower_bound = q//3
    m2 = secrets.randbelow(upper_bound - lower_bound) + lower_bound
    print("This is our second secret message (m2):", m2)

    upper_bound = q
    lower_bound = 2*(q//3)
    m3 = secrets.randbelow(upper_bound - lower_bound) + lower_bound
    print("This is our third secret message (m3):", m3)

    #compute other values
    n = p * q
    print(" ")
    print("Public value n (product of primes):", n)
    k = (p - 1)*(q - 1) #this value is kept private
    print("This is the private value k:", k)
    for e in range(2, k): 
        if math.gcd(e, k) == 1:
            print("Public value e (exponent):", e)
            break
    d = pow(e, -1, k) #this is the private key

    #Ecryption
    encrypt_m1 = pow(m1, e, n) #encoded ciphertext
    print() 
    print("This is the first encoded message (m1):", encrypt_m1)
    print()

    encrypt_m2 = pow(m2, e, n) #encoded ciphertext
    print() 
    print("This is the second encoded message (m2):", encrypt_m1)
    print()

    encrypt_m3 = pow(m3, e, n) #encoded ciphertext
    print()
    print("This is the thrid encoded message (m3):", encrypt_m1)
    print()

    #Decrypion
    decrypt_m1 = pow(encrypt_m1, d, n)
    print("This is the first decoded message (m1):", decrypt_m1)
    print()

    decrypt_m2 = pow(encrypt_m2, d, n)
    print("This is the second decoded message (m2):", decrypt_m2)
    print()

    decrypt_m3 = pow(encrypt_m3, d, n)
    print("This is the third decoded message (m3):", decrypt_m3)
    print()

    #Brute Force Attack
    print("Let's conduct a brute force attack...")
    start_time = time.time()
    for guess in range (n):
        if pow(guess, e, n) == m1:
            print("The hacker says the first message is", guess)
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m1, "took", time_elapsed, "seconds to crack!")
            break
    for guess in range (n):
        if pow(guess, e, n) == m2:
            print("The hacker says the second message is", guess)
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m2, "took", time_elapsed, "seconds to crack!")
            break
    for guess in range (n):
        if pow(guess, e, n) == m3:
            print("The hacker says the third message is", guess)
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m3, "took", time_elapsed, "seconds to crack!")
            break
    print("!" * 100)
    print()
            
