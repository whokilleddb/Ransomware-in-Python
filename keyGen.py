from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,PKCS1_OAEP # PKCS#1 OAEP is an asymmetric cipher based on RSA and the OAEP padding

#Geberate RSA Key
def generate_key():
    global key
    global key_pair

    #generate RSA key pair
    print("[+] Generating RSA Key Pair")
    key = RSA.generate(2048) #Create a new RSA key pair
    print(f"[+] Generated RSA Key :{key}")
    key_pair={}
    #print(key)
    key_pair['private']=key.exportKey() #export Private Key
    key_pair['public']=key.publickey().exportKey() #export Public Key
    print(f"[+] Public key : \n{key_pair['public'].decode('UTF-8')}")
    print(f"[+] Private key : \n{key_pair['private'].decode('UTF-8')}")

#Store keys in their respective files
def write_keys():
    global key_pair
    
    print("\n[+] Writing Public Key")
    f = open("public.pem", "wb")
    f.write(key_pair['public'])
    f.close()
    print("[+] Wrote Public Key In public.pem")

    print("\n[+] Writing Private Key")
    f = open(".private.pem", "wb") # Hidden file 
    f.write(key_pair['private'])
    f.close()
    print("[+] Wrote Private Key In .private.pem\n")

#Encrypt Fernet Key
def encrypt_fernet_key():
	global key_pair

	print("[+] Encrypting Fernet Key With RSA Public Key\n")

	#public_key=RSA.importKey(open('public.pem').read())
	public_key=RSA.importKey(key_pair['public']) #Import an RSA key (public), encoded in standard form
	#print(public_key)
	
	with open('fernet_key.txt','rb') as f :
		fernet_key=f.read()
	
	print(f"[+] Imported fernet key : \n{fernet_key}")
	#Create public encryptor
	public_encryptor=PKCS1_OAEP.new(public_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption

	#encrypt fernet key with public key
	with open('encrypted_fernet_key.txt','wb') as f:
		encrypted_fernet_key=public_encryptor.encrypt(fernet_key) #encrypt fernet key with public key
		f.write(encrypted_fernet_key)
	print(f"[+] Encrypted Fernet Key : \n{encrypted_fernet_key}")

def decrypt_fernet_key():
	global key_pair

	print("\n[+] Decrypting Fernet Key With RSA Private Key\n")

	#private_key=RSA.importKey(open('.private.pem').read())
	private_key=RSA.importKey(key_pair['private']) #Import an RSA key (private), encoded in standard form
	#print(private_key)
	
	with open('encrypted_fernet_key.txt','rb') as f :
		encrypted_fernet_key=f.read()
	
	print(f"[+] Imported Encrypted Fernet Key : \n{encrypted_fernet_key}")
	#Create public encryptor
	private_cryptor=PKCS1_OAEP.new(private_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption

	#encrypt fernet key with public key
	with open('decrypted_fernet_key.txt','wb') as f:
		decrypted_fernet_key=private_cryptor.decrypt(encrypted_fernet_key) #encrypt fernet key with public key
		f.write(decrypted_fernet_key)
	print(f"[\n+] Decrypted Fernet Key : \n{decrypted_fernet_key}")

if __name__ == '__main__':

    generate_key()
    write_keys()
    encrypt_fernet_key()
    decrypt_fernet_key()
