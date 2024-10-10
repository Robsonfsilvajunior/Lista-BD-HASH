import hashlib

def gerar_hash_sha256(senha):
    hash_object = hashlib.sha256(senha.encode())
    return hash_object.hexdigest()

senha = input("Digite a senha para gerar o hash SHA-256: ")
print("O Hash SHA-256:", gerar_hash_sha256(senha))
