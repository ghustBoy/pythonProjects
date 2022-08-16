dias = int(input())
km = int(input())
valordias = dias * 30 
valorkm = km * 0.01
valorTotal = valordias + valorkm
desconto = valorTotal - (valorTotal * 0.1)
print(f"{desconto:.2f}")
