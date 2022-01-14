from time import sleep

repeticao = 1
while repeticao == 1:
    try:
        print('======== CALCULADORA 3.000========')
        print('IMPORTANTE ATENÇÃO NAS OPERAÇÕES: 1 (somar), 2 (subtrair), 3 (multiplicar), 4 (dividir)')
        operacao = int(input('Qual será a operação das citadas ACIMA? '))
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        repeticao = 0
        print('CALCULANDO...')
        sleep(3.0)
        if operacao == 1:
            somar = (n1 + n2)
            print('A soma é {}'.format(somar))
            print(f'A soma é {somar}')
        elif operacao == 2:
            subtrair = (n1 - n2)
            print('A subtração é: {}'.format(subtrair))
        elif operacao == 3:
            multiplicar = (n1 * n2)
            print('A multiplicação é: {}'.format(multiplicar))
        elif operacao == 4:
            if n2 == 0:
                print('Não é possivel dividir por zero!')
            else:
                dividir = (n1 / n2)
                print('A divisão é: {}'.format(dividir))
        else:
            print('Operação invalida!')
    except Exception as erro:
        print(erro)