from datetime import datetime, date, timedelta, timezone, time

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 10
usuarios = []
contas = []

def exibir_deposito():
    global saldo, extrato

    print("----Depósito----")
    valor = float(input("Digite o valor do seu depósito: "))
    data_hora = datetime.now().strftime("%d/%m/%Y, %H:%M")

    if valor >= 0:
        saldo += valor
        extrato += f"depósito: R$: {valor:.2f} em: {data_hora}\n"
        
        print(f"deposito no valor de R$: {valor}, realizado com sucesso!") 
        print(f"Horário do depósito: {data_hora}")
        print(f"Saldo atual de: R$: {saldo:.2f}")
        print("-------------------------------")
    else:
        print("Valor não reconhecido, tente novamente!")

def exibir_saque():
    global saldo, extrato, numero_saques, limite, limite_saques

    print("----Saque----")
    valor = float(input("Digite o valor do seu saque: "))

    excedeu_saque = numero_saques >= limite_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    data_hora = datetime.now().strftime("%d/%m/%Y, %H:%M")
    data_atual = date.today()
    data_futura = data_atual + timedelta(days=1)

    if excedeu_saque:
        print("Não foi possivel realizar seu saque, pois excede o limite diario!")
        print(f"Saques liberam em: {data_futura}")
        print("-----------------")
    elif excedeu_limite:
        print("Não foi possivel realizar seu saque pois excede o limite de valor de saque permitido.")
        print("-----------------")
    elif excedeu_saldo:
        print(f"Saque não realizado pois excede o valor do saldo atual de: {saldo:.2f}")
        print("-----------------")        
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R$: {valor:.2f} em {data_hora}\n"
        numero_saques += 1
        print(f"Saque no valor de: R$:{valor:.2f}, realizado com sucesso!")
        print(f"Horário de depósito: R${data_hora}")
        print(f"saldo atual de: R$:{saldo:.2f}")
        print("-----------------")    
    else:
        print("Não foi possivel realizar o saque, tente novamente!")

def exibir_extrato():
    global saldo, extrato

    print("Não foram realizadas nenhuma transação" if not extrato else extrato)
    print(f"extrato atual: R$ {saldo:.2f}")    



def cadastro_usuario(usuarios):
    print("----Cadastro----")
    cpf = input("informe seu CPF (apenas os numeros:)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("ja existe um usuario com esse CPF")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço:")

    usuarios.append({"nome": nome , "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("usuario cadastrado com sucesso")
    print("-----------------")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(contas):
     print("---- Criar conta----")
     cpf = input("Informe o CPF do titular da conta: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if not usuario:
        print("Usuário não encontrado. Cadastre o usuário antes de criar uma conta.")
        return

     for conta in contas:
        if conta["cpf"] == cpf:
            print(f"Erro: O usuário com CPF {cpf} já possui uma conta.")
            return

     nova_conta = {
        "agencia": "0001",
        "numero_conta": len(contas) + 1,
        "cpf": cpf,
        "titular": usuario["nome"]
    }

     contas.append(nova_conta)
     print(f"Conta criada com sucesso! Agência: {nova_conta['agencia']}, Número da conta: {nova_conta['numero_conta']}")
     print("-----------------")


def listar_contas():
      if not contas:
        print("Nenhuma conta foi criada ainda.")
      else:
        for conta in contas:
            print(f"Titular: {conta['titular']}, CPF: {conta['cpf']}, Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")



def mostrar_menu():
    print("")
    print("-----------------------------------------")   
    print("-----Seja bem-vindo ao banco norter------")
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[4] Cadastro de usuário")
    print("[5] Criar conta")
    print("[6] Listar conta")
    print("[7] Sair")
    
    return input("escolha uma opção: ")

def executar ():
    while True:
        opcao = mostrar_menu()
        if opcao == "1":
            exibir_deposito()
        elif opcao == "2":
            exibir_saque()
        elif opcao =="3":
            exibir_extrato()
        elif opcao == "4":
            cadastro_usuario(usuarios)
        elif opcao == "5":
            criar_conta(contas)
        elif opcao == "6":
            listar_contas()
        elif opcao =="7":
            print("Muito obrigado por utilizar o nosso sistema! Até breve!")
            break
        else:
            print("Essa opção não existe, tente novamente!")

executar()