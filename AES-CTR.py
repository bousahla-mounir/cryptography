#!/usr/bin/env python3
"""
AES-CTR Implementation for Lab Testing
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class AESCTR:
    def __init__(self, key, nonce):
        self.key = key
        self.nonce = nonce
        self.cipher = Cipher(
            algorithms.AES(self.key),
            modes.CTR(self.nonce),
            backend=default_backend()
        )
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using AES-CTR (same as decrypt)"""
        encryptor = self.cipher.encryptor()
        return encryptor.update(plaintext) + encryptor.finalize()
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using AES-CTR (same as encrypt)"""
        decryptor = self.cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()

def test_aes_ctr():
    print("=" * 50)
    print("TESTING AES-CTR")
    print("=" * 50)
    
    # Generate random key (16 bytes = 128 bits)
    key = os.urandom(16)
    nonce = os.urandom(16)
    
    print(f"Key (hex):   {key.hex()}")
    print(f"Nonce (hex): {nonce.hex()}")
    print("Note: NONCE MUST BE UNIQUE for each encryption with the same key!")
    
    cipher = AESCTR(key, nonce)
    
    # CTR mode doesn't require padding!
    plaintext = b"salam"
    print(f"Plaintext: {plaintext}")
    
    ciphertext = cipher.encrypt(plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    decrypted = cipher.decrypt(ciphertext)
    print(f"Decrypted: {decrypted}")
    
    assert plaintext == decrypted
    print("✓ AES-CTR test passed!")

if __name__ == "__main__":
    test_aes_ctr()
