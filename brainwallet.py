import hashlib
import random
import base58
from secp256k1 import PrivateKey, PublicKey
from Crypto.Hash import RIPEMD160
from getpass import getpass

#returns tuple for compressed and uncompressed versions
# (compressed, uncompressed)
def getPublicKeysFromtheCurve(hashvalue):
    
    privkey = PrivateKey(hashvalue, raw=True)

    pubkey_ser = privkey.pubkey.serialize()
    pubkey_ser_uncompressed = privkey.pubkey.serialize(compressed=False)

    pubkey_ser_compressed = privkey.pubkey.serialize(compressed=True)

    return (pubkey_ser_compressed, pubkey_ser_uncompressed)

#Converts the ECC public key into Bitcoin public keys
def getBitcoinPublicKey(publicKeyBytes):
    
    publicSHA256 = hashlib.sha256(publicKeyBytes).digest()
    
    h = RIPEMD160.new()
    h.update(publicSHA256)
    hash160 = h.hexdigest()
    
    hash160app = "00"+ hash160
    
    firsHash = hashlib.sha256(bytes.fromhex(hash160app)).digest()
    secondHash = hashlib.sha256(firsHash).digest()   
    
    checksum = (secondHash.hex())[:8]

    encoded = "00"+ hash160 + checksum
    
    return  base58.b58encode( bytes.fromhex(encoded))
    
def getPrivateKeyinBitcoinFormat(hashvalue):
    
    #Now Wallet format

    ##prepend the version

    hashvalueHex = hashvalue.hex()

    privatekeyAndVersion = '80' + hashvalueHex 

    ## Now double SHA256 hashing for the checksum

    firsHash = hashlib.sha256(bytes.fromhex(privatekeyAndVersion)).digest()
    secondHash = hashlib.sha256(firsHash).digest()


    thePrivateKey =  privatekeyAndVersion+(secondHash.hex())[:8]

    privatekeyWif = base58.b58encode(bytes.fromhex(thePrivateKey))

    privateKeyAsInt = int.from_bytes(hashvalue, byteorder='big', signed=False)

    return privatekeyWif


val =input("Do you want to enter your password secretly? (Y/N)\n")
 
if val == 'N':
    
    password = input("Enter your password that has good strenght :")
else:
    password = getpass("Secret mode!!! Enter your password that has good strenght :")
    
#password = 'barinwallet online testing'

passwordAsByte = bytes(password,'utf-8') 

hashvalue = hashlib.sha256(passwordAsByte).digest()

print( "\n\nprivate key in Wif format = ", getPrivateKeyinBitcoinFormat(hashvalue) )

compressed, uncompressed = getPublicKeysFromtheCurve(hashvalue)


print( "uncompressed public key   = ", getBitcoinPublicKey(uncompressed) )
print( "compressed public key     = ", getBitcoinPublicKey(compressed) )
