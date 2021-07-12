words = input('Proszę podać wyrazy: ')

# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


lista = (convert(words))
# print(lista)

for word in lista:
    if word[-1] == 'a':
        print(word, end=' ')
