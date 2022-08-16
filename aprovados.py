aprovados = []
while True:
  portugues = int(input())
  if portugues < 0:
    break
  math = int(input())
  red = float(input())
  if portugues >= 40 and math >= 21 and red >= 7:
    aprovados.append(1)
    
print(len(aprovados))
