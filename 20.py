import hashlib

def gerar_hash_arquivo(nome_arquivo):
    hash_sha256 = hashlib.sha256()
    with open(nome_arquivo, "rb") as file:
        for bloco in iter(lambda: file.read(4096), b""):
            hash_sha256.update(bloco)
    return hash_sha256.hexdigest()

arquivo = "arquivo.txt"  
hash_inicial = gerar_hash_arquivo(arquivo)
print("Hash inicial do arquivo:", hash_inicial)

hash_verificacao = gerar_hash_arquivo(arquivo)
print("Hash após alteração:", hash_verificacao)

if hash_inicial == hash_verificacao:
    print("O arquivo não foi alterado.")
else:
    print("O arquivo foi alterado.")
