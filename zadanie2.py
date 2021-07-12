# Napisz program, aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5
# między 1500 a 2700 (obie liczby uwzględnione)

for a in range(1500, 2701):
    if a % 5 == 0 and a % 7 == 0:
        print(a)
