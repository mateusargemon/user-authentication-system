import hashlib
import secrets
import string

usuarios = {}

def registrarUsuario():
    
    print("\nCADASTRO DE USUÁRIO\n")
    user=input("Usuário: ")
    senha=input("Defina sua senha: ")
    confirmarsenha=input("Confirme sua senha: ")

    while senha != confirmarsenha:
        print("Tente novamente.")
        confirmarsenha=input("Confirme sua senha: ")
    print("\nUsuário Cadastrado!\n")

    crip=hashlib.sha256(senha.encode()).hexdigest()
    codrecuperacao = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
    usuarios[user]={
        "senha": crip,
        "codrecuperacao": codrecuperacao
    }
    print(f"Usuário: {user}\nSenha: {senha}\nCódigo de Recuperação: {codrecuperacao}\n")
    
def login():
    
    tentativas1=0
    print("\nLOGIN\n")
    loginuser=input("Usuário: ")
    loginsenha=input("Senha: ")
    crip=hashlib.sha256(loginsenha.encode()).hexdigest()

    while loginuser not in usuarios or crip != usuarios[loginuser]["senha"]:
        tentativas1 += 1
        print("\nUsuário ou senha incorretos. Tente novamente.\n")
        loginuser=input("Usuário: ")
        loginsenha=input("Senha: ")
        crip=hashlib.sha256(loginsenha.encode()).hexdigest()
        
        if tentativas1 == 4:
            print("Deseja redefinir a senha?\n1. Sim\n2. Não\n")
            opcao=input("Sua escolha: ")
            
            if opcao == "1":
              print("Você escolheu redefinir a senha.") 
              redefinirSenha()
              break
          
            elif opcao == "2":
                print("Você escolheu não redefinir a senha.")
                login()
                break 
            
    print("\nAcesso liberado.\n")
        
def redefinirSenha():
    
    print("\nREDIFINIÇÃO DE SENHA\n")
    tentativas=0
    maxtentativas=3
    loginuser=input("Usuário: ")
    
    while loginuser not in usuarios:
        print("Usuário não encontrado.")
        loginuser=input("Usuário: ")
    
    while tentativas < maxtentativas:
        codrecuperacao=input("Insira o código de recuperaçao: ")
        
        if codrecuperacao==usuarios[loginuser]["codrecuperacao"]:
            novasenha=input("Digite a nova senha: ")
            confirmarnovasenha=input("Confirme a nova senha: ")
            
            while confirmarnovasenha != novasenha:
                print("\nAs senhas não coincidem.\n")
                confirmarnovasenha=input("Confirme a nova senha: ")
            usuarios[loginuser]["senha"]=hashlib.sha256(confirmarnovasenha.encode()).hexdigest()
            
            print("Senha redefinida com sucesso!\n")
            print(f"Cadastro alterado:\nUsuário: {loginuser}\nSenha: {confirmarnovasenha}\n")
            return
        
        tentativas += 1
        print(f"Código incorreto. Tentativas restantes: {maxtentativas-tentativas}")

def exibirUsuario():
    
    print("\nEXIBIÇÃO DE CADASTROS\n")
    user=input("Qual é o usuário: ")
    
    while user not in usuarios:
        print("\nUsuário não encontrado. Tente novamente.\n")
        user=input("Usuário: ")
        
    print(f"\nUsuário: {user}")
    print(f"Senha: {usuarios[user]['senha']}")
    print(f"Código de Recuperação: {usuarios[user]['codrecuperacao']}\n")
    
#MENU
print("PROJETO 1: CADASTRO DE USUARIOS\n")

while True:
    print("Olá, o que você deseja fazer?\n \n1. Cadastrar\n2. Entrar" \
    "\n3. Redefinir senha\n4. Ver informações de cadastro\n5. Sair\n")
    
    opcao=input("Sua escolha: ")
    opcoes=["1","2","3","4","5"]
    
    while opcao not in opcoes:
        print("Opção inválida.")
        opcao=input("Sua escolha: ")
        
    if opcao == "1":
     registrarUsuario()
    elif opcao == "2":
        login()
    elif opcao == "3":
        redefinirSenha()
    elif opcao == "4":
        exibirUsuario()
    elif opcao == "5":
       print("Você escolheu sair...")
       exit()
    
        
    
    
    
    

            
            
            
        

    
    



   




        
            

        
        


    
        
    

    




    
