import math

def gcd(a, b):
    return math.gcd(a, b)

def inverse_mod(x, y):
    if gcd(x, y) != 1:
        return None
    u1, u2, u3 = 1, 0, x
    v1, v2, v3 = 0, 1, y
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % y

e = int(input("Enter the key, e : "))
phi_n = int(input("Enter Phi(N): "))

result = inverse_mod(e, phi_n)

if result is not None:
    print(f"The modular inverse of {e} mod {phi_n} is: {result}")
else:
    print(f"No modular inverse for {e} mod {phi_n}.")
