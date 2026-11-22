#!/usr/bin/env python3
"""
RC4 Implementation for Lab Testing
"""

class RC4:
    def __init__(self, key):
        self.key = key
        self.S = list(range(256))
        self._ksa()
        self.i = 0
        self.j = 0
    
    def _ksa(self):
        """Key Scheduling Algorithm"""
        j = 0
        key_len = len(self.key)
        for i in range(256):
            j = (j + self.S[i] + self.key[i % key_len]) & 0xFF
            self.S[i], self.S[j] = self.S[j], self.S[i]
    
    def _prga(self):
        """Pseudo-Random Generation Algorithm - returns one byte"""
        self.i = (self.i + 1) & 0xFF
        self.j = (self.j + self.S[self.i]) & 0xFF
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
        return self.S[(self.S[self.i] + self.S[self.j]) & 0xFF]
    
    def encrypt(self, data):
        """Encrypt/decrypt data using RC4 (symmetric)"""
        keystream = bytes([self._prga() for _ in range(len(data))])
        return bytes([data[i] ^ keystream[i] for i in range(len(data))])
    
    def decrypt(self, data):
        """Decrypt data using RC4 (same as encrypt)"""
        return self.encrypt(data)

def test_rc4():
    print("=" * 50)
    print("TESTING RC4")
    print("=" * 50)
    
    # RC4 key can be any length (1-256 bytes)
    key = b"my_secret_key_12345"
    
    print(f"Key: {key}")
    print("⚠️  RC4 is DEPRECATED! Don't use for production.")
    
    cipher = RC4(key)
    
    plaintext = b"salam"
    print(f"Plaintext: {plaintext}")
    
    ciphertext = cipher.encrypt(plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    # Reset the cipher state for decryption
    cipher = RC4(key)
    decrypted = cipher.decrypt(ciphertext)
    print(f"Decrypted: {decrypted}")
    
    assert plaintext == decrypted
    print("✓ RC4 test passed!")

if __name__ == "__main__":
    test_rc4()
