# Dia 02 Desafio Extra
nome = input("Qual é o seu nome? ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
resto = n1 % n2
potencia = n1 ** n2
print(f"\n--- Resultados para {nome} ---")
print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div:.2f}")
print(f"Resto da Divisão: {resto}")
print(f"{n1} elevado a {n2} = {potencia}")