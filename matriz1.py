array = []
for i in range(9):
  array.append(int(input()))

media = sum(array) / 9
maior = max(array)
if maior > 0:
  delta = 1
elif maior == 0:
  delta = 0
else:
  delta = -1
soma = array[0] + array[4] + array[8]
  
print(f"{media:.2f}", maior, delta, soma)
