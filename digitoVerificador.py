import re
chaves = []
while True:
  chave = input()
  if chave != 'FIM':
    chaves.append(chave)
  if chave == 'FIM':
    break

for chave in chaves:
  key = re.split(r"[.-]", chave)
  maxdig = []
  for i in range(len(key)-1):
    j = key[i]
    x = max([int(a) for a in str(j)])
    maxdig.append(x)
    
  ultimoDigito = int(key[-1])
  digitoVerificador = sum(maxdig) % 10
  if digitoVerificador == ultimoDigito:
    print("VALIDO")
  else:
    print("INVALIDO")
