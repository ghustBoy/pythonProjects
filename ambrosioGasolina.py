km, reais, litro, postos, gasolina = [float(x) for x in input().split()]
gasto1 = (200 - litro * 10) / 10 * 4
gasto2 = reais - gasto1
if gasto2 <= 0:
  print("Nao pode viajar")
else:
  print("Pode viajar")
  print(f"{gasto2:.0f}")
