print("Calculadora Simples")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha a operação: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = num1 + num2
elif opcao == "2":
    resultado = num1 - num2
elif opcao == "3":
    resultado = num1 * num2
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        exit()
else:
    print("Opção inválida")
    exit()

print("Resultado:", resultado)
