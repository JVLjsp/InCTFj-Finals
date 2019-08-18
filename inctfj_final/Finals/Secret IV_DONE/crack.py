#Thanks to @sayoojsamuel for helping out
pt= "Welcome to InCTFj finals! Hope you are having a great time here ;)"
ct= "1614ad13f934ca0e410da7785ddb3b248377eab15cb6cd46f355f5896ce848ce6675b8d48f284bf4186c982ac74f9f9302d2d0c78ab3cd87fd61f5fa02003b38418c2e33c09882de5da99a8066a2f4e7".decode('hex')
key= "YELLOW SUBMARINE"


from Crypto.Cipher import AES
from pwn import xor

def AES_decrypt(key, message):
	a = AES.new(key,AES.MODE_ECB)
	pt= a.decrypt(message)
	return pt

ct=AES_decrypt(key,ct)
IV= xor(ct,pt)[:16] #IV is only 16 bytes long 
print IV
