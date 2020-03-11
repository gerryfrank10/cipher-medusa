from Crypto.PublicKey import RSA
import Crypto
import ast
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

def generate():
    new_key = RSA.generate(2048)
    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")
    
    with open('private_key.pem','wb') as fd:
        fd.write(private_key)
    with open('public_key.pem','wb') as fd:
        fd.write(public_key)


def Ersa(msg, key):
    if key is None:
        print("Keys not specified, then generating new keys")
        generate()
        print("Specify the generated public keys ")
        print("Check you current working directory with <ls> to see the generated keys")
        exit(0)
    else:
        with open(key,'rb') as fd:
            public_key = fd.read()
            msg = str.encode(msg)
            rsa_public_key = RSA.importKey(public_key)
            rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
            enc_text = rsa_public_key.encrypt(msg)
            enc_text = base64.b64encode(enc_text)
        return enc_text

#generate rsa private keys for decrypt
def Drsa(msg, key):
    if key is None:
        print("Keys not specified, then generating new keys")
        generate()
        print("Specify the generated public keys ")
        print("Check you current working directory with <ls> to see the generated keys")
        exit(0)      
    with open (msg,'rb') as fd:
        enc_text = fd.read()
        enc_text = base64.b64decode(enc_text)
    with open (key, 'rb') as fd:
        private_key = fd.read()
        #enc_text = str.encode(enc_text)
        rsa_private_key = RSA.importKey(private_key)
        rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
        #print(enc_text)
        try:
            dec_text = rsa_private_key.decrypt(enc_text)
        except:
            print("Please use the correct keys")
            print("Otherwise use the new keys ")
            exit(0)
    return dec_text
    
#print(private_key)
#print(public_key)
#generate()
