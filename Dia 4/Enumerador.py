lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

indice = 0

for indice,item in enumerate(lista):
    print(indice,item)

my_tuple = list(enumerate(lista))
print(my_tuple[1][1])