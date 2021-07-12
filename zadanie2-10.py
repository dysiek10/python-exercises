liczby = range(1, 51)

for a in liczby:
    if a % 3 == 0:
        if a % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    else:
        if a % 5 == 0:
            print('buzz')
        else:
            print(a)
        # można jeszcze uprościć sprawdzając czy dzieli się przez 15 na początku

        # def max3(x, y, z):
        #     """zwraca największą z 3 liczb"""
        #     if x > y:
        #         if x > z:
        #             return x
        #         else:
        #             return z
        #     else:
        #         if y > z:
        #             return y
        #         else:
        #             return z
