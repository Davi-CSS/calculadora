print('Digite dois números:')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b

def calcular_multiplicacao(a, b):
    return a * b

def calcular_divisao(a, b):
    if b == 0:
        return 'Divisão por zero não é permitida.'
    return a / b

# Resultados das operações básicas
print(f'A soma é: {calcular_soma(num1, num2)}')
print(f'A subtração é: {calcular_subtracao(num1, num2)}')
print(f'A multiplicação é: {calcular_multiplicacao(num1, num2)}')
print(f'A divisão é: {calcular_divisao(num1, num2)}')

# Parte dos juros compostos
print('\nDigite o capital, a taxa de juros e o tempo:')
capital = float(input('Capital: '))
taxa = float(input('Taxa de juros (em decimal): '))
tempo = float(input('Tempo (em anos): '))

def calcular_juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    return montante, juros

montante, juros = calcular_juros_compostos(capital, taxa, tempo)

print(f'O montante é: R$ {montante:.2f}')
print(f'O juros é: R$ {juros:.2f}')
