saldo = 1000.00
numero_de_saque = 0
LIMITE_SAQUE = 3


while True:

    print("\n caixa eletronico")
    print("1 - verificar saldo")
    print("2 - depositar dinheiro")
    print("3 - sacar dinheiro")
    print("4 - sair")

    opcao = input("escolha uma opção 1-4:")

    if opcao == "1":

        print(f"Seu saldo é: R${saldo:.2f}") # .2f que dizer que o número vai ter 2 casas decimais

    elif opcao == "2":

        deposito = float(input("Digite o valor que deseja depositar R$:"))

        if deposito > 0:

            saldo += deposito
            print(f" Depósito de R${deposito:.2f} realizado com sucesso")

        else:
            print(f"Valor do saque invalido")

    elif opcao == "3":

        saque = float(input("Digite o valor que deseja sacar R$:"))
        numero_de_saque +=1

        if saque > 0 and saque <= saldo and saque<=500 and numero_de_saque<=LIMITE_SAQUE:

            saldo -= saque
            print(f" Saque de R${saque:.2f} realizado com sucesso")

        else:
            print(f"Valor de saque inválido, saldo insulficiente ou Limite de saque exedido")

    elif opcao == "4":

        print("Obrigado por utilizar nossos caixas eletrônico. Até mais!")

        break
    
    else:

        print("Opção inválida.Por favor tente novamente!")



    







