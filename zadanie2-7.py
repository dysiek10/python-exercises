a = input('Proszę podać liczby: ')


# definicja konwersji stringa na listę (funkcja :) )
def convert(string):
    li = list(string.split(' '))
    return li


numbers = convert(a)
# print(numbers)


for number in numbers:
    if number == max(numbers):
        print('maksimum to: ', number)
    if number == min(numbers):
        print('minimum to: ', number)

        # jak zrobić żeby tylko raz wyprintowało?