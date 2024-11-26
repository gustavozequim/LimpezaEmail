from setting import USR, SENHA

from imaplib import IMAP4_SSL

conexao = IMAP4_SSL('imap.gmail.com')
conexao.login(USR, SENHA)
ids = conexao.list()
print(ids)

