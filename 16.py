import hashlib

def comparar_tamanho_hashes(texto):
    md5_hash = hashlib.md5(texto.encode()).hexdigest()
    sha1_hash = hashlib.sha1(texto.encode()).hexdigest()
    sha256_hash = hashlib.sha256(texto.encode()).hexdigest()
    print(f"Tamanho MD5: {len(md5_hash)} caracteres")
    print(f"Tamanho SHA-1: {len(sha1_hash)} caracteres")
    print(f"Tamanho SHA-256: {len(sha256_hash)} caracteres")

texto = input("Digite a string para comparar os tamanhos dos hashes: ")
comparar_tamanho_hashes(texto)
