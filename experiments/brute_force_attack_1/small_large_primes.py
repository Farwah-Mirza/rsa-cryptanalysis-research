
"""
Date: 06/13/2025

This code is an attempt to generate primes and run through attack sequences on its own.
We also change the previous sequence so that we are generating multiple messages.
This code uses 1 large prime and 1 small prime.
"""

import math
import time
import secrets

prime_list = [
    [64483, 3],
    [52177, 5],
    [43597, 7],
    [36013, 11],
    [58907, 13],
    [62213, 43],
    [42557, 71],
    [33797, 97],
    [56569, 131],
    [61403, 157],
    [61651, 383],
    [58921, 727],
    [48163, 967],
    [60449, 1555]
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

    upper_bound = 2*(q//3)
    lower_bound = q//3
    m2 = secrets.randbelow(upper_bound - lower_bound) + lower_bound

    upper_bound = q
    lower_bound = 2*(q//3)
    m3 = secrets.randbelow(upper_bound - lower_bound) + lower_bound

    #compute other values
    n = p * q
    print(" ")
    k = (p - 1)*(q - 1) #this value is kept private
    for e in range(2, k): 
        if math.gcd(e, k) == 1:
            break
    d = pow(e, -1, k) #this is the private key
    print("This is our private d value:", d)

    #Ecryption
    encrypt_m1 = pow(m1, e, n) #encoded ciphertext
    encrypt_m2 = pow(m2, e, n) #encoded ciphertext
    encrypt_m3 = pow(m3, e, n) #encoded ciphertext

    #Decrypion
    decrypt_m1 = pow(encrypt_m1, d, n)
    decrypt_m2 = pow(encrypt_m2, d, n)
    decrypt_m3 = pow(encrypt_m3, d, n)

    #Brute Force Attack
    print("Let's conduct a brute force attack...")
    
    start_time = time.time()
    for guess in range (n):
        if pow(guess, e, n) == encrypt_m1:
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m1, "took", time_elapsed, "seconds to crack!")
            break

    start_time = time.time() 
    for guess in range (n):
        if pow(guess, e, n) == encrypt_m2:
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m2, "took", time_elapsed, "seconds to crack!")
            break

    start_time = time.time()   
    for guess in range (n):
        if pow(guess, e, n) == encrypt_m3:
            end_time = time.time()
            time_elapsed = end_time - start_time
            print("The message", m3, "took", time_elapsed, "seconds to crack!")
            break
    print("!" * 100)
    print()
            
