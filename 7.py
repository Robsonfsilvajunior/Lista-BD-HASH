from cryptography.fernet import Fernet

def criptografar_mensagem(mensagem):
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return chave, mensagem_criptografada

mensagem = input("Digite a mensagem para criptografar: ")
chave, criptografada = criptografar_mensagem(mensagem)
print("Chave:", chave.decode())
print("Mensagem criptografada:", criptografada.decode())
