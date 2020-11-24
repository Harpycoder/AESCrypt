#CifrarDecifrar_AES#
#Disciplina: Introdução à Programação Estruturada
# 2° Péríodo em Ciência da Computação - UNIP Campus Manaus

#Autor: Gustavo Abtibol de Oliveira

# Grupo:    Fábio Henrique Martins de Oliveira
#           Gustavo Abtibol de Oliveira
#           Levi Lima


# Nota: Em caso de caracteres errados durante o input de chaves e cifras
#       o programa poderá crashar.


from cryptography.fernet import Fernet
import os.path


def criar_chave():
    chave = Fernet.generate_key()
    arquivo = open("chave.key", 'wb')
    arquivo.write(chave)
    arquivo.close()
    return chave

def obter_chave():
    arquivo = open('chave.key', 'rb')
    chave = arquivo.read()
    arquivo.close()
    return chave

def gerador_chave():
    if os.path.exists('chave.key'):
        os.remove('chave.key')
    criar_chave()
    obter_chave()


def comandos():
    print(" ")
    print("----------------------------------------------------------------")
    print("Bem vindo(a) ao cifrador e decifrador em AES.")
    print("Selecione o que deseja a fazer com os comandos abaixo.")
    print(" ")
    print("(0) Fechar programa")
    print("(1) Gerar uma chave")
    print("(2) Criptografar uma mensagem (usando sua chave)")
    print("(3) Criptografar uma mensagem (usando chave gerada automaticamente)")
    print("(4) Decriptar uma mensagem")
    print("----------------------------------------------------------------")
    print(" ")
    acao() #Chama a função de ação para inserir um comando

def acao(): #Decidir qual ação será tomada à partir do comando
    comando = int(input(">>> "))

    if comando == 0: #Fechar programa
        quit()
    
    elif comando == 1: #Gerar uma chave (não é necessário chamar uma função)
        gerador_chave()
        chave = obter_chave()
        print("Sua chave é: ", chave.decode())
        comandos()
    
    elif comando == 2: #Criptografar uma mensagem (usando sua chave)
        criptografar_manual()

    elif comando == 3: #Criptografar uma mensagem (usando chave gerada automaticamente)
        criptografar_auto()

    elif comando == 4: #Decriptar uma mensagem"
        decriptar_manual()

    else:
        print("Por favor, digite um comando válido.")
        comandos()

    
def criptografar_manual():
    mensagem = str(input("Insira a mensagem a ser criptografada: "))
    chave = input("Insira sua chave: ")
    codificado = mensagem.encode()
    f = Fernet(chave)
    cifrado = f.encrypt(codificado)
    print(" ")
    print("Mensagem criptografada: ", cifrado.decode())
    comandos()


def criptografar_auto():
    mensagem = str(input("Insira a mensagem a ser cifrada: ")).encode()
    chave = Fernet.generate_key()
    f = Fernet(chave)
    cifrado = f.encrypt(mensagem)
    print(" ")
    print("Mensagem cifrada: ", cifrado.decode())
    print(" ")
    print("Chave utilizada: ", chave.decode())
    comandos()


def decriptar_manual():
    mensagem_cifrada = str(input("Mensagem a ser decifrada: ")).encode()
    chave = input("Chave: ").encode()
    f = Fernet(chave)
    decifrado = f.decrypt(mensagem_cifrada)
    print(" ")
    print("Mensagem decifrada: ", decifrado.decode())
    comandos()


comandos() # Aqui que a "tela" de comandos é chamada pela primeira vez
