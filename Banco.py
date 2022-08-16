#Função que imprime uma linha com o tamanho determinado no parâmetro
def linhas(tamanho):
  print('-' * tamanho)
  

#Função responsável pelo depósito da quantia determinada 
def depositar(valor):
  user["balance"] += valor
  user["extract"].append({"tipo": "Depósito", "value": valor})
  print(f'\033[32mDepósito de R${valor:.2f} realizado com sucesso\033[m')
  linhas(45)

#Função responsável pelo saque da quantia determinada  
def sacar(valor):
  user["balance"] -= valor
  user["extract"].append({"tipo": "Saque", "value": valor})
  print(f'\033[31mSaque de R${valor:.2f} realizado com sucesso\033[m')
  linhas(45)

#Função responsável por mostrar o saldo do usuário
def saldo():
  print(f'\033[34mSeu saldo atual é de R${user["balance"]:.2f}\033[m')
  linhas(45)

#Função responsável por mostrar os dados da transação
def extrato():
  cont = 1
  linhas(45)
  print('')
  print('\033[34mExtrato:\033[m')
  print('')
  #Loop que itera pelas chaves do dicionário "user" e mostra a ordem, o tipo e o valor
  if(user["extract"] == []):
    print('\033[34mAinda não houve nenhuma movimentação na conta.\033[m')
  for movimentacao in user["extract"]:
    print(f'\033[34m{cont} - Tipo: {movimentacao["tipo"]}, Valor: R${movimentacao["value"]:.2f}\033[m')
    cont += 1
  print('')  
  linhas(45)

#Cria um dicionário que possui as chaves nome, saldo e extrato(esse ultimo que é uma lista)
user = {
  "name": "",
  "balance": 0,
  "extract": []
}

#Prints responsáveis pela apresentação/início do banco
print('\033[1mEste é o Banco EduHil \033[0m'.center(54))
linhas(45)
#A chave "name" recebe o valor do input 
user["name"] = str(input('Por favor, digite o seu nome: '))
linhas(45)

print(f'Seja bem-vindo(a), Sr(a) {user["name"]}!\n')

#Loop que garante a continuação das funções do programa até o digito 0 ser digitado
while True:
  print('Digite "0" para encerrar o programa')
  print('Digite "1" para Depositar')
  print('Digite "2" para Sacar')
  print('Digite "3" para Ver o saldo')
  print('Digite "4" para Ver o extrato')
  linhas(45)
  
  opcao = int(input('Informe qual operação você deseja realizar: '))
  print('')
  #Se a opção 0 for escolhida o programa é encerrado
  if(opcao == 0):
    print(f'Adeus, {user["name"]}')
    break
  #Se a opção 1 for digitada ocorre um depósito através da chamada da função depositar()  
  elif(opcao == 1):
    valor = float(input('Informe o valor do depósito: '))
    print('')
    depositar(valor)
    print('')
  #Se a opção 2 for digitada ocorre um saque através da chamada da função sacar()    
  elif(opcao == 2):
    #Verifica se o cliente possui saldo, antes de perguntar o valor do saque.
    if(user["balance"] == 0):
      print('Saldo igual a 0. Por favor deposite alguma quantia.')
      print('')
    else:
      valor = float(input('Informe o valor do saque: '))
      #Se o valor digitado pelo usuário for menor que o valor presente no saldo, há uma mensagem de erro
      if(user["balance"] < valor):
        print('\033[31mSaldo menor que o valor desejado para saque!\033[m')
      else:
        print('')
        sacar(valor)
        print('')
  #Se a opção 3 for escolhida é mostrado o saldo do/a cliente
  elif(opcao == 3):
    saldo()

  #Se a opção 4 for escolhida são mostrados os dados das transações recentes
  elif(opcao == 4):
    extrato()

  else:
    print(f'\033[31mOperação Inválida!\033[m')
