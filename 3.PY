import hashlib
from pymongo import MongoClient

def salvar_hash_mongodb(texto):
    hash_texto = hashlib.sha256(texto.encode()).hexdigest()
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['exercices']
    colecao.insert_one({"texto": texto, "hash": hash_texto})
    client.close()
    print("Hash salvo no MongoDB com sucesso.")

texto = input("Digite a string para gerar e salvar o hash: ")
salvar_hash_mongodb(texto)
