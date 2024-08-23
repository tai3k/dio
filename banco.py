menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

extrato = ""
saldo = 0
qtde_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    valor = float(valor)
    global saldo
    global extrato

    extrato += f"Depósito: R$ {valor:.2f}\n"
    saldo = saldo + valor

def saque(valor):
    valor = float(valor)
    global saldo
    global extrato
    global qtde_saques
    
    if valor <= 500 and qtde_saques <= LIMITE_SAQUES and saldo > 0:
        print ("Saque realizado com sucesso!")
        saldo = saldo - valor
        qtde_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
    elif valor > 500:
        print ("O valor máximo permitido para saque é R$ 500,00!")
    elif qtde_saques > 3:
        print ("A quantidade máxima de saques (3) já foi realizada!")
    elif saldo <= 0:
        print ("Saldo insuficiente!")
    else:
        print ("Erro desconhecido! Não foi possível sacar.")


def gerar_extrato():
    print ("\n=================== EXTRATO ===================")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"\nSaldo: R$ {saldo:.2f}")
    print ("=================================================")



while True:

    opcao = input (menu)

    if opcao == "d":
        print ("Depósito")
        valor = input ("Digite o valor do depósito: ")
        deposito(valor)

    elif opcao == "s":
        print ("Saque")
        valor = input ("Digite o valor do saque: ")
        saque(valor)

    elif opcao == "e":
        print ("Extrato")
        gerar_extrato()

    elif opcao == "q":
        break

    else:
        print ("Operação inválida! Por favor, escolha a operação desejada.")