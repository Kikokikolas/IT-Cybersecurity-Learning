# HMACs and Digital Signatures

## 1. HMAC (Hash-based Message Authentication Code)

An HMAC computes a keyed hash using a shared secret key and a hash function (such as HMAC-SHA256):

### How It Works

Both sender and receiver share the same secret key. The sender computes `HMAC(secret_key, message)` and sends the message along with that tag. When the receiver gets it, they recompute `HMAC(secret_key, message)` locally and compare the two tags (using constant-time comparison!).

### Why Not Just `HASH(secret_key + message)`?

Naive concatenation can run into subtle structural flaws (like length-extension attacks on certain hash constructions). HMAC uses a carefully structured two-pass hash design with the key that avoids those pitfalls.

### Examples

- Webhooks (e.g., payment or repository events where the receiver verifies an `X-Signature` header using a shared webhook secret).

- API request signing and JWTs (HS256) where a single backend or trusted parties hold the symmetric secret.

**Limitation:** Because both sides share the same secret key, anyone who can verify an HMAC also has the key needed to forge a valid one—so HMACs don't give non-repudiation (proving to a third party that only one specific party could have signed it).

## 2. Digital Signatures (Hash-and-Sign)

Digital signatures use asymmetric cryptography (a private key to sign and a public key to verify), with hashing playing a crucial supporting role:

### How It Works

1. **Hash first:** Compute a compact digest of the message, e.g., `digest = SHA-256(message)`.

2. **Sign the digest:** Use the sender's private key to create the signature over that digest.

3. **Verify:** Anyone with the sender's public key hashes the received message to get the digest and checks that the signature matches the digest under that public key.

### Why Hash First Instead of Signing the Whole Message Directly?

Public-key operations are much slower than hashing and often have strict input size limits. Hashing a 500 MB release or contract down to a 256-bit digest lets you sign a tiny, fixed-size value while binding the entire file.

### Examples

Software releases/packages, TLS certificates, code commits, legal/financial documents, and blockchain transactions.
