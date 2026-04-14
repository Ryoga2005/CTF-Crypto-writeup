time = 1770242615
ciphertext = "24823b2b2d104b36ad2078cafc8d98f22488e78df83b29f507d9b910ad51a464"

from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(ciphertext: str, timestamp: int) -> str:
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
    return unpad(decrypted, AES.block_size).decode()

plaintext = decrypt(ciphertext, time)
print(plaintext)
