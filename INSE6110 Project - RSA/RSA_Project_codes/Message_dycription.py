# Square and multiply function
def square_multiply(base, exponent, MOD):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % MOD

        exponent = exponent // 2
        base = (base * base) % MOD

    return result

def hexadecimal_conversion(m):
    chunk_length = 3
    small_chunks = []
    hex_values = []

    for x in range(0, len(m), chunk_length):
        chunk = m[x:x + chunk_length]
        small_chunks.append(chunk)

    hex_texts = []

    for chunk in small_chunks:
        hex_text = ''
        hexa_values = []

        for char in chunk:
            hex_decimal_value = hex(ord(char))[2:]
            hex_text += hex_decimal_value
            hexa_values.append(hex_decimal_value)

        hex_values.append(hexa_values)
        hex_texts.append(hex_text)

    return small_chunks, hex_values, hex_texts


def decryption(C, d, N):
    decrypted_chunks = []

    for encrypted_value in C:
        decrypted_value = square_multiply(encrypted_value, d, N)
        hex_value = hex(decrypted_value)[2:]

        hex_value = '0' + hex_value if len(hex_value) % 2 == 1 else hex_value

        decrypted_chunks.append(''.join([chr(int(hex_value[i:i+2], 16)) for i in range(0, len(hex_value), 2)]))

    return ''.join(decrypted_chunks)

# N, d, and ciphertext C values from previous code
N = int(input("Enter you N: "))
print("N = ", N)
d = int(input("Enter your d: "))
print("d = ", d)
C = [664073908, 1136298954, 656717155, 2439024693, 2111470193, 839808978, 1424047661, 11737518, 1821188533]
print("Ciphertext, C =", C)

# Decrypt the ciphertext
decrypted_message = decryption(C, d, N)
print("Decrypted Message:", decrypted_message)
