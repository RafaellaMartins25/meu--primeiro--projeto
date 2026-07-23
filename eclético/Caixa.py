print(("=")*50)
print("CAIXA ELETRÔNICO")
print(("=")*50)

saldo = 1000

while True:
    print("1 - Ver Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    
    opcao = input("Escolha uma ação: ")
    
    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    elif opcao == "2":
        saque = float(input("Digite o valor para sacar: "))
        if saque > saldo:
            print("Saldo insuficiente!")
        elif saque <= 0:
            print("Valor inválido.")
        else:
            saldo = saldo - saque
            print(f"Saque feito! Saldo novo: R$ {saldo:.2f}")
    elif opcao == "3":
        deposito = float(input("Digite um valor para o deposito: "))
        if deposito > 0:
            saldo = saldo + deposito
            print(f"Depósito feito! Saldo novo: R$ {saldo:.2f}")
        else:
            print("Valor inválido para o depósito.")
    elif opcao == "4":
        print("Encerrando o atendimento. Obrigada!")
        break
    else:
        print("Opção inválida.Tente novamente.")