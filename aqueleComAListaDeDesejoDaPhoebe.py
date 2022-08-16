metasCumprir = []
meta0 = int(input())
for i in range(meta0): 
  metaCumprir = str(input())
  metasCumprir.append(metaCumprir)
meta1 = int(input())
for i in range(meta1):
  metaCumprida = str(input())
  if metaCumprida not in metasCumprir:
    continue
  else:
    metasCumprir.remove(metaCumprida)
if len(metasCumprir) == 0:
  print("Smelly Cat, Smelly Cat, what are they feeding you?")
else:
  print(f"Ainda falta(m) {len(metasCumprir)} objetivo(s)!")
  for i in metasCumprir:
    print(i)
