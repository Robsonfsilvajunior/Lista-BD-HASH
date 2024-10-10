from cryptography.fernet import Fernet

def ler_chave_e_criptografar(mensagem):
    with open("chave.key", "rb") as file:
        chave = file.read()
    fernet = Fernet(chave)
    return fernet.encrypt(mensagem.encode())

mensagem = input("Digite a mensagem para criptografar: ")
mensagem_criptografada = ler_chave_e_criptografar(mensagem)
print("Mensagem criptografada:", mensagem_criptografada.decode())
