a = input('Proszę podać wyrazy: ')


# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


words = convert(a)
# print(words)


for word in words:
    if len(word) % 2 == 0:
        print(word.upper(), end=" ")
    if len(word) % 2 != 0:
        print(word, end=" ")
