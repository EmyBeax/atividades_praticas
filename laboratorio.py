pre = 0
vag = 20
opcao = 0
while opcao != 5:
    print('\n===== LABORATÓRIO DE INFORMÁTICA =====')
    print(" [1]  -- Registrar entrada de aluno")
    print(" [2]  -- Registrar saída de aluno")
    print(" [3]  -- Consultar alunos presentes")
    print(" [4]  -- Consultar vagas dispiníveis")
    print(" [5]  -- Encerrar sistema")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Registrar entrada de aluno
        if pre < 20:
            pre += 1
            vag -= 1
            print('\n Entrada registrada!')
        elif pre >= 20:
            print('\n O laboratório está CHEIO!')
    elif opcao == 2:
        # Registrar saída de aluno
        if pre >= 20:
            pre -= 1
            vag += 1
            print('\n Saída registrada!')
        elif pre == 0:
            print('\n O laboratório está VAZIO!')
    elif opcao == 3:
        # Consultar alunos presentes
        print(f'\n Há {pre} ALUNOS')
    elif opcao == 4:
        # Consultar vagas dispiníveis
        print(f'\n Há {vag} VAGAS')
    elif opcao == 5:
        # Encerrar sistema
        print('ENCERRANDO O SISTEMA')
    else:
        print('\033[31m\nOpção invalida.\033[00m')