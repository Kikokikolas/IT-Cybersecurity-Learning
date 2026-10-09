flag = "THM{thisisafakeflag}"
hex_encoded = input("Texto hexadecimal: ").strip()


# Desfaz .encode().hex()
xored = bytes.fromhex(hex_encoded).decode("utf-8")


if len(xored) != len(flag):
    print("O texto cifrado e a flag têm tamanhos diferentes.")
    print("Confirma se esta é mesmo a flag usada pelo servidor.")
else:
    chave_repetida = "".join(
        chr(ord(cifrado) ^ ord(original))
        for cifrado, original in zip(xored, flag)
    )

    print("Sequência recuperada:", repr(chave_repetida))