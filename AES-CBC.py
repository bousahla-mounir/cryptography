#!/usr/bin/env python3
"""
AES-CBC Implementation for Lab Testing
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class AESCBC:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        )
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using AES-CBC"""
        encryptor = self.cipher.encryptor()
        
        # PKCS7 padding
        padding_len = 16 - (len(plaintext) % 16)
        plaintext_padded = plaintext + bytes([padding_len] * padding_len)
        
        return encryptor.update(plaintext_padded) + encryptor.finalize()
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using AES-CBC"""
        decryptor = self.cipher.decryptor()
        plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove PKCS7 padding
        padding_len = plaintext_padded[-1]
        return plaintext_padded[:-padding_len]

def test_aes_cbc():
    print("=" * 50)
    print("TESTING AES-CBC")
    print("=" * 50)
    
    # Generate random key (16 bytes = 128 bits)
    key = os.urandom(16)
    iv = os.urandom(16)
    
    print(f"Key (hex): {key.hex()}")
    print(f"IV (hex):  {iv.hex()}")
    
    cipher = AESCBC(key, iv)
    
    plaintext = b"salam"
    print(f"Plaintext: {plaintext}")
    
    ciphertext = cipher.encrypt(plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    decrypted = cipher.decrypt(ciphertext)
    print(f"Decrypted: {decrypted}")
    
    assert plaintext == decrypted
    print("✓ AES-CBC test passed!")

if __name__ == "__main__":
    test_aes_cbc()
