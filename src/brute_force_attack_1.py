#06/02/2025
#First brute force attacks: runs through all possible answers for m until it gets the right one

import math
import time
import secrets

#Manullly input a prime number
p = int(input("Enter a prime number p: "))

q = int(input("Enter a prime number q: "))

m = int(input("Enter your message: "))

if m >= q:
    print("Your message must be less than q!")
else:
    #Calculate RSA numbers
    n = p * q #this is a public value
    print("Public value n:", n)
    k = (p - 1)*(q - 1)
    for d in range(2, k): 
        if math.gcd(d, k) == 1: #this is a public value
            print("Public value d:", d) 
            break

#Encryption
e = pow(m, d, n)
print("This is the encoded message:", e)

#Decryption
d_inverse = pow(d, -1, k)
decoded_message = pow(e, d_inverse, n)
print("Here is the decoded message:", decoded_message)

#Brute Force Attack: runs through all possible messages (m) thinks about the bound and encodes until it gets (e).
start_time = time.time()
for guess in range (n):
    if pow(guess, d, n) == e:
        print("The original message is", guess)
        break
end_time = time.time()
time_elapsed = end_time - start_time
print("It took", time_elapsed, " seconds to decode the message!")