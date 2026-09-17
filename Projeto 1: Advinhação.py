# Jogo de Adivinhação
import random  # Importa o módulo 'random' para gerar números aleatórios


def jogar_adivinhacao():  # Define a função 'jogar_adivinhacao'
    print("Bem-vindo ao jogo de adivinhação!")  # Imprime uma mensagem de boas-vindas
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100 e o atribui à variável 'numero_secreto'
    tentativas = 0  # Inicializa a variável 'tentativas' com o valor 0
    print("Tente adivinhar o número secreto entre 1 e 100.")  # Imprime uma mensagem instruindo o jogador a adivinhar o número secreto

    while True:  # Inicia um loop infinito
        try:  # Inicia um bloco 'try' para capturar exceções
            palpite = int(input("Digite o seu palpite: "))  # Solicita ao jogador um palpite e converte em número inteiro
        except ValueError:  # Captura a exceção 'ValueError' caso a conversão falhe
            print("Por favor, digite um número válido.")  # Imprime uma mensagem de erro caso o jogador não digite um número válido
            continue  # Continua para a próxima iteração do loop

        tentativas += 1  # Incrementa a variável 'tentativas' em 1

        if palpite < numero_secreto:  # Verifica se o palpite é menor que o número secreto
            print("Muito baixo! Tente novamente.")  # Imprime uma mensagem indicando que o palpite é muito baixo
        elif palpite > numero_secreto:  # Verifica se o palpite é maior que o número secreto
            print("Muito alto! Tente novamente.")  # Imprime uma mensagem indicando que o palpite é muito alto
        else:  # Caso o palpite seja igual ao número secreto
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")  # Imprime uma mensagem de parabéns indicando que o jogador acertou o número secreto e quantas tentativas foram feitas
            break  # Sai do loop ao acertar o número secreto


if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    jogar_adivinhacao()  # Chama a função 'jogar_adivinhacao' para iniciar o jogo