from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_parameters, load_pem_public_key, load_pem_private_key
from dhCheck import dhCheckCorrectness 

dhParamsPem = b'-----BEGIN DH PARAMETERS-----\nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrAo8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n'  

antoniosKeyPem = b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n' 

def Diffie_Hellman():
  # Deserialize the given DH params and public key
  try:
    dhParams = load_pem_parameters(dhParamsPem)
    antoniosKey = load_pem_public_key(antoniosKeyPem)
  except ValueError:
    print("Decoding step failed - the program encountered an error in the PEM object")
  except UnsupportedAlgorithm:
    print("Decoding step failed - an unsupported key type was given")

  if not isinstance(antoniosKey, dh.DHPublicKey):
    raise ValueError("The key object obtained from the decoded PEM must be of type DHPublicKey. Key object of type", type(antoniosKey), "was rejected")

  # Use the DH params to generate a new key pair
  privateKey = dhParams.generate_private_key()
  publicKey = privateKey.public_key()

  # Perform the key exchange to obtain the shared key
  sharedKey = privateKey.exchange(antoniosKey)

  # Calculate derived key
  derivedKey = HKDF(
      algorithm=hashes.SHA256(), length=32,
      salt=None, info=b'handshake data'
  ).derive(sharedKey)

  # Convert public key to serializable PEM format
  publicKeyPem = publicKey.public_bytes(
    encoding=Encoding.PEM, 
    format=PublicFormat.SubjectPublicKeyInfo)

  return (publicKeyPem, derivedKey)

if __name__ == "__main__":
  print(Diffie_Hellman())