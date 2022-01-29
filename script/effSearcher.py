# effSearcher
# Dev. por: João V. Coelho
# GitHub:   https://github.com/joaovcoelho/



# SPLASH HEADER ====
print("\n", "=" * 14, "effSearcher", "=" * 14)
print("\n  | Version:  1.0  | Released on:  01/2022")
print("\n  | Dev. by:  João V. Coelho")
print("  | GitHub:  https://github.com/joaovcoelho/effSearcher\n")
print("=" * 41, "\n\n")



arquivo = input("Insira o nome completo do arquivo (precisa incluir o .txt)\n  >> ")
separador = ":"

credenciais = [] # Armazena login (ou usuário) e senha

def gera_credenciais():
	with open(arquivo) as base_dados:
		dados = base_dados.read() # Abre o arquivo todo
		linhas = dados.split() # Separa pela quebra de linha
		print(f'\n -=-=  A base "{arquivo}" contém {len(linhas)} credenciais =-=-')		

		for conta in (linhas): # Lê cada linha e cria a tabela
			posicao = conta.find(separador) # Encontra posição do separador
			login = conta[:posicao]
			senha = conta[posicao + 1:]
			credenciais.append((login, senha))
	
gera_credenciais() # Preenche a tabela de credenciais

def localiza_conta():
	print('\n\n\nDigite, diretamente, o que deseja verificar \n(login, e-mail, senha ou domínio (ex. @exemplo.com))')
	busca = input('>> ')
	
	indice = 0 # indice de itens
	for linha in credenciais:
		login = linha[0]
		senha = linha[1]
		
		# Busca por e-mail ou senha
		if busca == login or busca == senha:
			print(f" [{indice}]\n   |  Login:  {login}\n   |  Senha:  {senha}")
			indice += 1
			
		# Busca por domínio	
		posicao_arroba = login.find("@") # Encontra o domínio
		if busca == login[posicao_arroba:]: # Exibe todas as contas com o domínio
			print(f" [{indice}]\n   |  Login:  {login}\n   |  Senha:  {senha}")
			indice += 1

		# Busca independentemente do domínio	
		posicao_arroba = login.find("@") # Encontra o domínio
		if busca == login[:posicao_arroba]: # Exibe todas as contas com o domínio
			print(f" [{indice}]\n   |  Login:  {login}\n   |  Senha:  {senha}")
			indice += 1


while True:
	localiza_conta()
	
	
