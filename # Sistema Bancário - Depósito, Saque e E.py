# Sistema Bancário - Depósito, Saque e Extrato
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    menu = str(input(''' Selecione uma opção:

    D = Depositar
    E = Extrato
    S = Saque
    O = Sair
                     Você tem um limite de 3 saques por dia. 

    ''')).upper().strip()

    if menu == 'S':
      saque = int(input('Qual valor você deseja sacar? '))
      if saque <= extrato:
        extrato -= saque
        numero_saques += 1
        print(f'Obrigado por usar nossos serviços. Seu extrato atual é de: R${extrato:.2f}')
      else:
         print('Você não tem saldo suficiente para ser sacado.')
    
    elif menu == "D":
        deposito = int(input('Qual o valor que você deseja depositar? ')) 
        extrato += deposito 
        print(f'Obrigado por usar nossos serviços. Seu extrato atual é de: R${extrato:.2f}')
      

    elif menu == 'E':
        print(f'Esse é o seu extrato atual: R${extrato:.2f}')
       

    elif menu == 'O':
       print('Obrigado por usar nossos serviços, volte sempre!')
       break

    else:
     print('Essa opção não existe, escolha novamente: ')
     continue

    if numero_saques == LIMITE_SAQUES:
       print('Você atingiu o limite de saques dísponivel, volte depois.')

       

    




    

      
     
     



