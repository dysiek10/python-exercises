a = input('Proszę podać wyrazy: ')


# definicja konwersji stringa na listę
def convert(string):
    li = list(string.split(' '))
    return li


words = convert(a)
# print(words)


for palindrom in words:
    # if len(palindrom) % 2 != 0:
    #     print(palindrom[:len(palindrom) // 2+1])
    #     print(palindrom[:len(palindrom) // 2-1:-1])
    # elif len(palindrom) % 2 == 0:
    #     print(palindrom[:len(palindrom) // 2])
    #     print(palindrom[:len(palindrom) // 2-1:-1])
    if len(palindrom) % 2 != 0 and palindrom[:len(palindrom) // 2+1] == palindrom[:len(palindrom) // 2-1:-1]:
        print(palindrom, end=" ")
    if len(palindrom) % 2 == 0 and palindrom[:len(palindrom) // 2] == palindrom[:len(palindrom) // 2-1:-1]:
        print(palindrom, end=" ")

    # if palindrom[:len(palindrom)//2 + 1] == palindrom[len(palindrom)//2:]:
    #     print(palindrom, end=" ")


########################################
# Zadanie 5 seria 2
#  OK
########################################
# lista=input("wprowadz wyrazy: ")
# lista=lista.split()
# result=[]
# for  wyraz in lista :
#     lenght = int(len(wyraz) / 2)
#     palindrom=True
#     for j in range(lenght):
#         if wyraz[j - 1] != wyraz[-j]:
#             palindrom = False
#     if palindrom :
#         result.append(wyraz)
# print(f"lista {result}")