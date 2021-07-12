a = input('Proszę podać wyrazy: ')


# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


words = convert(a)


# wybieranie drukowanych wyrazów
for uppercase in words:
    if uppercase.isupper():
        print(uppercase, end=" ")