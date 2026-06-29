def staet_game():
    sticks=21
    turn=input("Хотите ходить первым? (да/нет): ").strip().lower()
    if turn=="да":
        human_first=True
    else:
        human_first=False
    play_game(human_first,sticks)


