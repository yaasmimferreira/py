num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
    

def resultado():
    print("\n Selecione o número da operação desejada: \n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão \n")

    opcao = input("Digite sua opção (1/2/3/4): ")

   
    if opcao == '1':
        resultado = num1 + num2
        print(num1, "+", num2, "=", resultado)

    elif opcao == '2':
        resultado = num1 - num2
        print(num1, "-", num2, "=", resultado)

    elif opcao == '3':
        resultado = num1 * num2
        print(num1, "*", num2, "=", resultado)

    elif opcao == '4':
        resultado = num1 / num2
        print(num1, "/", num2, "=", resultado)

    else:
        print("Opção inválida, tente novamente.")

loop = True


while loop:
    resultado()

    sair = input("\nDeseja sair da calculdora? (S/N) ")

    if sair == "S": 
        loop = False