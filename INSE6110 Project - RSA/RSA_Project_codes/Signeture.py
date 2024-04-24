def square_and_multiply(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2

    return result


def signeture(message, d, N):
    S = [square_and_multiply(ord(char), d, N) for char in message]
    return S


N = int(input("Enter your N: "))
d = int(input("Enter your d: "))

message = "Ovy"

#Signeture
S = signeture(message, d, N)
print("My Signeture:", S)
