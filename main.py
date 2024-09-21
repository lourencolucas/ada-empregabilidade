def adicao(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolhas = input("Digite a opção (1/2/3/4): ")

        if escolhas in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolhas == '1':
                print(f"{num1} + {num2} = {adicao(num1, num2)}")

            elif escolhas == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            elif escolhas == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolhas == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

        else:
            print("Opção inválida! Tente novamente.")

        proximo_calculo = input("Deseja realizar outra operação? (s/n): ")
        if proximo_calculo.lower() != 's':
            break

calculator()