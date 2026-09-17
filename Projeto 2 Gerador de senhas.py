import random
import string


def gerar_senha(tamanho=16, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%^&*()-_=+"
    if not caracteres:
        raise ValueError("Escolha pelo menos um tipo de caractere!")

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("Gerador de Senhas\n")

    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
            if tamanho < 4:
                print("O tamanho mínimo da senha é 4. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    print("\nTipos de caracteres (s/n):")
    maiusculas = input("incluir MAIÚSCULAS? [s] ").strip().lower() != "n"
    minusculas = input("incluir minúsculas? [s] ").strip().lower() != "n"
    numeros = input("incluir números? [s] ").strip().lower() != "n"
    simbolos = input("incluir símbolos? [s] ").strip().lower() != "n"

    try:
        senha = gerar_senha(
            tamanho=tamanho,
            usar_maiusculas=maiusculas,
            usar_minusculas=minusculas,
            usar_numeros=numeros,
            usar_simbolos=simbolos,
        )
    except ValueError as e:
        print(f"\nErro: {e}")
        return

    print(f"\nSua Senha: {senha}")
    print(f"Comprimento da Senha: {len(senha)} caracteres")


if __name__ == "__main__":
    main()