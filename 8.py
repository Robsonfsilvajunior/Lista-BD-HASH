from cryptography.fernet import Fernet

def descriptografar_mensagem(chave, mensagem_criptografada):
    fernet = Fernet(chave)
    return fernet.decrypt(mensagem_criptografada).decode()

chave = input("Digite a chave: ").encode()
mensagem_criptografada = input("Digite a mensagem criptografada: ").encode()
mensagem_original = descriptografar_mensagem(chave, mensagem_criptografada)
print("Mensagem original:", mensagem_original)
