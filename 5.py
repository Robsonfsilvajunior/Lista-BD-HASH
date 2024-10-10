import hashlib

def gerar_hash_md5(senha):
    hash_object = hashlib.md5(senha.encode())
    return hash_object.hexdigest()

senha = input("Digite a senha para gerar o hash MD5: ")
print("Hash MD5:", gerar_hash_md5(senha))
