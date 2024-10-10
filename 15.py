from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as file:
        file.write(chave)

def ler_chave():
    with open("chave.key", "rb") as file:
        return file.read()

def criptografar_arquivo(nome_arquivo):
    chave = ler_chave()
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = fernet.encrypt(dados)
    with open("arquivo_criptografado", "wb") as file:
        file.write(dados_criptografados)
    print(f"Arquivo '{nome_arquivo}' criptografado.")

def descriptografar_arquivo(nome_arquivo):
    chave = ler_chave()
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados_criptografados = file.read()
    dados = fernet.decrypt(dados_criptografados)
    with open("arquivo_descriptografado", "wb") as file:
        file.write(dados)
    print(f"Arquivo '{nome_arquivo}' descriptografado.")

gerar_chave()
criptografar_arquivo("arquivo.txt")  
descriptografar_arquivo("arquivo_criptografado")
