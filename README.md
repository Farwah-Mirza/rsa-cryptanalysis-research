# RSA Cryptanalysis Research

**Undergraduate Research Project | Benedictine University | May–August 2025**

An undergraduate research project investigating the security of the RSA public-key cryptosystem through implementation, cryptanalysis, and experimental analysis.

**Research Advisor:** Dr. Ellen Ziliak

---

## Overview

RSA is a public-key cryptosystem whose security relies on the computational difficulty of certain mathematical problems, particularly the difficulty of factoring large composite numbers.

During this summer research project, I implemented an RSA encryption-decryption scheme in Python and performed cryptanalysis against the implementation to investigate how different RSA parameters affect system security and attack performance.

My research focused on three attacks:

1. **Brute Force Attack #1** — attempts to recover the plaintext by testing possible message values.
2. **Factorization-Based Attack (Brute Force Attack #2)** — searches for the prime factors of `n` in order to recover information needed to decrypt the message.
3. **Wiener's Attack** — exploits RSA systems using sufficiently small private exponent values.

Experimental analysis was conducted to investigate the effects of prime size, message size, and RSA parameters on attack runtime.

---

## Research Objectives

The primary objectives of this research were to:

- Implement the RSA encryption-decryption scheme in Python.
- Implement the Miller-Rabin primality test for generating large prime numbers.
- Develop and test multiple cryptanalytic attacks against the RSA implementation.
- Investigate how RSA parameters affect the effectiveness and runtime of attacks.
- Analyze experimental results and identify unexpected relationships between RSA parameters and attack performance.
- Explore potential directions for future research in cryptographic security.

---

## RSA Implementation

The RSA implementation includes:

- RSA key generation
- Prime number generation
- Miller-Rabin probabilistic primality testing
- RSA encryption
- RSA decryption

The Miller-Rabin primality test was used to generate larger prime values for experiments rather than relying solely on manually selected primes.

### Miller-Rabin Primality Testing

Prime generation is an important component of RSA key generation. The project implemented the Miller-Rabin primality test to probabilistically determine whether generated numbers were prime.

The research also examined the relationship between the Miller-Rabin test and Fermat's Little Theorem, including the vulnerability of Fermat-based primality testing to pseudoprimes such as Carmichael numbers.

---

## Cryptanalysis

### 1. Brute Force Attack #1

The first attack attempts to recover the plaintext by iterating through possible message values and encrypting each candidate.

If the resulting ciphertext matches the observed ciphertext, the corresponding message has been recovered.

Initial experiments demonstrated that RSA implementations using very small prime values were highly vulnerable to this approach.

The experiment was then repeated using progressively larger prime values to investigate the relationship between prime size and attack runtime.

---

### 2. Factorization-Based Attack

The second attack searches for the prime factors of `n`.

Once the factors `p` and `q` are recovered, additional RSA parameters can be calculated and the private key can be reconstructed, allowing the original message to be decrypted.

This attack was used in experiments investigating whether message size affected the time required to compromise the RSA system.

---

### 3. Wiener's Attack

Wiener's Attack targets RSA implementations that use an unusually small private exponent `d`.

The attack uses the public RSA values `e` and `n` and applies continued fractions to identify candidates for the private key components.

Candidate convergents are tested to determine whether they produce valid RSA parameters and recover the original factors of `n`.

In our experiments, Wiener's Attack recovered vulnerable RSA configurations significantly faster than the brute-force approaches investigated in this project.

---

## Experimental Analysis

Several experiments were conducted to investigate relationships between RSA parameters and cryptanalytic attack performance.

### Brute Force Attack #1

Experiments investigated:

- **Prime size:** Comparing systems using small and large prime values.
- **Two large primes:** Investigating the effect of using large values for both `p` and `q`.
- **Message size:** Testing whether different plaintext sizes affected attack runtime.

### Factorization-Based Attack

An experiment investigated whether message size affected the runtime required to factor `n` and recover the message.

Three message ranges were tested:

- `m₁`: `1` to `q/3`
- `m₂`: `q/3` to `2q/3`
- `m₃`: `2q/3` to `q`

### Wiener's Attack

Experiments investigated the relationship between RSA parameters and the runtime of Wiener's Attack, including the effects of:

- Prime size
- Message size
- Public exponent `e`
- Private exponent `d`

---

## Key Findings

### Prime Size and Brute Force

Increasing the size of the RSA primes substantially increased the runtime of the first brute-force attack in our implementation.

When very small primes were used, the plaintext could be recovered extremely quickly. Increasing the prime size from 16-bit to 32-bit and eventually 64-bit values made the attack substantially more time-consuming.

### Message Size

The experiments did not demonstrate a clear relationship between message size and attack runtime.

For the factorization-based attack, messages from different ranges of possible plaintext values required approximately similar amounts of time to compromise.

This result differed from the initial hypothesis and motivated further questions about which RSA parameters actually influence the runtime of this attack.

### Wiener's Attack

In our experiments, Wiener's Attack was significantly faster than the brute-force approaches when the RSA system used a sufficiently small private exponent.

Increasing the prime sizes did not have the same effect on Wiener's Attack runtime as it did on the brute-force attacks.

These results demonstrate that increasing key parameters alone does not necessarily protect an RSA implementation from every form of cryptanalysis; appropriate parameter selection is also important.

---

## Research Materials

### Code

The [`src/`](src/) directory contains the primary RSA implementation and cryptanalysis attacks.

### Experiments

The [`experiments/`](experiments/) directory contains the code used to investigate specific RSA variables and attack performance.

### Results

The [`results/`](results/) directory contains the experimental data and results.

### Research Report

The [research report](research/summer_research_essay_report.pdf) documents the methodology, mathematical background, experiments, and results of the project.

### Research Poster

The research was presented at the **Undergraduate Research, Scholarship and Arts (URSA) Conference in April 2026**.

The [research poster](research/rsa_cryptanalysis_research_poster.pdf) is available here.

---

## Technologies

- Python
- RSA
- Public-Key Cryptography
- Number Theory
- Miller-Rabin Primality Testing
- Cryptanalysis
- Continued Fractions
- Experimental Data Analysis

---

## Future Work

Future research could investigate modifications to RSA and alternative cryptographic approaches designed to address emerging threats, including those associated with quantum computing.

Potential areas of investigation include post-quantum cryptography and cryptographic systems that do not rely on the mathematical assumptions underlying traditional RSA.

---

## References

Research sources and references are available in the [`references/`](references/) directory.

For additional details about the methodology, mathematical background, experiments, and results, see the [research report](research/rsa_cryptanalysis_research_report.pdf).