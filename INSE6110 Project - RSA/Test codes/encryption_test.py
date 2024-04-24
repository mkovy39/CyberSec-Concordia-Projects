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

# Encryption function
def encryption(m, e, N):
    message_chunks, hex_decimal_values, hex_texts = hexadecimal_conversion(m)
    encrypted_text = []

    for hex_value in hex_decimal_values:
        decimal = int(''.join(hex_value), 16)
        encrypted_msg = square_multiply(decimal, e, N)
        encrypted_text.append(encrypted_msg)

    return encrypted_text, message_chunks, hex_texts

# Decryption function
def decryption(C, d, N):
    decrypted_chunks = []

    for encrypted_value in C:
        decrypted_value = square_multiply(encrypted_value, d, N)
        hex_value = hex(decrypted_value)[2:]

        hex_value = '0' + hex_value if len(hex_value) % 2 == 1 else hex_value

        decrypted_chunks.append(''.join([chr(int(hex_value[i:i+2], 16)) for i in range(0, len(hex_value), 2)]))

    return ''.join(decrypted_chunks)

# N, e, d values from previous code, plaintext m chosen by you
N = 1674054013
e = 11
d = 1521792491
m = "comment ca va"
print("Plaintext, m =", m)

# Display the message chunks, hexadecimal values, and hexa text of the message
message_chunks, hex_values, hex_texts = hexadecimal_conversion(m)
print("Message Chunks:", message_chunks)

C, message_chunks, hex_texts = encryption(m, e, N)
print("Encrypted Message, C =", C)

# Decrypt the ciphertext
decrypted_message = decryption(C, d, N)
print("Decrypted Message:", decrypted_message)

