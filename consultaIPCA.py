meses = int(input())
anoMes = {}
for i in range(meses):
  anomes, indice = input().split()
  indice.replace(",", ".")
  anoMes[anomes] = indice

print(anoMes)

mes, mesAno, n = input().split()
#M 2/2021
while mes != '*':
  if mes == 'M':
    mes, mesAno = input().split()
    monthyear = []
    monthyear = mesAno.split("/")
    for i in range(len(monthyear)):
      month = monthyear[0]
      year = monthyear[1]
    
    month = '0'+ month
    ano = [year, month]
    ano = '-'.join(ano)
    print(anoMes[ano])
    break
  elif mes == 'P':
    mes, mesAno, n = input().split()
    monthyear = []
    monthyear = mesAno.split("/")
    for i in range(len(monthyear)):
      month = monthyear[0]
      year = monthyear[1]
    
    month = '0'+ month
    ano = [year, month]
    ano = '-'.join(ano)
    

#ano = '-'.join(monthyear)
print(ano)

