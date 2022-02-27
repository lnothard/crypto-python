from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt(plainText: str, publicKey: bytes) -> bytes:
  return publicKey.encrypt(
    plainText.encode(),
    padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )
  )

def decrypt(cipherText: bytes, privateKey: bytes) -> str:
  return privateKey.decrypt(
    cipherText,
    padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )
  ).decode()

if __name__ == "__main__":
  privateKey = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024
  )
  publicKey = privateKey.public_key()
  plainText = input("Enter plaintext message: ")
  cipherText = encrypt(plainText, publicKey)
  print(cipherText)
  print(decrypt(cipherText, privateKey))