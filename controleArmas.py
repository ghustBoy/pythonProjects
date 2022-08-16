nacionalidade = str(input())
ocupacao = str(input())
armas = int(input())
calibre = int(input())
if nacionalidade == 'E' and armas == 0 and calibre == 0:
  print("Liberado")
else:
  print("Barrado")
if nacionalidade == 'B' and ocupacao == 'M':
  print("Liberado")
if nacionalidade == 'B' and ocupacao == 'T' or 'O' and armas <= 1 and calibre <= 22:
  print("Liberado")
else:
  print("Barrado")      
if ocupacao == 'C' and armas <= 2 and calibre <= 38:
  print("Liberado")
else:
  print("Barrado")
      
      
    
    
  
