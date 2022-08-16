while True:
  lista = list()
  alimento = str(input().strip().split(',').append(lista))
  
  lista2 = list()
  kcal = int(input().strip().split(',').append(lista2))
  if input == '*':
    break

while True:
    t, meta = [int(x) for x in input().split()]
    if t == '*':
        break
while True:
    alimento3, quantidade = [int(x) for x in input().split()]
    if alimento3 and quantidade == 0:
        break
if t > meta:
  print("Acima da meta")
if t == meta:
  print("Exatamente na meta")
else:
  print("Abaixo da meta")
