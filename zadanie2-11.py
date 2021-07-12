# Napisz program który sprawdza wynik gry w kamień papier nożyce. Program powinien przyjąć ruch pierwszego
# gracza, ruch drugiego a następnie wypisać wynik gry.

first = input("Podaj ruch 1 gracza: ")
second = input("Podaj ruch 2 gracza: ")


def rock_paper_scissors(first, second):

    # rozwiązanie przy użyciu słownika, nie ifów
    game_dict = {"rock": "scissors",
                 "scissors": "paper",
                 "paper": "rock"}

    if first == second:
        print("Remis")
        return
    if game_dict[first] == second:
        print("Wygrywa 1 gracz")
    else:
        print("Wygrywa 2 gracz")

rock_paper_scissors(first, second)

#     if first == "stone":
#         if second == "scissors":
#             return "Wygrywa 1"
#         if second == "paper":
#             return "Wygrywa 2"
#     if first == "scissors":
#         if second == "stone":
#             return "Wygrywa 2"
#         if second == "paper":
#             return "Wygrywa 1"
#     if first == "paper":
#         if second == "scissors":
#             return "Wygrywa 2"
#         if second == "stone":
#             return "Wygrywa 1"
#
# print(rock_paper_scissors("stone", "scissors"))