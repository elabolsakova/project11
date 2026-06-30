def start_game():
    crystals = 21
    turn = input("Хотите ходить первым? (да/нет): ").strip().lower()
    human_first = (turn == "да")
    play_game(human_first, crystals)
