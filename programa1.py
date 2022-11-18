import rsa
import hashlib
from zipfile import ZipFile

entrada = input("Você deseja Criar um Par de chaves S/N: ")[0].lower()

if entrada == 's':
  # I - Gerar Chaves
  public_key, private_key = rsa.newkeys(1024)
  # II - Salvar Chaves
  with open("public.pem", "wb") as file:
    file.write(public_key.save_pkcs1("PEM"))

  with open("private.pem", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))
else:
  # VI - O programa ler o conteúdo e gera o código hash
  z = ZipFile('codigoCrypted.rar', 'r')
  z.extractall()
  z.close()

  with open('mensagem.txt', 'r') as file:
    mensagem = file.read()

  newhsh = hashlib.sha256(mensagem.encode()).hexdigest()    

  with open('private.pem', 'rb') as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

  msgCrypted = open('hashCriptografado.txt', 'rb').read()

  # VII - o programa descriptografa o código
  msgDecrypted = rsa.decrypt(msgCrypted, private_key)
  
  # VIII - O programa compara os códigos hash
  if msgDecrypted.decode() == newhsh:
    print('Arquivo autêntico')
  else:
    print('Arquivo não Autêntico')
