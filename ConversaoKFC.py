escala = str(input())
temperatura = float(input())
if escala == 'K' and temperatura < 0.0 or escala == 'F' and temperatura < -459.67 or escala == 'C' and temperatura < -273:
  print("Valor de temperatura abaixo do minimo")  
else:
  if escala == 'K':
    fahrenheit = (temperatura - 273.15) * 9 / 5 + 32
    celsius = temperatura - 273.15
    print(f"{celsius:.2f} C")
    print(f"{fahrenheit:.2f} F")
  elif escala == 'F':
    celsius = (temperatura - 32) / 1.8
    kelvin = (temperatura - 32) * 5 / 9 + 273.15
    print(f"{celsius:.2f} C")
    print(f"{kelvin:.2f} K")
  elif escala == 'C':
    fahrenheit = temperatura * 1.8 + 32
    kelvin = temperatura + 273.15
    print(f"{fahrenheit:.2f} F")
    print(f"{kelvin:.2f} K")

