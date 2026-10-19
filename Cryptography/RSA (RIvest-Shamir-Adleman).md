# RSA (Rivest–Shamir–Adleman)

RSA is an asymmetric cryptographic algorithm that uses a public key and a private key. When encrypting a message for someone, we use the recipient's public key. The recipient uses their private key to decrypt it.

RSA also supports digital signatures through separate signature schemes, such as RSA-PSS.

## Key Generation

Choose two large, distinct prime numbers, `p` and `q`, and calculate:

```text
n = p × q
λ(n) = lcm(p − 1, q − 1)
```

Choose a public exponent `e` that is relatively prime to `λ(n)`, meaning `gcd(e, λ(n)) = 1`. Then calculate the private exponent `d` so that:

```text
(e × d) mod λ(n) = 1
```

This makes `d` the modular inverse of `e` modulo `λ(n)`.

| Value | Meaning | Visibility |
| --- | --- | --- |
| `p`, `q` | Prime factors of `n` | Secret |
| `n` | Modulus | Public |
| `e` | Public exponent | Public |
| `d` | Private exponent | Secret |

The public key is `(n, e)`. A basic representation of the private key is `(n, d)`; implementations typically also store the prime factors and other values to make calculations faster.

## Encryption and Decryption

The underlying mathematical operations are:

```text
Encryption: c = m^e mod n
Decryption: m = c^d mod n
```

- `m` is the message representative: an integer from `0` to `n − 1`.
- `c` is the ciphertext representative.
- `mod` means the remainder after division.
- `gcd` means greatest common divisor.
- `lcm` means least common multiple.

In practice, secure RSA encryption uses an encoding and padding scheme such as **RSA-OAEP** before applying the mathematical operation. The bare formulas alone are not secure encryption.

### Why Randomized Padding Matters

RSA-OAEP uses fresh randomness each time a message is encrypted. This means that encrypting the **same message with the same public key** produces different ciphertexts, provided the random seed differs.

```text
Same message + same public key + fresh random padding → different ciphertext
```

The recipient uses their private key to decrypt each ciphertext and removes the OAEP encoding to recover the same original message.

Raw RSA, without randomized padding, is deterministic: the same message and public key always produce the same ciphertext. It is the randomness in schemes such as OAEP that changes this behavior, not simply adding extra bytes.

## Small Example for Learning

These numbers are deliberately small and insecure. This example demonstrates the bare mathematical operations, without padding.

```text
p = 61
q = 53
n = 61 × 53 = 3233
λ(n) = lcm(60, 52) = 780

e = 17
d = 413

17 × 413 = 7021
7021 mod 780 = 1

Public key:  (3233, 17)
Private key: (3233, 413)

Message: m = 65
Encrypt: c = 65^17 mod 3233 = 2790
Decrypt: m = 2790^413 mod 3233 = 65
```

## RSA and Symmetric Encryption

RSA is not normally used to encrypt large files or entire conversations. In a hybrid encryption scheme, RSA-OAEP can protect a randomly generated symmetric key, while an algorithm such as AES-GCM protects the actual data.

In the older RSA key transport method used in TLS, the client instead encrypted a **premaster secret** with the server's RSA public key. Both sides then derived symmetric keys from that secret.

TLS 1.3 removed RSA key transport. RSA can still be used for authentication through digital signatures, while a method such as ECDHE establishes the shared secret.

```text
RSA encryption: public key encrypts → private key decrypts
RSA signatures: private key signs → public key verifies
ECDHE: both sides calculate a shared secret locally
```
