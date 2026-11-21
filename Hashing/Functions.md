# Hashing Functions

Hashing turns data of any size into a fixed-length result called a **hash** or **digest**. A hash function can turn a message or file into a short fingerprint.

## Fast Hashes vs. Password Hashes

General-purpose hash functions (e.g., SHA-256, SHA-3, and BLAKE3) are designed to be fast. That is useful for checksums, file integrity checks, and digital signatures, where hashing gigabytes of data quickly is an advantage. For passwords, speed is a liability because attackers with GPUs or ASICs can test billions of guesses per second.

Password-hashing functions such as Argon2id, bcrypt, and PBKDF2 are intentionally designed to make each password guess more expensive. They use a unique, random salt for each password, so identical passwords produce different stored results and precomputed attacks are less effective.

| Algorithm | Key design traits | Typical status / notes |
| --- | --- | --- |
| Argon2id | Memory-hard; configurable time, memory, and parallelism costs | Modern choice for password hashing; combines Argon2i and Argon2d approaches |
| bcrypt | Adjustable work factor; derived from the Blowfish design; has a 72-byte password input limit in common implementations | Well-established and still widely used |
| PBKDF2 | Applies a pseudorandom function (such as HMAC-SHA-256) repeatedly; not memory-hard | Widely supported, including in some FIPS-validated environments; less resistant to specialized hardware than memory-hard functions |

## What “Using Memory” Means in Argon2id

Imagine solving a puzzle using a giant whiteboard instead of a tiny notepad:

- **Large workspace (RAM allocation):** Argon2id fills a large area of memory with pseudorandom data derived from the password and salt.
- **Unpredictable memory access:** As it mixes data, Argon2id accesses different parts of that memory. This makes it difficult to reduce memory use without significantly increasing the computation required.
- **Cost of reducing memory:** If an attacker reduces the workspace or recomputes data instead of keeping it in memory, each guess takes longer. The memory required for each guess can also limit how many guesses can run in parallel.

A salt is normally public, unique for each password, and stored alongside the hash. It helps prevent precomputed attacks, such as rainbow-table lookups. A **pepper** is a secret kept separately from the password database, for example in a hardware security module or a protected environment variable. A pepper can add protection if the database is exposed, but it does not make password hashes impossible to crack offline.