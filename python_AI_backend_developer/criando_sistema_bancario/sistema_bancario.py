'''
- REGRAS DE NEGÓCIO

	- Regras DEPÓSITO
		Deve ser possível depositar valores positivos para a minha conta bancária.
		A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
		nos preocupar em identificar qual é o número da agência e conta bancária.
		Todos os depósitos devem ser armazenados em uma variável e exibidos na
		operação de extrato.
        A função de depósito deve receber os argumentos apenas por posição (positional only).
        Sugestão de args:
        - saldo,
        - valor,
        - extrato
        Sugestão de retorno:
        - saldo,
        - extrato
		
	- Regras SAQUE
		O sistema deve permitir realizar 3 saques diários com limite máximo de
		R$ 500.00 por saque. Caso o usuário não tenha saldo em conta, o sistema
		deve exibir uma mensagem informando que não será possível sacar o dinheiro
		por falta de saldo. Todos os saques devem ser armazenados em uma variável
		e exibidos na operação de extrato.
        A função de saque deve receber os argumentos apenas por nome (kayword only).
        Sugestão de args:
        - saldo,
        - valor,
        - extrato,
        - limite,
        - quantidade_saques,
        - limite_saques
        Sugestão de retorno:
        - saldo,
        - extrato
		
	- REGRAS EXTRATO
		Essa operação deve listar todos os depósitos e saques realizados na conta.
		No fim da listagem deve ser exibido o saldo atual da conta.
		Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
		
		Ex.:
		1500.45 = R$ 1500.45
        A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
        Args posicionais:
        - saldo
        Args nomeados:
        - extrato
    
    - REGRAS PARA CRIAÇÃO DE USUÁRIOS(Cliente)
		O programa deve armazenar os usuários em uma lista.
        Um usuário é composto por:
        - nome,
        - data de nascimento,
        - CPF,
        - endereço
        O endereço é uma string com o formato:
        - logradouro,
        - número,
        - bairro
        - cidade/UF
        O CPF deve ser armazenado somente os números.
        Náo podem haver dois usuários com o mesmo CPF.
        
    - REGRAS PARA CRIAÇÃO DE CONTAS CORRENTES
		O programa deve armazenar contas em uma lista.
        Uma conta é composta por:
        - agência,
        - número da conta
        - usuário
        O número da conta é sequencial, iniciando em 1.
        O número da agência é fixo: '0001'.
        Um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
'''
import textwrap

# MENU
def menu():
	menu = '''
	================= SELECIONE UMA OPÇÃO ======================
	[nu] - Novo Usuário
    [nc] - Novo Conta Corrente
    [lc] - Listar Contas Correntes
    [d] - Depositar
	[s] - Sacar
	[e] - Extrato
	[q] - Sair

	=> '''
	
	return input(textwrap.dedent(menu))

# CADASTRO DE USUÁRIOS
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Usuário já cadastrado com este CPF!')
    
    nome = input('Informe o nome completo do usuário: ')
    data_nascimento = input('Informe a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o endereço(logradouro, numero, bairro - cidade/estado(sigla)): ')
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
	})
    
    print('Usuário cadastrado com sucesso!')

# CADASTRO DE CONTAS CORRENTES
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
		}
    
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado!!')

# LISTAR CONTAS
def listar_contas(contas):
    for conta in contas:
        linha = f'''
			Agência:\t{conta["agencia"]}
			C/C:\t\t{conta["numero_conta"]}
			Titular:\t\t{conta["usuario"]["nome"]}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

# FILTRAR USUÁRIO
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# DEPOSITAR
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: de R$ {valor:.2f} realizado.\n'
        print('\n Depósito realizado com sucesso!')
    
    else:
        print('A operação falhou. O valor informado é inválido.')
    
    return saldo, extrato

# SACAR
def sacar(*, saldo, valor, extrato, limite, quantidade_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = quantidade_saques >= limite_saques
    
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
        print('\n Saque realizado com sucesso!')
    
    else:
        print('A operação falhou. O valor informado é inválido.')
    
    return saldo, extrato

# EXTRATO
def exibir_extrato(saldo, /, *, extrato):
    print('\n========== EXTRATO ==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==============================')

def main():
    LIMIE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite_saque = 500
    extrato = ''
    quantidade_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        opcao = str.lower(opcao)

        match str.lower(opcao):
            case "d":
                valor = float(input('Informe o valor do depósito: '))
                saldo, extrato = depositar(saldo, valor, extrato)

            case "s":
                valor = float(input('Informe o valor do saque: '))
                saldo, extrato = sacar(
					saldo=saldo,
					valor=valor,
					extrato=extrato,
					limite=limite_saque,
					quantidade_saques=quantidade_saques,
					limite_saques=LIMIE_SAQUES
				)

            case "e":
                exibir_extrato(saldo, extrato=extrato)

            case "nu":
                criar_usuario(usuarios)

            case "nc":
                numer_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numer_conta, usuarios)
                
                if conta:
                    contas.append(conta)

            case "lc":
                listar_contas(contas)

            case 'q':
                break

            case _:
                print('Opção inválida, por favor selecione novamente a operação desejada.')
                print('\n')
