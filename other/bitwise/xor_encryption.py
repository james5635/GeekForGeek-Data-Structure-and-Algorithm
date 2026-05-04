def xor_encryption_encrypt(plaintext: str, key: int) -> str:
    """Encrypt plaintext using XOR with shifting key."""
    result = []
    for i, char in enumerate(plaintext):
        result.append(chr(ord(char) ^ (key + i)))
    return "".join(result)


def xor_encryption_decrypt(ciphertext: str, key: int) -> str:
    """Decrypt ciphertext using XOR with shifting key."""
    result = []
    for i, char in enumerate(ciphertext):
        result.append(chr(ord(char) ^ (key + i)))
    return "".join(result)


if __name__ == "__main__":
    encrypted = xor_encryption_encrypt("Hello", 5)
    print(encrypted)
    print(xor_encryption_decrypt(encrypted, 5))
