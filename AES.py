from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'7\x19n\x99\x92\x7f\x0c\x16\xa7\xd5Lo\xe0 y\xf0\xe1\x1b\xe5\x8c<N\x96\xdb\x8e\xb0(4\xde\xa7Nu'
password = ""
iv = ""


def w_key(fn, key):
    with open(fn, 'wb') as f:
        f.write(key)


def w_enc(fn, civ, cipherdata):
    with open(fn, 'wb') as f:
        f.write(civ)
        f.write(cipherdata)


def rkey(fn):
    with open(fn, 'rb') as f:
        key = f.read()
    return key


def r_enc(fn):
    with open(fn, 'rb') as f:
        iv = f.read(16)
        dec_data = f.read()
    return dec_data, iv


def r_dec(fn):
    with open(fn, 'r+') as f:
        data = f.read()
    return data


def main():
    password = input("Enter Your password: ")
    mfile = input("Enter File Name: ")
    enfile = input("Encrypted data File name : ")
    keyfile = input("Key File name :")
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    message = r_dec(mfile)
    cipherdata = cipher.encrypt(pad(message.encode("ASCII"), AES.block_size))
    civ = cipher.iv
    w_enc(enfile, civ, cipherdata)
    with open(enfile, 'rb') as f:
        iv = f.read(16)
        dec_data = f.read()
    w_key(keyfile, key)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(dec_data), AES.block_size)
    print("Key: {}".format(key))
    print("Orginal: {}".format(original.decode('ASCII')))
    print("Cipherdata: {}".format(cipherdata))


if __name__ == "__main__":
    main()
