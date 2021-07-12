a = float(input('Podaj ilość inwestowanej gotówki: '))

b = float(input('Podaj cenę bitcoina: '))
e = float(input('Podaj cenę etherum: '))
l = float(input('Podaj cenę litecoina: '))

bitcoin = int(a // b)
etherum = int(a // e)
litecoin = int(a // l)

print('Za', a, 'zł', 'możesz kupić', bitcoin, 'x bitcoin,', etherum, 'x etherum lub', litecoin, 'x litecoin.')
