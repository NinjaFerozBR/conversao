#Crie um sistema para converter real em dollar 

#Variantes Dolar e Real
dolar = 1

real = 1

#Opção para digitar

opcao = int(input("Digite a opção \n 1- para converter real/dolar \n 2- para dolar/real) \n : "))


if opcao ==1: # Real*Dolar
    moeda = float(input("Digite o valor que deseja converter "))
    resultado = dolar * 5.19
    print(f"o valor em reais Convertidos para Dolar é {resultado}")
elif opcao ==2: # Dolar/Real
    moeda = float(input("Digite o valor que deseja converter "))
    resultado = dolar / 5.19
    print(f"o valor em dolar Convertidos para reais é {resultado}")
else:
    print("Opcao Invalida")

    







   

