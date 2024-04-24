import random
import math

#defining prime checking function
def prime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

#generating random prime p
while True:
    p = random.randint(32768, 65535)
    if prime(p):
        break

print("p = ", p)

#generating random prime q
while True:
    q = random.randint(32768, 65535)
    if prime(q) and q != p:
        break
print("q = ", q)

#calculating N
N = p * q
print("N = ", N)

#Calculating Phi of N
phi_N = (p-1) * (q-1)
print("phi_(N) = ", phi_N)

#Defining GCD check Function
def gcd(a, b):
   return math.gcd(a, b)

#generating e by checking the condition
while True:
    e = random.randint(2, 100)
    if gcd(e, phi_N) == 1:
        print("e = ", e)
        break

#Defining Multiplicative inverse function
def multiplicative_inverse(x, y):
    if gcd(x, y) != 1:
        return None
    u1, u2, u3 = 1, 0, x
    v1, v2, v3 = 0, 1, y
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % y

#Calculating d = e inverse mod phi of N
d = multiplicative_inverse(e, phi_N)

if d is not None:
    print("d = ", d)


