# MD5 and SHA-1

A hash is often used like a digital fingerprint. If an attacker can create a harmless-looking file and a malicious file with the same hash, a system that trusts that hash may mistake one for the other. This is especially dangerous for digital signatures and for verifying important files.

- **MD5:** Collisions can be created very easily with modern techniques.
- **SHA-1:** It is stronger than MD5, but practical collisions have also been demonstrated.

Think of a hash as a machine that turns data into a short fingerprint. Because there are far more possible inputs than fingerprints, different inputs must sometimes share a fingerprint. That is called a **collision**.

The security goal is to make it infeasible to deliberately find a collision. Weaknesses in MD5 and SHA-1 let researchers find collisions much faster than simply trying random files.

### A Simplified Example of the Risk

1. Someone digitally signs a document. The signature is made over the document’s hash.
2. An attacker creates a different document with the same hash.
3. A system checking the signature may accept the second document because its hash matches the one that was signed.

Finding such a match is not usually as simple as changing one word in a file. Collision techniques exploit the hash algorithm’s structure and carefully construct inputs. The demonstrated attacks on MD5 and SHA-1 make them unsuitable for uses where collision resistance matters.
