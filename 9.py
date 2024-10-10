from cryptography.fernet import Fernet
from pymongo import MongoClient

def armazenar_mensagem_mongodb(mensagem):
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())

    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['mensagens']
    colecao.insert_one({"chave": chave, "mensagem": mensagem_criptografada})
    client.close()
    print("Mensagem criptografada armazenada no MongoDB.")

mensagem = input("Digite a mensagem para criptografar e armazenar: ")
armazenar_mensagem_mongodb(mensagem)
