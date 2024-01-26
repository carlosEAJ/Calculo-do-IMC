peso = int(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))




if altura == int(altura):
    altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)     
print(f'Seu IMC é: , {imc:.2f}')
if imc < 18.5:
    print("Abaixo do peso")
    
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
    
elif imc >= 25 and imc < 30:
    print("Acima do peso")
    
elif imc >= 30 and imc < 40:
    print("Obeso")
    
else:
    print("Obesidade grave")