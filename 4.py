import hashlib
from pymongo import MongoClient

def comparar_hash_mongodb(texto):
    hash_texto = hashlib.sha256(texto.encode()).hexdigest()
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['exercices']
    documento = colecao.find_one({"hash": hash_texto})
    client.close()
    if documento:
        print("Hash encontrado no MongoDB, corresponde ao valor armazenado.")
    else:
        print("Hash não encontrado no MongoDB.")

texto = input("Digite a string para verificar o hash no MongoDB: ")
comparar_hash_mongodb(texto)
