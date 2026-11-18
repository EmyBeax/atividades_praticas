lrv = 10
lvem = 0
opcao = 0
while opcao != 5:
    print('\n===== BIBLIOTECA ESCOLAR =====')
    print(" [1]  -- Emprestar um livro")
    print(" [2]  -- Devolver um livro")
    print(" [3]  -- Consultar livros disponíveis")
    print(" [4]  -- Consultar livros emprestados")
    print(" [5]  -- Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Emprestar um livro
        if lrv > 0:
            lrv -= 1
            lvem += 1
            print(f'\nUm EMPRESTIMO de livro foi registrado!')
        elif lrv <= 0:
            print('Não há livros para serem emprestados')
    elif opcao == 2:
        # Devolver um livro
        if lvem > 0:
            lrv += 1
            lvem -= 1
            print('\nUma DEVOLUÇÃO de livro foi registrado!')
        elif lvem <= 0:
            print('Não há livros para serem devolvidos')
    elif opcao == 3:
        # Consultar livros disponíveis
        print(f'\nNúmero de livros disponíveis: {lrv}')
    elif opcao == 4:
        # Consultar livros emprestados
        print(f'\nNúmero de livros emprestados: {lvem}')
    elif opcao == 5:
        # Encerrar
        print("ENCERRANDO")
    else:
        print('\033[31m\nOpção invalida.\033[00m')