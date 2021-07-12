sentence = input('Proszę podać zdanie: ')


# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


pig = convert(sentence)
# print(pig)


for word in pig:
    print((word[1:] + word[0] + 'ya'), end=' ')
    # (item, end=' ') drukowanie w jednej linijce