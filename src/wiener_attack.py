"""
Date: 07/14/2025

Implementation of Weiner's Attack
    Runs multiple trials of attack with different d values (some small, some large)
    to see where Weiner's Attack is effective and where it is not
"""


import math
import secrets
import time
from fractions import Fraction

# ======== Prime Generation and Miller-Rabin Test ========
def prime_check(n, i=10): 
    if n in (2, 3): return True
    if n <= 1 or n % 2 == 0: return False
    s, r = 0, n - 1
    while r % 2 == 0:
        r //= 2
        s += 1
    for _ in range(i):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == 1: return False
                if x == n - 1: break
            else: return False
    return True

def prime_candidate(bits):
    q = secrets.randbits(bits)
    q |= (1 << (bits - 1)) | 1
    return q

def generate_prime(bits=32):
    while True:
        candidate = prime_candidate(bits)
        if prime_check(candidate, 64):
            return candidate

# ======== Wiener's Attack Components ========
#Computes the continued fracton of e/N
def continued_fraction(e, n):
    cf = []
    while n:
        a = e // n
        cf.append(a)
        #Euclidean Algorithm
        temp = e
        e = n
        n = temp - a * n

    return cf

#Computes all convergents of the continued fraction
def convergents(cf):
    convs = []
    for i in range(len(cf)):
        frac = Fraction(cf[i])
        for j in reversed(cf[:i]):
            frac = 1 / frac + j
        convs.append((frac.numerator, frac.denominator))
    return convs

#Value-Check for Weiner's Attack Test #3 (does the quad.eq. have rational roots?)
def is_perfect_square(n):
    if n < 0: return False
    root = math.isqrt(n)
    return root * root == n

#Value-Check for Weiner's Attack Test
def valid_kd_pair(k, d, e, n):
    if k == 0: return False
    phi_candidate = (e * d - 1) // k #check 1
    s = n - phi_candidate + 1 #check 2
    discr = s * s - 4 * n
    return discr >= 0 and is_perfect_square(discr) #check 3, uses is_perfect_square function to verify pass/fail

def wiener_attack(e, n):
    cf = continued_fraction(e, n) #Input values e and n to expand continued fraction
    convs = convergents(cf) #Get convergents of that fraction
    for k, d in convs: 
        if k == 0 or (e * d - 1) % k != 0: #Check if values satisfy RSA basic tests
            continue
        if valid_kd_pair(k, d, e, n): #Run Weiner's Attack Tests
            return d
    return None

# ======== RSA Trials with Attack and Timing ========
def run_trials(num_trials = 15, bits = 32):
    print(f"Running {num_trials} attack trials...\n")
    for i in range(num_trials):
        print(f"--- Trial {i + 1} ---")
        p = generate_prime(bits)
        q = generate_prime(bits)
        n = p * q
        phi = (p - 1) * (q - 1)

        # First e value: small
        while True:
            upper_bound = phi // 3
            e1 = secrets.randbelow(upper_bound - 1) + 1
            if math.gcd(e1, phi) == 1:
                d1 = pow(e1, -1, phi)
                break

        # Second e value: medium
        while True:
            lower_bound = phi // 3
            upper_bound = 2 * (phi // 3)
            e2 = secrets.randbelow(upper_bound - lower_bound) + lower_bound
            if math.gcd(e2, phi) == 1:
                d2 = pow(e2, -1, phi)
                break

        # Third e value: large
        while True:
            lower_bound = 2 * (phi // 3)
            upper_bound = phi
            e3 = secrets.randbelow(upper_bound - lower_bound) + lower_bound
            if math.gcd(e3, phi) == 1:
                d3 = pow(e3, -1, phi)
                break

        # Encrypt/decrypt a random message
        m = secrets.randbelow(n)
        c1 = pow(m, e1, n)
        c2 = pow(m, e2, n)
        c3 = pow(m, e3, n)

        decrypted_e1 = pow(c1, d1, n)
        decrypted_e2 = pow(c2, d2, n)
        decrypted_e3 = pow(c3, d3, n)

        # Attack e1
        e1_start = time.time()
        recovered_d1 = wiener_attack(e1, n)
        e1_end = time.time()
        e1_elapsed = e1_end - e1_start
        if recovered_d1 == d1:
            print("Weiner's Attack = SUCCESSFUL")
            print("It took", e1_elapsed, "seconds to crack the code with e-value", e1, "and d-value", d1)
        else:
            print("Weiner's Attack = FAILURE")
            print("It took", e1_elapsed, "seconds for the attack to fail with e-value", e1, "and d-value", d1)

        # Attack e2
        e2_start = time.time()
        recovered_d2 = wiener_attack(e2, n)
        e2_end = time.time()
        e2_elapsed = e2_end - e2_start
        if recovered_d2 == d2:
            print("Weiner's Attack = SUCCESSFUL")
            print("It took", e2_elapsed, "seconds to crack the code with e-value", e2, "and d-value", d2)
        else:
            print("Weiner's Attack = FAILURE")
            print("It took", e2_elapsed, "seconds for the attack to fail with e-value", e2, "and d-value", d2)

        # Attack e3
        e3_start = time.time()
        recovered_d3 = wiener_attack(e3, n)
        e3_end = time.time()
        e3_elapsed = e3_end - e3_start
        if recovered_d3 == d3:
            print("Weiner's Attack = SUCCESSFUL")
            print("It took", e3_elapsed, "seconds to crack the code with e-value", e3, "and d-value", d3)
        else:
            print("Weiner's Attack = FAILURE")
            print("It took", e3_elapsed, "seconds for the attack to fail with e-value", e3, "and d-value", d3)


        print("-" * 50 + "\n")


# ======== Run the Demo ========
run_trials()
