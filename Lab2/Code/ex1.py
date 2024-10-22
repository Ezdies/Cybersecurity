import secrets
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


with open('tux.bmp', 'rb') as f: 
    byteblock = f.read() 
header = byteblock[:54] 
data = byteblock[54:]

data_padded = pad(data, 16)
key = secrets.token_bytes(16) #16 * 8 = 128

cipher = AES.new(key, AES.MODE_ECB) 
ciphertext = cipher.encrypt(data_padded)

encrypted_image = header + ciphertext

with open('tux-96_enc.bmp', 'wb') as f: 
    f.write(encrypted_image)

    
    