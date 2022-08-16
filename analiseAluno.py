media, aulas, faltas = input().split()
media = float(media)
aulas = int(aulas)
faltas = int(aulas)
frequencia = 100 * faltas / aulas
if media >= 5:
  if frequencia >= 75:
    print("APROVADO")
  else:
    print("REPROVADO")
else:
  if media >= 7:
    if frequencia >= 50:
      print("APROVADO")
    else:
      print("REPROVADO")
  else:
    print("REPROVADO")
  
