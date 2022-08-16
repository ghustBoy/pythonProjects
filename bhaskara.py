import re
import math

n = int(input())
deltas = []
dig1 = []
dig2 = []
for i in range(n):
    texto = input()
    dig1.append(texto)
    dig = [int(s) for s in re.findall(r'-?\d+\.?\d*', texto)]
    a = dig[0]
    b = dig[2] 
    c = dig[3]
    dig2.append(b)
    dig2.append(a)
    
    delta = b ** 2 - 4 * a * c
    deltas.append(delta)
  

print(dig2)
for d in range(len(deltas)):
  if deltas[d] == 0:
    x = (dig2[d] + math.sqrt(deltas[d])) / (2 * dig2[d + 1])
    print(f"Test {d+1}:", dig1[d])
    print(f"X = {x:.2f}")

  elif deltas[d] > 0:
    x1 = (-dig2[d] + math.sqrt(deltas[d])) / (2 * dig2[d + 1])
    x2 = (-dig2[d] - math.sqrt(deltas[d])) / (2 * dig2[d + 1])
    print(f"Test {d+1}:",  dig1[d])
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")
  
  else:
    x = 0
    print("SEM RESPOSTA")


