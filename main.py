from cryptography.fernet import Fernet


def read_file(fn):
    f = open(fn, "r+")
    data = f.read()
    return data


def write_file(fn, data):
    f = open(fn, "w+")
    fd = f.write(data.decode("ASCII"))
    return fd


def encrypt(key, data):
    dd = data.encode("ASCII")
    f_data = Fernet(key).encrypt(dd)
    return f_data


def decrypt(key, data):
    dd = data.encode("ASCII")
    f_data = Fernet(key).decrypt(dd)
    return f_data


def save_key(fn, data):
    f = open(fn, "w+")
    fd = f.write(data.decode("ASCII"))
    return fd


def main():
    opt = input("(N)ew or (O)ld key? ")
    match opt.lower():
        case 'n':
            key = Fernet.generate_key()
            print(key.decode('ASCII'))
        case 'o':
            key = input('Paste Key: ')
            key = key.encode('ASCII')
    opt2 = input("(S)ave Key or (D)ont: ")
    match opt2.lower():
        case 's':
            output_fn = input("Enter Key File name: ")
            save_key(output_fn, key)
        case 'd':
            pass
    opt3 = input("(E)ncrypt or (D)ecrypt data? ")
    match opt3.lower():
        case 'e':
            file_n = input("Enter File name: ")
            output_fn = input("Enter Output File name: ")
            data = read_file(file_n)
            new_data = encrypt(key, data)
            outd = write_file(output_fn, new_data)
            print(outd)
        case 'd':
            file_n = input("Enter File name: ")
            output_fn = input("Enter Output File name: ")
            data = read_file(file_n)
            new_data = decrypt(key, data)
            outd = write_file(output_fn, new_data)
            print(outd)


if __name__ == '__main__':
    main()
