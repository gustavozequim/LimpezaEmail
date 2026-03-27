from setting import USR, SENHA

from imaplib import IMAP4_SSL

conexao = IMAP4_SSL('imap.gmail.com') # conexão com o servidor do gmail
conexao.login(USR, SENHA) # login com o email e senha
ids = conexao.list("INBOX")[1][0].decode().split(' ')[2].strip('"') # pega o id da caixa de entrada
conexao.select('INBOX') # seleciona a caixa de entrada para realizar as operações
status, data = conexao.search(None, 'ALL') # busca por todos os emails da caixa de entrada, o status é para verificar se a busca foi realizada com sucesso
ids = data[0].split() # divide os ids dos emails
print(f'Foram encontrados {len(ids)} emails.') # imprime a quantidade de emails encontrados
print(status)
conexao.logout() # desconecta do servidor
