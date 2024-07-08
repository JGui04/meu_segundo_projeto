"""
Programa: Caixa Eletrônico
Autor: J. Guilherme
licença: GNU
Data: 2024/07/02
Versão: v1.1.1

Objetivo: Desenvolver um programa em Python que simula as
operações básicas de um caixa eletrônico. O usuário deve ser capaz de
verificar o saldo, depositar dinheiro, sacar dinheiro e sair do programa.
"""

# O saldo inícial da conta
saldoDinheiro = 0

# Para que o caixa entre em um Loop e o usuário consiga fazer quantas operações ele quiser.
while True:


    # Caso o que seja digitado não for um número inteiro, o programa irá verificar
    try:

        # O Menu inícial do usuário para escolher e fazer as operações.
        opcoes = int(input("Caixa Eletrônico"
                    "\n1 - Verificar Saldo"
                    "\n2 - Depositar Dinheiro"
                    "\n3 - Sacar Dinheiro"
                    "\n4 - Sair"
                    "\nEscolha uma opção (1-4): "))

        # O usuário pode acabar apertando em números maiores do que os que estão disponíveis, então dará um erro e entrará em um Loop para que ele possa digitar novamente.
        while opcoes < 1  or opcoes > 4:
            print('\nERRO - Número de verificação não existe\n')
            opcoes = int(input("Caixa Eletrônico"
                    "\n1 - Verificar Saldo"
                    "\n2 - Depositar Dinheiro"
                    "\n3 - Sacar Dinheiro"
                    "\n4 - Sair"
                    "\nEscolha uma opção (1-4): "))
        
    # Caso a verificação for falsa e tenha algo que não seja um número inteiro, ele dará um erro, mas voltará com Menu inícial novamente para o usuário.
    except:
        print('Erro digite novamente a sua operação')

        # Volte ao menu inicial ao usuário.
        continue



    # Se a opção que o usuário escolher for o número 1 ou seja o saldo da conta, ele mostrará na tela quanto o usuário tem disponível.
    if opcoes == 1:
    
        print("\nO saldo da sua conta é de: R$", saldoDinheiro)

    # Se a opção 2 for a escolhida ou seja depositar dinheiro, o usuário poderá fazer um depósito em sua conta.
    elif opcoes == 2:

        # Esse Loop foi feito para o caso do usuário for fazer um depósito e acabar digitando errado e ele voltar para que o usuário possa digitar novamente a quantia que deseja depositar.
        while True:

            # Aqui onde o Programa irá verificar se o usuário digitou certo.
            try:

                # O usuário vai digitar a quantia do seu depósito.
                saldoDeposito = int(input("Digite quanto você quer depositar R$ "))

                '''
                Por ser um depósito não pode ser digitado em números negativos, esse Loop vai verificar se o que o usuário digitou seja positivo para que não dê errado a operação, caso o usuário digite um número negativo, vai mostrar a opção novamente para que ele possa digitar a quantia do seu depósito certo.
                '''
                while saldoDeposito < 0:
                    print('\nVocê não pode depositar um valor negativo, digite novamente\n')
                    saldoDeposito = int(input("Digite quanto você quer depositar R$ "))

                # Imprimirá na tela o valor em que foi feito o depósito em sua conta.
                print(f"Você depositou: R$ { saldoDeposito} em sua conta.")

                # Fará a soma do depósito feito mais o saldo da conta. 
                saldoDinheiro += saldoDeposito

                # Vai parar o Loop e voltará para o Menu inicial ao usuário.
                break
            
            # Se a verificação do programa for falsa, ele imprimirá um erro na tela do usuário 
            except:
                print('\nIsso não é um valor válido, digite novamente\n')

                # Volte ao início desse Loop, para que o usuário possa digitar novamente a quantia que vai depositar.
                continue


    # Se a opção escolhida for o 3 ou seja o sacar dinheiro, o usuário poderá fazer um saque de sua conta.
    elif opcoes == 3:
        
        # Esse Loop foi feito para o caso do usuário for fazer um saque e acabar digitando errado e ele volte para que o usuário possa digitar novamente a quantia que deseja sacar.
        while True:

            # O Programa irá verificar se o que o usuário digitou está de acordo com o que se pede.
            try:

                # A opção onde será digitado o valor do saque.
                saldoSaque = int(input("Digite quanto você quer sacar R$ "))

                # Caso a quantia que o usuário deseja sacar for maior do que o que ele tem em sua conta, dará um erro e opção de digitar a quantia aparecerá novamente
                while saldoSaque > saldoDinheiro:
                    print('\nVocê não possui saldo suficiente.\n')
                    saldoSaque = int(input("\nDigite quanto você quer sacar R$ "))
                
                # A quantia digitada para poder fazer o saque tem que ser positiva.
                while saldoSaque < 0:
                    print('\nErro - Digite números positivos.\n')
                    saldoSaque = int(input("\nDigite quanto você quer sacar R$ "))

                # Imprimirá na tela a quantia em que foi sacada da conta do usuário.
                print(f"\nVocê sacou: R$ { saldoSaque} de sua conta.")

                # Fará a subtração do saldo que o usuário tem na conta menos a quantia que ele quer sacar.
                saldoDinheiro -= saldoSaque

                # Vai parar o Loop e voltará para o Menu inícial ao usuário.
                break

            # Se a verificação feita pelo programa for falsa, ele dará um erro.
            except:
                print('\nIsso não é um valor válido, digite novamente\n')

                # O Programa recomecará na opção de colocar a quantia para fazer o saque.
                continue

    # Caso a opção escolhhida seja o 4 ou seja sair, ele encerrará o programa.
    else:
        print("Sua operação acabou. Volte sempre!")

        # Vai parar o Loop do caixa e encerrará o programa.
        break