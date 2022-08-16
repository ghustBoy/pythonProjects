def lista(list):
  media = (sum(list)) / len(list)
  print(media)

list = [float(x) for x in input().split()]
lista(list)
