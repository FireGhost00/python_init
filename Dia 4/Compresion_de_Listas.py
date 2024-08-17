palabra = 'python'

list = []

for letra in palabra:
    list.append(letra)



print(list)

list = [letra for letra in palabra]

list = [n for n in range(0,21,2) if n * 2 > 10]

print(list)

pies = [10,20,30,40,50]

metros = [round(p / 3.281,2) for p in pies]

print(metros)
