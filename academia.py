dados = []
entrada = input()
counter = 1

while entrada != "SAIR" and counter < 100:
  dados.append(entrada)
  entrada = input()
  counter += 1 

senhas = []
entrada = input()

while entrada != '-1':
  senhas.append(entrada)
  entrada = input()

for senha in senhas:
  if senha in dados:
    indice = dados.index(senha)
    nome = dados[indice - 1]
    payment = dados[indice + 1]
    if payment == 'P':
      print(f"{nome}, seja bem-vindo(a)!")
    else:
      print(f"Não está esquecendo de algo, {nome}?, Procure a recepção!")   
  else:
    print("Seja bem-vindo(a)! Procure a recepção!")

  

