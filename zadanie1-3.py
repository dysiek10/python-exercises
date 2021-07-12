a = float(input('Podaj wartość bitcoina: '))
b = float(input('Podaj procent wzrostu/spadku: '))

income = a * b
value = a + income

if b >= -1 and b <= 1:
    print('Aktualna wartość Twoich bitcoinów to', value,".",'Zyskałeś/straciłeś', income)
else:
    print('Błędna wartość! Podaj wartość z przedziału (-1,1)')





