corridas = int(input())
price = []

for i in range(corridas):
  x, y = map(float, (input().split()))
  valor = x * y

  primo = True
  for num in range(2, (int(valor // 1))):
    if (valor // 1) % num == 0:
        primo = False
        break
  if primo:
    valor -= valor * 0.42
  price.append(valor)
  
for valor in price:
  print(f"{valor:.2f}")



          
