from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

if __name__ == "__main__":
  publicKey = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr0s4Ppf3cqrxgW44Mt08\nKQwcHrns8+FPRzi7gxvA/aoVHGweDJ76x479k7UEcEcPKWjv33vlZ9ipswMognNe\neiNmLTAw5oytBDLes2CtnRacxHdq3bB2Eq/n/3qzLTbm/EbiB0aIrEyfP/KQrbqR\npNb7aqlieW9YvGDIvQnVKb1sxOMATrJlA8xfpqa5Pu31GRnoWiZ1MCZ4u81+Mr54\nVQw6JiyXLXLA6t4UKbwOHYiSOxKmSOxDWTMcLtQ3Poh+dBMjawSv2i5kj7ECV24m\niQYUw26gRcTMwTrOPQXS+/kB4l/fEdU+WCRnJU2+L+pVvXY78m9BgnnSjJsK+boq\nzwIDAQAB\n-----END PUBLIC KEY-----\n".encode() 

  signature = "l\xf3\xb2\x12\x81\x9eO\xba\x06\xeaq\xd3xV\xf9\xa3/B\xad\xa0\xe6\x1ao\xdc\xa2\xee\x03\x84<;~\x99x\x94\x1d\x8c|\xd5\xb2\xb1n\xa3\x9a\xf5\xa3}q\xd2\xed\x8eQ\xb9\xd5$\r\xab:\x04y\x85f\xde\x1fk\xc18sH\x13\x02\xd3\xfc,\xd0\xee\x89\xe5\xa70\xa6\x1f\xc3\x05@P\xa8*\x98\xb2u_$\x87\xbd\t\x87N\x14\x97\xef\xa1O\xc8-[\x8fc\x1fft\xccH(\xbe\x18\xd5\xeaqO\x0bm\x95\xbc4 W\xa5\xd7\x11\xa1\xb8\xb9~\x03 xP\xbf\x10\x11y\x1aCtu\xc9\xd1?\\\xf8\xc7\xe0\xfc>e`\x9f\xb7} \x82cg4\x1f\xb8\x88\r\x8f\x1bg\x80\xb7<\xc2\xcb\x829zh\x86u\xe3c\x0f\x8a\xa8c\xa3\xa3\xcb\x1bZ\xc5\xfeE\xc0\xc30\xf8@\xc3\xf0\xca\xa2\x0f\xcb=)\xdc\xa1\x08\x19\xda\x0b\xbf\xd3zB\xfb7\xb2\x07\x80e\xf7=<\xd9u\x92\x93I\xf1\r\xecw\xf5|^\xca\xb0\xcfh\xfc5\xa92\x1e_\xadr\x9c`=p".encode() 

verified = publicKey.verify(
  signature,
  "It's-A Me, Mario!".encode(),
  padding.PSS(
    mgf=padding.MGF1(hashes.sha256()),
    salt_length=padding.PSS.MAX_LENGTH
  ),
  hashes.sha256()
)
