from cryptography.fernet import Fernet
from pymongo import MongoClient

def criptografar_multiplas_mensagens(mensagens):
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['mensagens_criptografadas']

    for mensagem in mensagens:
        mensagem_criptografada = fernet.encrypt(mensagem.encode())
        colecao.insert_one({"mensagem": mensagem_criptografada})

    client.close()
    print("Mensagens criptografadas e armazenadas no MongoDB.")

mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3"]
criptografar_multiplas_mensagens(mensagens)
