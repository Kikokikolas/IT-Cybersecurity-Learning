"""Experimenta automaticamente chaves no laboratório W1seGuy."""

import argparse
import re
import socket
import string
import time


ALPHABET = string.ascii_letters + string.digits
PROMPT = b"What is the encryption key?"


def is_rejection(message):
    return any(text in message for text in (
        "Close but no cigar", "THM{Try_Again}", "Nope nope nope"
    ))


def is_success(message):
    if is_rejection(message):
        return False
    return "Congrats! That is the correct key!" in message or bool(
        re.search(r"THM\{[^{}\r\n]+\}", message)
    )


def attempt(host, port, last_character):
    with socket.create_connection((host, port), timeout=10) as connection:
        banner = b""
        while PROMPT not in banner:
            chunk = connection.recv(4096)
            if not chunk:
                raise ValueError("O servidor fechou antes de pedir a chave.")
            banner += chunk
            if len(banner) > 65536:
                raise ValueError("A mensagem do servidor excedeu o tamanho esperado.")

        match = re.search(rb"flag 1:\s*([0-9a-fA-F]+)\s*\r?\n", banner)
        if not match:
            raise ValueError("Não encontrei o hexadecimal na mensagem.")
        xored = bytes.fromhex(match.group(1).decode("ascii")).decode("utf-8")
        if len(xored) < 4:
            raise ValueError("O texto cifrado é demasiado curto.")

        prefix = "".join(chr(ord(xored[i]) ^ ord(c)) for i, c in enumerate("THM{"))
        if any(c not in ALPHABET for c in prefix):
            raise ValueError("A chave recuperada não corresponde ao formato esperado.")
        key = prefix + last_character
        connection.sendall((key + "\n").encode("utf-8"))

        response = b""
        while True:
            chunk = connection.recv(4096)
            if not chunk:
                break
            response += chunk
            if len(response) > 65536:
                raise ValueError("A resposta excedeu o tamanho esperado.")

    message = response.decode("utf-8", errors="replace").strip()
    success = is_success(message)
    flag = "".join(chr(ord(c) ^ ord(key[i % 5])) for i, c in enumerate(xored))
    return key, message, success, flag


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="10.128.178.141")
    parser.add_argument("--port", type=int, default=1337)
    parser.add_argument("--attempts", type=int, default=310)
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error("--attempts deve ser pelo menos 1")

    print("A chave muda em cada ligação: cada tentativa tem uma hipótese em 62.", flush=True)
    for number in range(args.attempts):
        try:
            key, message, success, flag = attempt(
                args.host, args.port, ALPHABET[number % len(ALPHABET)]
            )
        except (OSError, ValueError) as error:
            print(f"Erro: {error}", flush=True)
            return 1
        print(f"[{number + 1}/{args.attempts}] Chave {key!r}: {message}", flush=True)
        if success:
            print(f"Flag 1: {flag}", flush=True)
            return 0
        if not is_rejection(message):
            print("Resposta sem confirmação de sucesso; a continuar.", flush=True)
        time.sleep(0.2)

    print("Limite atingido. Como a chave muda, percorrer os 62 caracteres não garante acertar.")
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nInterrompido.")
        raise SystemExit(130)
