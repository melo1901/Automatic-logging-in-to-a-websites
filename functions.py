from cryptography.fernet import Fernet


def key_create():
    key = Fernet.generate_key()
    return key


def key_write(key, key_name):
    with open(key_name, 'wb') as mykey:
        mykey.write(key)


def key_load(key_name):
    with open(key_name, 'rb') as mykey:
        key = mykey.read()
    return key


def file_encrypt(key, original_file, encrypted_file):
    f = Fernet(key)

    with open(original_file, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open(encrypted_file, 'wb') as file:
        file.write(encrypted)


def file_decrypt(key, encrypted_file, decrypted_file):
    f = Fernet(key)

    with open(encrypted_file, 'rb') as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open(decrypted_file, 'wb') as file:
        file.write(decrypted)
