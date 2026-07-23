print(("=")*50) 
print("MENU DO JOGO")
print(("=")*50) 

print("1 - Novo Jogo")
print("2 - Carregar Jogo")
print("3 - Configurações")
print("4 - Sair")

opcao=input("Escolha uma opção:")

if opcao =="1":
    print("Começando o jogo...")
elif opcao =="2":
    print("Abrindo seu jogo...")
elif opcao =="3":
    print("Abrindo as configurações")
elif opcao =="4":
    print("Fechando o jogo...")
else:
    print("Opção inválida.Escolha de 1 a 4.")