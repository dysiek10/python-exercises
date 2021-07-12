a = input('Proszę podać wyrazy: ')


# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


words = convert(a)


for longerThan5 in words:
    if len(longerThan5) > 5:
        print(longerThan5, end=" ")