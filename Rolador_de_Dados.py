import random

Quantidade = int(input("Quantos dados serão rolados? "))
Dificuldade = int(input("Qual o número alvo da rolagem? "))
for _ in range(Quantidade):
    resultado = random.randint(1, 10)
    print(f"Seu resultado foi: {resultado}")
    if resultado >= Dificuldade:
        print("Sucesso!")
    elif resultado == 1:
        print("Falha Crítica!")
    else:
        print("Falha!")