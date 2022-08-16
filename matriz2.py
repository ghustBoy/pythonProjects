array = []
for i in range(9):
  array.append(int(input()))
somaP = []
for i in array:
  if i > 0:
    somaP.append(i)

    
media = sum(somaP) / len(somaP)
menor = min(array)
if menor % 2 == 0:
  delta = 1
else:
  delta = 0
soma = array[1] + array[2] + array[3] + array[5] + array[6] + array[7]
  
print(f"{media:.2f}", menor, delta, soma)
