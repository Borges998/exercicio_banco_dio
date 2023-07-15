saldo_atual = 1500
limite_saque = 500
num_saques_realizados = 0
movimentacoes = []

while True:
    MOEDA = 'R$'

    print('Bem vindo ao ING Bank...')
    print()
    print('[1] Sacar \n[2] Depositar \n[3] Saldo \n[4] Extrato \n[5] Sair')
    print()
    cliente_operacao = input('Por favor, selecione uma opção: ')
    print()

    try:
        cliente_operacao = int(cliente_operacao)
    except ValueError:
        print('Escolha inválida, escolha entre as opções.')
        print()
        continue

    if cliente_operacao == 1:
        if num_saques_realizados < 3:
            valor_saque = int(input('Quanto você gostaria de sacar: '))
            print()

            if valor_saque > limite_saque:
                print(f'Limite por saque atingido, seu limite é de {MOEDA}{float(limite_saque):.2f}')
                print()
                continue

            if valor_saque <= saldo_atual:
                saldo_atual -= valor_saque
                num_saques_realizados += 1
                movimentacoes.append(f'Saque de {MOEDA}{float(valor_saque):.2f}')
                print('Por favor, pegue seu dinheiro na boca do caixa!')
                print()
                continue
            else:
                print('Saldo insuficiente!')
                continue
        else:
            print('Limite máximo de saques atingido (3 vezes).')
            continue

    elif cliente_operacao == 2:
        valor = int(input('Quanto você gostaria de depositar: '))
        print()
        if valor >= 1:
            saldo_atual += valor
            movimentacoes.append(f'Depósito de {MOEDA}{float(valor):.2f}')
            print(f'Você acabou de depositar {MOEDA}{float(valor):.2f}, seu saldo agora é {MOEDA}{float(saldo_atual):.2f}')
            print()
            continue
        else:
            print('Valor para depósito inválido, tente novamente!')
            print()
            continue

    elif cliente_operacao == 3:
        print(f'Seu saldo é de {MOEDA}{float(saldo_atual):.2f}')
        print()
        continue

    elif cliente_operacao == 4:
        print('Extrato de movimentações:')
        for movimento in movimentacoes:
            print(movimento)
        print()
        continue

    elif cliente_operacao == 5:
        print('Agradecemos pela visita!')
        print('Saindo...')
        print()
        break

    else:
        print('Escolha inválida, escolha entre as opções.')
        print()
        continue
