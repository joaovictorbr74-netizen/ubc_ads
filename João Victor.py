# =============================================================
# PROJETO: Calculadora em Python
#integrantes :
#Davi Henrique Viana da Silva 43494633
#Gabriel Rodrigues Da Silva 41780841
#Guilherme Virche Dos Santos 42574773
#João Victor Nogueira Galvão 42721482
# =============================================================

"""
ESTRUTURA SUGERIDA DO PROJETO NO GITHUB

calculadora-python/
│
├── calculadora.py
├── README.md
└── .gitignore

Este arquivo representa o script principal: calculadora.py
"""

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b


def menu():
    print("=== CALCULADORA EM PYTHON ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def main():
    calc = Calculadora()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Digite apenas números válidos.\n")
            continue

        if opcao == "1":
            resultado = calc.somar(num1, num2)
        elif opcao == "2":
            resultado = calc.subtrair(num1, num2)
        elif opcao == "3":
            resultado = calc.multiplicar(num1, num2)
        elif opcao == "4":
            resultado = calc.dividir(num1, num2)
        else:
            print("Opção inválida")
            continue

        print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    main()

