import hashlib

def avalancheCalculator(string1: str, string2: str) -> int:
  string1Hash = int( hashlib.sha256(string1.encode()).hexdigest(), 16 )
  string2Hash = int( hashlib.sha256(string2.encode()).hexdigest(), 16 )

  xor = string1Hash ^ string2Hash
  count = 0
  while (xor > 0):
    xor = xor & (xor - 1)
    count += 1

  return count


if __name__ == "__main__":
  print(avalancheCalculator("Hello World1", "Hello World2"))
