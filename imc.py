def calcular_imc(peso, altura):
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    return imc

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))

imc = calcular_imc(peso, altura)

print("Seu IMC é: {:.2f}".format(imc))


#  Ela converte a altura para metros e calcula o IMC usando a fórmula IMC = peso / (altura ** 2).
