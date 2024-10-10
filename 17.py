import hashlib

def hash_hexadecimal(texto):
    hash_object = hashlib.sha256(texto.encode())
    return hash_object.hexdigest()

texto = input("Digite a string para gerar o hash hexadecimal: ")
print("Hash SHA-256 em hexadecimal:", hash_hexadecimal(texto))
