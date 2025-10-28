def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypts/Decrypts a string using a Caesar Cipher."""
    if mode == 'decrypt':
        shift = -shift
        
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif 'a' <= char <= 'z':
            start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic chars unchanged
    return result

# Usage:
original_text = "Hello, Python World! 2025"
key = 3

encrypted = caesar_cipher(original_text, key)
decrypted = caesar_cipher(encrypted, key, mode='decrypt')

print(f"Original:  {original_text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
