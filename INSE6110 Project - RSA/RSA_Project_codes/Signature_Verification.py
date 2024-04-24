# Square and multiply function
def square_multiply(base, exponent, MOD):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % MOD

        exponent = exponent // 2
        base = (base * base) % MOD

    return result

def signature_plaintext(S, e, N):
    decrypted_chunks = []

    for encrypted_value in S:
        decrypted_value = square_multiply(encrypted_value, e, N)
        hex_value = hex(decrypted_value)[2:]

        hex_value = '0' + hex_value if len(hex_value) % 2 == 1 else hex_value

        decrypted_chunks.append(''.join([chr(int(hex_value[i:i+2], 16)) for i in range(0, len(hex_value), 2)]))

    return ''.join(decrypted_chunks)

# N, e, and signature S values
N = int(input("Enter your Partner's N: "))
print("N =", N)
e = int(input("Enter your Partner's exponent: "))
print("e =", e)
S = [1061287228, 660577792, 621279061, 1403763239]
print("Signature, S =", S)
Signer = input("Signer Name: ")

# Decrypt the signature
Plaintext_Signature = signature_plaintext(S, e, N)
print("Decrypted Signature:", Plaintext_Signature)
if Signer == Plaintext_Signature:
    print("Signature Verified")
else:
    print("False signature")

