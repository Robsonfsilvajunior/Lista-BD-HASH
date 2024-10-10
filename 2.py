import hashlib

def gerar_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

texto1 = input("Digite a primeira string: ")
texto2 = input("Digite a segunda string: ")

hash1 = gerar_hash_sha256(texto1)
hash2 = gerar_hash_sha256(texto2)

if hash1 == hash2:
    print("As strings possuem o mesmo hash.")
else:
    print("As strings possuem hashes diferentes.")
