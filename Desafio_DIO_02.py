def menu_inicial():
    menu = """\n
    --------------------- [[ BANCO ]] ----------------------------
    Seja bem-vindo(a) ao Banco XYZ! Escolha uma opção pra iniciar:

    [1] - Já possuo cadastro

    [2] - Criar usuário

    [3] - Nova conta corrente
 
    --------------------------------------------------------------
    => """
    return input(menu)

def criar_usuario(usuarios):
    cpf=int(input("Digite seu CPF: \n"))
    usuario=filtro_usuarios(cpf,usuarios)
    if usuario:
        print("Usuário já cadastrado!")
        return
    nome=str(input("Digite seu nome: \n"))
    data_nascimento=str(input("Digite sua data de nascimento separada por barras \n"))
    endereco = str(input("Digite seu endereço(logradouro, número, bairro, cidade /sigla do estado)"))
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "endereco":endereco})
    print("Usuário criado com sucesso!")

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf=int(input("Digite seu CPF: \n"))
    usuario=filtro_usuarios(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso! Obrigado pela preferência!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario" : usuario}
    print("Usuário não encontrado! Por favor crie um novo usuário!")

def saque_func(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo == 0:
        print("Seu saldo será creditado.Deseja continuar?")
        escolha = int(input("[1] para sim; [2] para não;\n"))
        if escolha == 2:
            print("Operação cancelada!")
            return main()
    if numero_saques < limite_saques:
        if valor > limite:
            print("Seu limite de saque é R$500,00. Por favor insira um valor menor.")
            print("----------------------------------------------------------------------------------")
        elif valor <= 0:
            print("Você inseriu um valor inválido. Por favor insira um valor positivo.") 
            print("----------------------------------------------------------------------------------")
        else:
            saldo -= valor
            print(f"Seu saque no valor de R${valor:.2f} foi registrado! Obrigado pela preferência.")
            extrato += f"Saque - R${valor:.2f}\n"
            numero_saques += 1
            print("----------------------------------------------------------------------------------")
    else:
        print("Você atingiu o número máximo de saques diários. Tente novamente amanhã.")
    return saldo, extrato, numero_saques


def deposito_func(saldo, valor, extrato,/):
    if valor <= 0:
        print("Você inseriu um valor inválido. Por favor insira um valor positivo.")
        print("----------------------------------------------------------------------------------")
    else:
        saldo += valor
        print(f"Seu depósito no valor de R${valor:.2f} foi registrado! Obrigado pela preferência.")
        extrato += f"Depósito - R${valor:.2f}\n"
        print("----------------------------------------------------------------------------------")
    return saldo, extrato

def extrato_func(saldo,/,*,extrato):
    print("-------------EXTRATO-------------\n")
    if extrato == "":
        print("Não houveram movimentações na conta bancária.")
    else:
        print(extrato)
        print(f"Saldo: R${saldo:.2f}")
    print("---------------------------------\n")
    return saldo,extrato

def listar_contas(contas):
    print("-------------CONTAS-------------\n")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}")
        print(f"Usuário: {conta['usuario']['nome']}")
        print("--------------------------------\n")
def escolha_opcao():
    escolha_usuario= """
    -------------------- [[ BANCO ]] ----------------------------
    Que operação deseja realizar?

    [s] - Saque

    [d] - Depósito

    [e] - Extrato

    [q] - Sair
  
    --------------------------------------------------------------
    => """
    return input(escolha_usuario)
    


def main():
    saldo = 0.0
    limite = 500
    extrato = ""
    contas = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    inicio = menu_inicial()
    AGENCIA ="001"
    while True:
        if inicio == "1": #já possuo conta
            escolha= escolha_opcao()
            if escolha == "s":
                valor= float(input("Digite a quantia que deseja sacar "))
                saldo, extrato, numero_saques = saque_func(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                    )
            elif escolha == "d":
                valor = float(input("Digite a quantia que deseja depositar "))
                saldo, extrato =deposito_func(saldo,valor,extrato)
            elif escolha == "e":
                saldo, extrato =extrato_func(saldo,extrato=extrato)
            elif escolha == "q":
                print ("Operação finalizada.")
                break
            else:
                print("Operação inválida! Tente Novamente.")
                print("----------------------------------------------------------------------------------")
        elif inicio == "2": #criar usuario
            criar_usuario(usuarios)
        elif inicio =="3": #Nova conta
            numero_conta = len(contas) + 1
            nova_conta= criar_conta(AGENCIA,numero_conta,usuarios)
            if nova_conta:
                contas.append(nova_conta)
        else:
            print("Opção inválida! Escolha novamente")    
            return main()
       
        
main()

