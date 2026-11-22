# Key Derivation Functions: HKDF

Often you don't start with a human password—you start with a high-entropy secret (like a shared Diffie-Hellman key in TLS or a master root key) and need one or more clean, independent cryptographic keys (for example, one key to encrypt messages and another key to authenticate them).

HKDF (HMAC-based Extract-and-Expand Key Derivation Function) is the standard way to turn an existing secret into specific keys safely.

## How HKDF Works: Extract and Expand

HKDF splits key derivation into two distinct phases using an HMAC (such as HMAC-SHA256):

### 1. Extract

```text
HKDF-Extract(salt, input_key_material) → PRK (Pseudorandom Key)
```

- Takes your raw input keying material (IKM) and an optional salt.

- Condenses/distills them into a fixed-length pseudorandom key (PRK) of uniform cryptographic strength.

**Why it matters:** Raw secrets (like a Diffie-Hellman shared secret) might not be uniformly distributed across all bits. Extraction concentrates that entropy into a clean key.

### 2. Expand

```text
HKDF-Expand(PRK, info, length) → OKM (Output Keying Material)
```

- Takes the PRK, a context/application label (`info`), and the desired output byte length.

- Produces as many pseudorandom key bytes as you ask for (up to HKDF's standard limit).

**Why `info` matters (domain separation):** Passing a distinct info string like `"chat-encryption-key"` vs. `"chat-mac-key"` ensures two keys derived from the same master secret are completely independent. If one leaks or is used in a wrong context, it doesn't directly compromise the other.

## Comparison

- **HKDF:** derives keys from secret material that is already strong.
- **Argon2id / PBKDF2:** makes password verification costly to help protect stored passwords.

## Examples

### HKDF — TLS 1.3

When your browser connects securely to a website, the two sides establish shared secret material during the handshake. TLS 1.3 uses HKDF to derive separate keys for encrypting traffic in each direction. HKDF is deriving keys from an existing secret, not storing a password.

### Argon2id — app password storage

When you create an account, an app can process your password with Argon2id and a unique salt, then store the resulting hash and its parameters—not your original password. At login, it checks the password you enter against that stored hash.

### PBKDF2 — WPA2-Personal Wi-Fi

A WPA2-Personal network uses PBKDF2 with the Wi-Fi passphrase and network name (SSID) to derive key material for securing the connection. PBKDF2 is also used in some systems for password storage and password-based encryption.
