from hashlib import sha256
from random import choice
from string import ascii_lowercase

def HexBinSHA256(stringToConvert: str) -> tuple[str, str]:
  # The function should calculate the SHA256 value of stringToConvert
  # and convert the hex value to its binary representation
  hexValue = sha256(stringToConvert.encode()).hexdigest()
  asBinary = bin(int(hexValue, 16))
  return (hexValue, asBinary)

def bruteForcer(hexDigest: str) -> str:
  while True:
    attempt = ''.join(choice(ascii_lowercase) for i in range(5)) 
    hashVal = sha256(attempt.encode()).hexdigest()
    if hashVal == hexDigest:
      return attempt

if __name__ == "__main__":
  """
  1. Create a string, e.g. “hello world!”
  2. Call HexBinSHA256 to calculate its SHA256 value (hex and binary)
  3. Print the values
  """
  print(bruteForcer("94f94c9c97bfa92bd267f70e2abd266b069428c282f30ad521d486a069918925"))