from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# key generation Alice
privatekey = RSA.generate(2048)
f = open('KeyFile/aliceprivatekey.txt', 'wb')
f.write(bytes(privatekey.exportKey()))
f.close()
publickey = privatekey.publickey()
f = open('KeyFile/alicepublickey.txt', 'wb')
f.write(bytes(publickey.exportKey()))
f.close()

# key generation Bob
privatekey = RSA.generate(2048)
f = open('KeyFile/bobprivatekey.txt', 'wb')
f.write(bytes(privatekey.exportKey()))
f.close()
publickey = privatekey.publickey()
f = open('KeyFile/bobpublickey.txt', 'wb')
f.write(bytes(publickey.exportKey()))
f.close()
