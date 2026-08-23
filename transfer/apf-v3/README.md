# Adversarial Puzzle Forge — V3 protected transfer

This directory contains the exact V3 source contents (49 files), preserved as an encrypted transfer package. The plaintext source is not stored on this public branch.

## Integrity

Encrypted payload SHA-256:
`3b3a0eca6ba2079e404dec3a71dbfa853965b6878ca40b7308e227306b057bbd`

The 49 extracted source files were verified against the original V3 archive before encryption.

## Reassemble

From this directory:

```bash
python reassemble.py
```

This creates:
`apf-v3-source.tar.xz.aes`

## Decrypt

OpenSSL:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 \
  -in apf-v3-source.tar.xz.aes \
  -out apf-v3-source.tar.xz
```

Enter the password supplied separately by the owner.

## Extract

```bash
mkdir apf-v3
tar -xJf apf-v3-source.tar.xz -C apf-v3
```

Do not commit the password to this repository.
