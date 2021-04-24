
encrypt = '2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'


def xor_decrypt(encrypt, key):
    encrypt = int(encrypt, 16)
    key = bytes(key, 'ascii')
    key = int(key.hex(), 16)
    decrypt = encrypt ^ key
    decrypt_str = bytes.fromhex(hex(decrypt)[2:])
    return decrypt_str


def special_xor(encrypt, key):  # вернуть расшифрованную строку. Нужен шифр-текст в  hex и ключ в dec
    encrypt = int(encrypt, 16)
    key = hex(key)[2:]*26
    key = int(key, 16)
    decrypt = encrypt ^ key
    decrypt_str = bytes.fromhex(hex(decrypt)[2:])
    return decrypt_str


print(special_xor('f807d7abd0cf8f82f56c22b59f1d22fcf1732163dcc4062a3f18', 55))


encrypt = open('output.txt', 'r')


with open('text.txt', 'w') as file:
    for enc in encrypt:
        print(enc)
        for i in range(256):
            try:
                file.write(str(special_xor(enc, i)) + '\n')
            except ValueError:
                continue
        
encrypt.close()
