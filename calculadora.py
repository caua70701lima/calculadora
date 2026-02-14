while True:
    print("\nCalculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Resto da divisão")
    print("6 - Potenciação")
    print("7 - Porcentagem")
    print("0 - Sair")

    opcao = input("Escolha a operação: ")

    if opcao == "0":
        print("Encerrando...")
        break

    if opcao in ["1", "2", "3", "4", "5", "6", "7"]:
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
                continue
        elif opcao == "5":
            if num2 != 0:
                resultado = num1 % num2
            else:
                print("Erro: divisão por zero")
                continue
        elif opcao == "6":
            resultado = num1 ** num2
        elif opcao == "7":
            resultado = (num1 * num2) / 100

        print("Resultado:", resultado)
    else:
        print("Opção inválida")
