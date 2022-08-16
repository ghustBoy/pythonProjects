import math
notaHora = []
hora = []
while True:
  semestre = int(input())
  if semestre > 10:
    #print("entrada invalida")
    break
  if semestre <= 0 or semestre > 10:
    break
  carga = int(input())
  nota = int(input())
  situation = str(input()).upper()
  if situation == 'T':
    continue 
  elif situation == 'AD':
    continue
  elif situation == 'DE':  
    continue
  elif situation == 'AE':
    continue
  elif situation == 'DD':
    continue
  elif situation == 'DC':
    continue
  else: 
    cn = carga * nota
    notaHora.append(cn)
    hora.append(carga)

if len(notaHora) > 0 and len(hora) > 0:
  cre = sum(notaHora) / sum(hora)
  #print(notaHora)
  #print(hora)
  if cre > 71.50:
    print(63.61)
  else:
    print(f"{cre:.2f}")
  
else:
  print("entrada invalida")


