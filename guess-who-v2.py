import os

characters = ["Katie", "Mike", "Farah", "Daniel", "Emma", 
              "Carmen", "Amy", "Al", "Sam", "Mia", "David",
              "Joe", "Lily", "Leo", "Nick", "Laura", "Rachel",
              "Ben", "Sofia", "Gabe", "Olivia", "Liz", "Eric", "Jordan"]

players = ["Conor", "Sophie"]

log = []

def ask_names(player):
    names = input(f"{player}, who would you eliminate? (comma separated): ")
    os.system("cls" if os.name == "nt" else "clear")
    return [n.strip() for n in names.split(",") if n.strip()]


def ask_question(asker, other):
    print(f"\n{asker}'s turn.)")
    question = input("Your question: ")
    
    answers = {}
    print(f"Characters: {', '.join(characters)}")
    answers[other] = ask_names(other) 
    print(f"Question from {asker}: {question}")
    print(f"Characters: {', '.join(characters)}")
    answers[asker] = ask_names(asker)

    log.append({"asker": asker, "question": question, "answers": answers})


def show_results():
    for i, entry in enumerate(log, 1):
        asker = entry["asker"]
        other = players[1] if asker == players[0] else players[0]
        one = entry["answers"][asker]
        two = entry["answers"][other]
        agreed = [n for n in one if n.lower() in [t.lower() for t in two]]

        print(f"\nQ{i} (asked by {asker}): {entry['question']}")
        print(f"  {asker} thinks: {', '.join(one) or 'nobody'}")
        print(f"  {other} thinks: {', '.join(two) or 'nobody'}")
        print(f"  Agreed on: {', '.join(agreed) or 'nothing'}")


turn = 0
while True:
    asker = players[turn % 2]
    other = players[(turn + 1) % 2]
    ask_question(asker, other)

    if input("End the game? (y/n): ").strip().lower() == "y":
        break
    turn += 1

show_results()


