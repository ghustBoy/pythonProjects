mercadorias = {}
resultado = []

dado = input()
while dado != '9999':
  c, q = [int(x) for x in dado.split()] 
  mercadorias[c] = q
  dado = input()
print(mercadorias)

dado = input()
while dado != '9999':
  c, cod, q = [int(x) for x in dado.split()]

  if mercadorias[cod] >= q:
    resultado.append("OK")
    mercadorias[cod] -= q

  else:
    resultado.append("ESTOQUE INSUFICIENTE")
    
  dado = input()

for r in resultado:
  print(r)

for c in mercadorias:
  q = mercadorias[c]
  print(c, q)
  

    
      
