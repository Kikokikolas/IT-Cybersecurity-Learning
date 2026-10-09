import string

hex_encoded = input("Texto hexadecimal: ").strip()
xored = bytes.fromhex(hex_encoded).decode("utf-8")

# Recupera os primeiros quatro caracteres da chave.
prefixo = "THM{"
inicio_key = "".join(
    chr(ord(xored[i]) ^ ord(prefixo[i]))
    for i in range(4)
)

# Experimenta cada possibilidade para o quinto carácter.
for ultimo in string.ascii_letters + string.digits:
    key = inicio_key + ultimo

    flag = "".join(
        chr(ord(caracter) ^ ord(key[i % 5]))
        for i, caracter in enumerate(xored)
    )

    print(f"Chave: {key!r} → Flag: {flag!r}")