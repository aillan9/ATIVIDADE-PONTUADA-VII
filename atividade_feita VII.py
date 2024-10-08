
# Entrada
nome = input("Informe seu nome completo: ")
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

# Definindo funções
def calcular_imc(peso, altura):
    resultado = peso / (altura * altura)

def classificar_imc(imc):
   if imc <18.5:
     return"Você está abaixo do peso!"
   elif imc >= 18.5 and imc <= 24.9:
      return"Você está no peso normal"
   elif imc >= 25 and imc <= 29.9:
      return"Sobrepeso"
   elif imc >= 30 and imc <= 34.9:
      return"Você está obeso no grau 1"
   elif imc >= 35 and imc <= 39.9:
      return"Você está obeso no grau 2"
   elif imc >= 40:
      return"Você está obeso no grau 3"

# Saída 
print(f"Nome completo:  {nome}")
print(f"Altura:  {altura}")
print(f"Peso:  {peso}")

classificar_imc(imc)
calcular_imc(peso, altura)