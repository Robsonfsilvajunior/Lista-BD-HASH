from cryptography.fernet import Fernet
from pymongo import MongoClient

def recuperar_mensagem_mongodb():
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['mensagens']
    documento = colecao.find_one()

    if documento:
        chave = documento['chave']
        mensagem_criptografada = documento['mensagem']
        fernet = Fernet(chave)
        mensagem_original = fernet.decrypt(mensagem_criptografada).decode()
        print("Mensagem descriptografada:", mensagem_original)
    else:
        print("Nenhuma mensagem encontrada.")

    client.close()

recuperar_mensagem_mongodb()
