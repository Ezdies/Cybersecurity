import secrets
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES


with open('tux.bmp', 'rb') as f: 
    byteblock = f.read() 
header = byteblock[:54] 
data = byteblock[54:]

data_padded = pad(data, 16)
key = secrets.token_bytes(16) #16 * 8 = 128
iv = secrets.token_bytes(16) #16 * 8 = 128

cipher = AES.new(key, AES.MODE_CBC, iv) 
ciphertext = cipher.encrypt(data_padded)

encrypted_image = header + ciphertext

with open('tux-96_cbc_enc.bmp', 'wb') as f: 
    f.write(encrypted_image)
    
with open('tux-96_cbc_enc.bmp', 'rb') as f: 
    byteblock = f.read() 
header = byteblock[:54] 
data = byteblock[54:]

cipher = AES.new(key, AES.MODE_CBC, iv) 
decrypted_data_padded = cipher.decrypt(ciphertext)
data_unpadded = unpad(decrypted_data_padded, 16)

decrypted_image = header + data_unpadded
with open('tux-96_dec.bmp', 'wb') as f:
    f.write(decrypted_image)


    
    