from hashlib import sha256

def mine(hashDigest: str, difficulty: int) -> str:
  prefix = '0' * difficulty
  nonce = 0
  while True:
    attempt = sha256((hashDigest + hex(nonce)).encode()).hexdigest()
    if attempt[:difficulty] == prefix:
      return attempt
    nonce += 1

if __name__ == "__main__":
  hashDigest = "0b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf"
  result = mine(hashDigest, 6)
  print("New block found")
  print("Hash of current block:", result)
