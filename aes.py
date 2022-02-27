from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(key: bytes, plainText: str) -> tuple[bytes, bytes]:
  iv = urandom(16)
  encryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).encryptor()
  cipherText = encryptor.update(plainText.encode()) + encryptor.finalize()
  return (cipherText, iv)

def decrypt(key: bytes, cipherText: bytes , iv: bytes) -> str:
  decryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).decryptor()
  return (decryptor.update(cipherText) + decryptor.finalize()).decode()


if __name__ == "__main__":
  key = urandom(32)
  (cipherText, iv) = encrypt(key, input("Enter plaintext message: "))
  print(cipherText)
  plainText = decrypt(key, cipherText, iv)
  print(plainText)
