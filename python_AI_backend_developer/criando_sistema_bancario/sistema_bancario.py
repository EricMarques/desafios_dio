'''
  - REGRAS DE NEGÓCIO

  
	- Regras DEPÓSITO
		Deve ser possível depositar valores positivos para a minha conta bancária.
		A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
		nos preocupar em identificar qual é o número da agência e conta bancária.
		Todos os depósitos devem ser armazenados em uma variável e exibidos na
		operação de extrato.
		
	- Regras SAQUE
		O sistema deve permitir realizar 3 saques diários com limite máximo de
		R$ 500.00 por saque. Caso o usuário não tenha saldo em conta, o sistema
		deve exibir uma mensagem informando que não será possível sacar o dinheiro
		por falta de saldo. Todos os saques devem ser armazenados em uma variável
		e exibidos na operação de extrato.
		
	- REGRAS EXTRATO
		Essa operação deve listar todos os depósitos e saques realizados na conta.
		No fim da listagem deve ser exibido o saldo atual da conta.
		Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
		
		Ex.:
		1500.45 = R$ 1500.45
		
'''

menu = '''
================= SELECIONE UMA OPÇÃO ======================
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> '''

saldo = 0
limite_saque = 500
extrato = ''
quantidade_saques = 0
LIMIE_SAQUES = 3

while True:
    opcao = input(menu)
    opcao = str.lower(opcao)
    
    match str.lower(opcao):
        case "d":
            valor = float(input('Informe o valor do depósito: '))
            
            if valor > 0:
                saldo += valor
                extrato += f'Depósito: R$: {valor:.2f}\n'
                
            else:
                print('A operação falhou. O valor informado é inválido.')

        case "s":
            valor = float(input('Informe o valor do saque: '))
            
            saldo_excedido = valor > saldo
            
            limite_excedido = valor > limite
            
            saque_excedido = quantidade_saques >= LIMITE_SAQUES
            
            if saldo_excedido:
                print('A operação falhou. Saldo insuficiente.')
            
            elif limite_excedido:
                print('A operação falhou. O valor do saque excede o limite.')
                
            elif saque_excedido:
                print('A operação falhou. Quantidade de saques excedidas.')
                
            elif valor > 0:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                quantidade_saques += 1
            
            else:
                print('A operação falhou. O valor informado é inválido.')
                
        case "e":
            print('\n========== EXTRATO ==========')
            print('Não foram realizadas movimentações.' if not extrato else extrato)
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('==============================')
        
        case 'q':
            break
        
        case _:
            print('Opção inválida, por favor selecione novamente a operação desejada.')
            print('\n')
