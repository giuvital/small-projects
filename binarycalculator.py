print('___Calculadora de Decimal para Binários___')
print('\n')
def decimalparabinario(num):
    if num > 1:
        decimalparabinario(num // 2)
    print(num % 2, end='')

numero = int(input("Digite o valor de um número decimal: "))

decimalparabinario(numero)
