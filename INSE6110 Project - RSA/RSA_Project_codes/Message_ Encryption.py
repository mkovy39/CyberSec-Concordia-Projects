#Square and multiply function
def square_multiply(base, exponent, MOD):
    result = 1

    while exponent > 0:
        #if exponent is odd
        if exponent % 2 == 1:
            result = (result * base) % MOD

        #exponent divided by 2
        exponent = exponent // 2
        base = (base * base) % MOD
    return result

def hexadecimal_conversion(m):
    chunk_lenth = 3
    small_chunks = []
    hexa_value = []
    for x in range(0, len(m), chunk_lenth):
        chunk = m[x:x + chunk_lenth]
        small_chunks.append(chunk)

    print("Dividing m in m1, m2, m3, m4, & m5 ", small_chunks)

    for chunk in small_chunks:
        hexaText = ''

        for char in chunk:
            hexaDecimal_value = hex(ord(char))[2:]
            hexaText += hexaDecimal_value
        hexa_value.append(hexaText)

    return hexa_value

#message_encryption_with_chunk
def encryption(m, e, N):
    hexaDecimalValues = hexadecimal_conversion(m)
    encryptedText = []

    for hex_value in hexaDecimalValues:
        decimal = int(hex_value, 16)
        print(decimal)
        encryptedMsg = square_multiply(decimal, e, N)
        encryptedText.append(encryptedMsg)

    return encryptedText


#N, e value from my Partner, Plaintext Chosen by Me.
N = int(input("Enter Partners N: "))
print("N = ", N)
e = int(input("Enter Partners exponent: "))
print("e = ", e)
m = "comment ca va"
print("Main Message, m = ", m)

C = encryption(m, e, N)
print("Encrypted Message, C =", C)