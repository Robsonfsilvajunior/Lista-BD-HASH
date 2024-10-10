import hashlib

def gerar_hashes_diferentes(texto):
    md5_hash = hashlib.md5(texto.encode()).hexdigest()
    sha1_hash = hashlib.sha1(texto.encode()).hexdigest()
    sha256_hash = hashlib.sha256(texto.encode()).hexdigest()
    return md5_hash, sha1_hash, sha256_hash

texto = input("Digite a string para gerar hashes com MD5, SHA-1 e SHA-256: ")
md5, sha1, sha256 = gerar_hashes_diferentes(texto)
print("MD5:", md5)
print("SHA-1:", sha1)
print("SHA-256:", sha256)
