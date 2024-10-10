from cryptography.fernet import Fernet

def gerar_e_salvar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as file:
        file.write(chave)
    print("Chave Fernet salva em 'chave.key'.")

gerar_e_salvar_chave()
''