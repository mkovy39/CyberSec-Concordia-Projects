import random

def prime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

while True:
    p = int(input("enter your number: "))
    if prime(p):
        print("its a prime", p)
        break
    else:
        print("Its not prime", p)
        break