valorGalao = float(input())
valorGasolina = float(input())
cotacaoDR = float(input())
litroEUA = valorGalao / 3.8 * cotacaoDR
print(f"Gasolina EUA: R$ {litroEUA:.2f}")
print(f"Gasolina Brasil: R$ {valorGasolina:.2f}")
if litroEUA > valorGasolina:
  print("Mais barata no Brasil")
elif valorGasolina > litroEUA:
  print("Mais barata nos EUA")
elif litroEUA == valorGasolina:
  print("Igual")
