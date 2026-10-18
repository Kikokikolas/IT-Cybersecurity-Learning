# Symmetric vs Asymmetric Cryptography

In **symmetric cryptography**, the same secret key is used to encrypt and decrypt data.

In **asymmetric cryptography**, a pair of mathematically related keys is generated: a public key and a private key. For asymmetric encryption, we use the recipient's public key to encrypt a message. The recipient then decrypts it using their private key.

Symmetric encryption is generally faster because it uses less computationally expensive operations. Asymmetric encryption is generally slower because its mathematical operations require more computation.

Some symmetric cryptographic algorithms are:

- AES (Advanced Encryption Standard)
- DES (Data Encryption Standard)
- 3DES (Triple DES)
- Blowfish
- Twofish
- IDEA (International Data Encryption Algorithm)
- RC4

Some asymmetric cryptographic algorithms and approaches are:

- RSA (Rivest–Shamir–Adleman)
- ECC (Elliptic Curve Cryptography), a family of techniques based on elliptic curves
- Diffie–Hellman (DH), used for key agreement
- DSA (Digital Signature Algorithm), used for digital signatures
- ElGamal

Asymmetric cryptography includes encryption, key agreement, and digital signatures; not every asymmetric algorithm encrypts messages.

The ones I have studied are AES, RSA, and ECC.
