lista = []
while True:
  i, j = [int(x) for x in input().split()]
  if i == 0 and j == 0:
    break
  array = []
  for a in range(i, j+1):
    y = [int(z) for z in str(a)]
    for i in y:
      array.append(i)
  

  zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
  for i in array:
    if i == 0:
      zero += 1
    elif i == 1:
      um += 1
    elif i == 2:
      dois += 1
    elif i == 3:
      tres += 1
    elif i == 4:
      quatro += 1
    elif i == 5:
      cinco += 1
    elif i == 6:
      seis += 1
    elif i == 7:
      sete += 1
    elif i == 8:
      oito += 1
    elif i == 9:
      nove += 1
  
  lista.append(zero)
  lista.append(um)
  lista.append(dois)
  lista.append(tres)
  lista.append(quatro)
  lista.append(cinco)
  lista.append(seis)
  lista.append(sete)
  lista.append(oito)
  lista.append(nove)


x = 10
final_list = lambda lista, x: [lista[i:i+x] for i in range(0, len(lista), x)]

output = final_list(lista, x)


for j in output:
  for i in j:
    for d in range(9):
      print(i, end=" ")
      break
    


  
  
  
