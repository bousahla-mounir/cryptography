#!/usr/bin/env python3
"""
ChaCha20 - Working with cryptography library (16-byte nonce)
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def test_chacha20_cryptography():
    print("=" * 50)
    print("CHACHA20 (cryptography library)")
    print("=" * 50)
    
    # 32-byte key (256-bit)
    key = os.urandom(32)
    
    # 16-byte nonce (128-bit) - REQUIRED for this library!
    nonce = os.urandom(16)
    
    print(f"Key:    {key.hex()}")
    print(f"Nonce:  {nonce.hex()}")
    print(f"Nonce length: {len(nonce)} bytes")
    
    cipher = Cipher(
        algorithms.ChaCha20(key, nonce),
        mode=None,
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    plaintext = b"salam"
    print(f"Plaintext:  {plaintext}")
    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    print(f"Ciphertext: {ciphertext.hex()}")
    
    # Decrypt
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    print(f"Decrypted:  {decrypted}")
    
    assert plaintext == decrypted
    print("✓ PASSED")

if __name__ == "__main__":
    test_chacha20_cryptography()
