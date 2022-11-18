import rsa
import hashlib
import zipfile

with open('public.pem', 'rb') as file:
  public_key = rsa.PublicKey.load_pkcs1(file.read())
# III - O programa ler um arquivo e gera um hash
with open('mensagem.txt', "r") as file:
  mensagem = file.read()

hsh = hashlib.sha256(mensagem.encode('utf-8')).hexdigest()

hashCrypted = rsa.encrypt(hsh.encode(), public_key)

with open('hashCriptografado.txt', 'wb') as file:
  file.write(hashCrypted)

# V - O programa cria um pacote .rar
z = zipfile.ZipFile('codigoCrypted.rar', 'w', zipfile.ZIP_DEFLATED)
z.write('mensagem.txt')
z.write('hashCriptografado.txt')
z.close()
