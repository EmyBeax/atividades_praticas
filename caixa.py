saldo = 500
op = 0
opcao = 0
dep = 0
saq = 0
while opcao != 5:
    print('\n===== CAIXA ELETRÔNICO =====')
    print(" [1]  -- Consultar saldo")
    print(" [2]  -- Realizar depósito")
    print(" [3]  -- Realizar saque")
    print(" [4]  -- Consultar quantidade de operações")
    print(" [5]  -- Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Consultar saldo
        print(f'\n Saldo: R${saldo}')
    elif opcao == 2:
        # Realizar depósito
        print('\n Qual o valor do depósito?')
        dep = int(input('ADICIONE O VALOR: R$'))
        if dep > 0:
            saldo += dep
            op += 1
            print('Depósito concluído')
        elif dep <= 0:
            print('\nImpossível fazer o depósito desse valor.')
    elif opcao == 3:
        # Realizar saque
        print('\n Qual o valor do saque?')
        saq = float(input('ADICIONE O VALOR: R$'))
        if saq <= saldo:
            saldo -= saq
            op += 1
            print('Saque concluído')
        elif saq > saldo:
            print('\nImpossível fazer o saque desse valor.')
    elif opcao == 4:
        # Consultar quantidade de operações
        print(f'\nQuantidade de operações registradas:{op}')
    elif opcao == 5:
        # Encerrar
        print("ENCERRANDO")
    else:
        print('\033[31m\nOpção invalida.\033[00m')