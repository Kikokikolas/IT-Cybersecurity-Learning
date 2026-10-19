ECC is a family of cryptographic techniques based on the mathematical properties of elliptic curves.

The technique I explored in more detail was **ECDH (Elliptic Curve Diffie–Hellman)**. It allows two people to establish a shared secret over a public network without sending the secret itself. This secret is then used to **derive symmetric keys**, which can encrypt and decrypt data using an algorithm such as AES.

The mathematics behind it works as follows:

Both people use the same elliptic curve and a publicly known base point called **G**. Each person generates a private key and calculates a corresponding public key.

| | Alice | Bob |
|---|---|---|
| Private key — kept secret | `a` | `b` |
| Public key — shared openly | `A = aG` | `B = bG` |

The private keys are numbers, while the public keys are points on the curve. Here, `aG` means **scalar multiplication**: adding the point `G` to itself according to the curve’s mathematical rules.

Alice and Bob exchange their public keys. Each then combines their own private key with the other person’s public key:

```text
Alice calculates: S = aB
Bob calculates:   S = bA
```

Both obtain the same shared point because:

```text
aB = a(bG) = abG
bA = b(aG) = abG

Therefore: aB = bA
```

For a small demonstration, imagine that Alice’s private key is `3` and Bob’s private key is `5`:

```text
Alice's public key: A = 3G
Bob's public key:   B = 5G

Alice calculates: 3(5G) = 15G
Bob calculates:   5(3G) = 15G
```

These small numbers are only for illustration. Real implementations use very large private values. An observer can see the public points `G`, `A`, and `B`, but recovering the private keys from them is computationally infeasible with appropriate parameters and known classical methods.

The shared point provides secret material that is processed by a **key derivation function (KDF)** to produce symmetric keys:

```text
ECDH → shared secret → key derivation → symmetric keys → encrypted data
```

**ECDHE** is the ephemeral version of ECDH. It uses temporary key pairs, typically generated for a connection’s handshake rather than for every message.

ECDH alone does not authenticate the other person. Protocols such as TLS combine key agreement with authentication to protect against impersonation.

## From ECDHE to Encrypted Data

Both sides calculate the shared secret locally. Each side needs **its own private key and the other side's public key**, using the same curve parameters:

```text
Alice: Alice's private key × Bob's public key → shared secret
Bob:   Bob's private key × Alice's public key → same shared secret
```

Only the public keys are exchanged over the network. The private keys remain on their respective devices. Neither side needs to send the shared secret.

A **key derivation function (KDF)** then uses the shared secret and information about the connection to derive symmetric keys. Both sides use the same inputs and derive the same keys locally, so these keys do not need to be sent over the network either.

In TLS, separate keys protect each direction:

- Alice uses one key to encrypt data sent to Bob, and Bob uses that key to decrypt it.
- Bob uses another key to encrypt data sent to Alice, and Alice uses that key to decrypt it.

Algorithms such as **AES-GCM** or **ChaCha20-Poly1305** use these keys to encrypt and authenticate the data exchanged over the connection, including HTTP requests and responses.

```text
ECDHE → both sides calculate the same shared secret
KDF   → both sides derive the same symmetric keys
AES-GCM or ChaCha20-Poly1305 → protect the actual data
```

The ephemeral key pairs are temporary: in a typical TLS handshake using ECDHE, each side generates a pair for that handshake, not for every HTTP request. The temporary private keys should be erased once they are no longer needed. Public keys do not need to be erased for secrecy. The derived symmetric keys continue to protect the connection until they are replaced or discarded.
