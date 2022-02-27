import string
import math

def encryptAffine(plainText, a: int, b: int):
  # Ensure positive a, b
  if a < 1 or b < 1:
    raise ValueError("`a` and `b` must be positive integers")

  # Check if `a` is set to an invalid value
  if math.gcd(a, 26) != 1:
    raise ValueError("The value of `a` must be coprime with 26")

  cipherText = ""
  for ch in plainText:
    if ch in string.ascii_uppercase:
      cipherText += string.ascii_uppercase[(a * string.ascii_uppercase.index(ch) + b) % 26]
    else:
      cipherText += ch

  return cipherText
  
if __name__ == "__main__":
  print(encryptAffine("HELLO WORLD", 1, 1))