itens="poção, espada, escudo, varinha mágica, arco"
print(("=")*50)
print("SISTEMA DE INVENTÁRIO").center()
print(("=")*50)

opcao=input("Escolha uma opção:")

while True:
    print("Olhar")
    print("Usar")
    print("Sair")
    if opcao =="olhar":
        print(f"ITENS:{itens}")

    elif opcao =="usar":
      print(f"ITENS:{itens}")
      item=input("Qual item vc deseja escolher?").lower()
        
      if "item" in "itens":
       print(f"Ação realizada, você usou o item: {item}")

      else:
       print(f"Você não tem esse item {item} no seu inventário")

    elif opcao =="sair":
        print("Encerrando o sistema...")
        break
    else:
        print("Ação não identificada!")        
