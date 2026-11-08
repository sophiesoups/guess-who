characters = ["Amy", "Gabe", "Katie"]
players = ["Conor", "Sophie"]

board = {player: list(characters) for player in players}

game_log = []

turn = 0
while True:
    asker = players[turn % 2]
    answerer = players[(turn + 1) % 2]
    print(f"\n{asker}'s turn. Remaining: {', '.join(board[asker])}")

    question = input("Your question: ")
    print(f"{answerer}, which names does that eliminate for you?")
    names = input("Names (comma seperated): ")
    eliminated = [n.strip() for n in names.split(",") if n.strip()]
    board[asker] = [c for c in board[asker] if c.lower() not in [e.lower() for e in eliminated]]
    game_log.append((asker, question, eliminated))

    if input("End the game? (y/n): ").strip().lower() == "y":
        break
    turn += 1



for p in players:
    print(f"\n Questions {p} asked: ")
    for asker, q, elim in game_log:
        if asker == p:
            print(f" Q: {q}\n   Eliminated: {', '.join(elim) or 'nobody'}")


