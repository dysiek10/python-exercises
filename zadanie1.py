# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for

a = input('Podaj 1 liczbę: ')
b = input('Podaj 2 liczbę: ')

liczby = range(1, 50)


for x in liczby:
    x > 0
    if a % x == 0 and b % x == 0 and a < b:
        print('Największy wspólny dzielnik podanych liczb to', max(liczby))
