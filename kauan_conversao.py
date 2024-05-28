# Sistema de Conversão de Temperatura
def celsius_para_kelvin(celsius): # Celsius para Kelvin 
    try:
        kelvin = celsius + 273.15
        return kelvin
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Celsius.")


def kelvin_para_celsius(kelvin): # Inverso Kelvin para Celsius
    try:
        celsius = kelvin - 273.15
        return celsius
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Kelvin.")

def Celsius_para_Fareheing(fareheing): # Celsius para Fareheing
    try:
        fareheing = celsius + 33.8
        return fareheing
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Fareheing.")

def Fareheing_para_Celsius(fareheing): # Fareheing para Celsius
    try:
        celsius = fareheing -457.87
        return celsius
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Celsius.")



# Condiçoes
try:
    celsius = float(input("Digite uma temperatura em celsius °C: "))
    kelvin = celsius_para_kelvin(celsius)
    print(f"{celsius:.2f}°C é igual a {kelvin:.2f}K")
except ValueError:
    print("Por favor, insira um número válido.")

try:
    kelvin = float(input("Digite a temperatura em Kelvin °K : "))
    celsius = kelvin_para_celsius(kelvin)
    print(f"{kelvin:.2f}K é igual a {celsius:.2f}°C")
except ValueError:
    print("Por favor, insira um número válido.")

try:
    fareheing = float(input("Digite a temperatura em Fareheing °F : "))
    celsius = Fareheing_para_Celsius(fareheing)
    print(f"{fareheing:.2f}K é igual a {celsius:.2f}°C")
except ValueError:
    print("Por favor, insira um número válido.")

try:
    celsius = float(input("Digite a temperatura em Celsius °F : "))
    fareheing = Fareheing_para_Celsius(celsius)
    print(f"{celsius:.2f}°C é igual a {fareheing:.2f}°F")
except ValueError:
    print("Por favor, insira um número válido.")
