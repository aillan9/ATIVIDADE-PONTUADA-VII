import os
os.system("cls || clear")

# Entrada
nome = input("Informe seu nome completo: ")
peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em metros): "))

# Processamento
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        print("Você está abaixo do peso!")
    elif 18.5 <= imc <= 24.9:
        print("Você está no peso normal.")
    elif 25 <= imc <= 29.9:
        print("Você está com sobrepeso.")
    elif 30 <= imc <= 34.9:
        print("Você está obeso no grau 1.")
    elif 35 <= imc <= 39.9:
        print("Você está obeso no grau 2.")
    elif imc >= 40:
        print("Você está obeso no grau 3 (obesidade mórbida).")

# Definindo imc
imc = calcular_imc(peso, altura)

# Saída 
print(f"\nNome completo: {nome}")
print(f"Altura: {altura} m")
print(f"Peso: {peso} kg")
print(f"IMC: {imc:.2f}")
classificar_imc(imc)