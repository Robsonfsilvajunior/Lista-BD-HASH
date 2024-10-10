from cryptography.fernet import Fernet
from pymongo import MongoClient

def recuperar_chave_e_descriptografar(mensagem_criptografada):
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['chaves']
    documento = colecao.find_one()

    if documento:
        chave = documento['chave']
        fernet = Fernet(chave)
        mensagem_original = fernet.decrypt(mensagem_criptografada.encode()).decode()
        print("Mensagem descriptografada:", mensagem_original)
    else:
        print("Nenhuma chave encontrada no MongoDB.")

    client.close()

mensagem_criptografada = input("Digite a mensagem criptografada: ")
recuperar_chave_e_descriptografar(mensagem_criptografada)
