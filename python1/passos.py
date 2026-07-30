print(("=")*50)
print("CONTADOR DE PASSOS").center()
print(("=")*50)



print("1 - Leve")
print("2 - Moderado")
print("3 - Intenso")

passos=input("Escolha um modo:")

if passos =="1":
    print("Quantidades de passos:10")
    for Leve in range (10):
        print("Dando passos.."(Leve))
elif passos =="2":
    print("Quantidades de passos:20")
    for Moderado in range (20):
        print("Dando passos.."(Moderado))
else:
    print("Quantidades de passos:30")
    for Intenso in range (30):
        print("Dando passos.."(Intenso))


