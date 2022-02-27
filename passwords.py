from os import urandom
from cryptography import exceptions
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def create(salt: bytes, password: str) -> bytes :
  derivFunc = Scrypt(salt=salt,
                  length=32,
                  n=2**14,
                  r=8,
                  p=1
  ) 
  return derivFunc.derive(password.encode())

def verify(salt: bytes, password: str, key: bytes) -> str:
  derivFunc = Scrypt(salt=salt,
                  length=32,
                  n=2**14,
                  r=8,
                  p=1
  ) 
  try: 
    derivFunc.verify(password.encode(), key)
  except exceptions.InvalidKey:
    return "Invalid password"
  return "Success"

if __name__ == "__main__":
  salt = urandom(16)
  key = create(salt, "password")
  password = str(input("Enter a password: "))
  result = verify(salt, password, key)
  print(result)