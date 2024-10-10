import hashlib
from pymongo import MongoClient

def salvar_hash_senha(senha):
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    client = MongoClient('mongodb+srv://robsonfsilvajunior:robson1234@cluster0.4vkav.mongodb.net/')
    db = client['Lista-BD']
    colecao = db['senhas']
    colecao.insert_one({"hash_senha": hash_senha})
    client.close()
    print("Hash da senha armazenado no MongoDB.")

def validar_senha(senha):
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    client = MongoClient('mongodb://localhost:27017/')
    db = client['meu_banco']
    colecao = db['senhas']
    documento = colecao.find_one({"hash_senha": hash_senha})
    client.close()
    if documento:
        print("Senha válida.")
    else:
        print("Senha inválida.")

senha = input("Digite a senha para armazenar seu hash: ")
salvar_hash_senha(senha)

senha_verificar = input("Digite a senha para validar: ")
validar_senha(senha_verificar)
