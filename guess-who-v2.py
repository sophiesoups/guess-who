import os

characters = ["Katie", "Mike", "Farah", "Daniel", "Emma", 
              "Carmen", "Amy", "Al", "Sam", "Mia", "David",
              "Joe", "Lily", "Leo", "Nick", "Laura", "Rachel",
              "Ben", "Sofia", "Gabe", "Olivia", "Liz", "Eric", "Jordan"]

players = ["Conor", "Sophie"]

board = {p: list(characters) for p in players}
log = []

def ask_names(player):
    names = input(f"{player}, who would you eliminate? (comma separated): ")
    os.system("cls" if os.name == "nt" else "clear")
    return [n.strip() for n in names.split(",") if n.strip()]


def ask_question(asker, other):
    print(f"\n{asker}'s turn. Remaining characters: {', '.join(board[asker])}")
    question = input("Your question: ")

