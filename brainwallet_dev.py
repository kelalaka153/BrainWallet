import hashlib
import random
import base58
from secp256k1 import PrivateKey, PublicKey
from Crypto.Hash import RIPEMD160

def getPublicKey(publicKeyBytes):
    
    publicSHA256 = hashlib.sha256(publicKeyBytes).digest()
    
    h = RIPEMD160.new()
    h.update(publicSHA256)
    hash160 = h.hexdigest()
    
    #print("hash160", hash160)
    hash160app = "00"+ hash160
    
    firsHash = hashlib.sha256(bytes.fromhex(hash160app)).digest()
    secondHash = hashlib.sha256(firsHash).digest()   
    
    checksum = (secondHash.hex())[:8]
    #print( "checksum = " , checksum )
          
    encoded = "00"+ hash160 + checksum
    
    #print("encoded", encoded)
    
    print("encode BASE58 = ",  base58.b58encode( bytes.fromhex(encoded)) )
    
    
password = 'barinwallet online testing'



passwordAsByte = bytes(password,'utf-8') 

hashvalue = hashlib.sha256(passwordAsByte).digest()

hashvalueHex = hashvalue.hex()

print(hashvalueHex)


#Now Wallet format

##prepend the version

privatekeyAndVersion = '80' + hashvalueHex 

print(privatekeyAndVersion)

## Now double SHA256 hashing for the checksum

firsHash = hashlib.sha256(bytes.fromhex(privatekeyAndVersion)).digest()
secondHash = hashlib.sha256(firsHash).digest()

print("The checksum = ", (secondHash.hex())[:8])

thePrivateKey =  privatekeyAndVersion+(secondHash.hex())[:8]
print( thePrivateKey )


privatekeyWif = base58.b58encode(bytes.fromhex(thePrivateKey))

print("WIF in BASE58 = ", privatekeyWif)


privateKeyAsInt = int.from_bytes(hashvalue, byteorder='big', signed=False)

print("privateKeyAsInt = ", privateKeyAsInt)

##Public key part

privkey = PrivateKey(hashvalue, raw=True)

pubkey_ser = privkey.pubkey.serialize()
pubkey_ser_uncompressed = privkey.pubkey.serialize(compressed=False)


pubkey_ser_compressed = privkey.pubkey.serialize(compressed=True)


print("UC PUB IN Bytes  = ", pubkey_ser_uncompressed)
print("Co PUB IN Bytes  = ", pubkey_ser_compressed)


print("UC PUB IN Hex    = ", pubkey_ser_uncompressed .hex())
print("Co PUB IN Hex    = ", pubkey_ser_compressed .hex())

print("UC PUB IN BASE58 = ", base58.b58encode(pubkey_ser_uncompressed))
print("Co PUB IN BASE58 = ", base58.b58encode(pubkey_ser_compressed))


getPublicKey(pubkey_ser_uncompressed)
getPublicKey(pubkey_ser_compressed)
