from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend
import math

messageA = b"I'll give you 500 and that's my last offer."
messageA_encrypted = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4" 
messageB = b"I'll give you 100 and that's my last offer."

def asInt(encodedStr: bytes) -> int:
  return int.from_bytes(encodedStr, byteorder='big', signed=False)

def findCipherText() -> bytes:
  # The general formula to derive the key stream, E(K,iv), given some
  # plaintext A and its corresponding ciphertext, E(A), is as follows:
  #   > E(K,iv) = A XOR E(A)
  keyStream = asInt(messageA) ^ asInt(messageA_encrypted)

  # Since the key stream was reused in a subsequent message, B, we can
  # now derive E(B), given B is known, like so:
  #   > E(B) = E(K,iv) XOR B
  messageB_encrypted = keyStream ^ asInt(messageB)

  # Return the derived ciphertext as bytes 
  return messageB_encrypted.to_bytes(
    math.ceil(messageB_encrypted.bit_length() / 8),
    byteorder='big'
  )

if __name__ == "__main__":
  print(findCipherText())