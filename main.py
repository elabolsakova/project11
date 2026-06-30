import random

def human_turn(crystals):
    while True:
        try:
            taken = int(input(f"Осталось кристаллов: {crystals}. Сколько заберёте (1–3)? "))
            if 1 <= taken <= min(3, crystals):
                return taken
            print("Некорректное количество. Можно взять от 1 до 3 кристаллов.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def computer_turn(crystals):
    # Стратегия: оставить игроку кратное 4 (проигрышная позиция), если возможно
    taken = crystals % 4
    if taken == 0 or crystals <= 4:
        taken = random.randint(1, min(3, crystals))
    print(f"Компьютер забирает кристаллов: {taken}")
    return taken

def check_winner(crystals, last_player):
    """Возвращает имя победителя, если игра закончена, иначе None."""
    if crystals == 0:
        # Кто взял последний кристалл — тот проиграл
        return "Вы победили!" if last_player == "computer" else "Победил компьютер!"
    return None

def play_game(human_first, crystals):
    current_player = "human" if human_first else "computer"
    
    while crystals > 0:
        if current_player == "human":
            taken = human_turn(crystals)
        else:
            taken = computer_turn(crystals)
            
        crystals -= taken
        
        winner = check_winner(crystals, current_player)
        if winner:
            print(winner)
            break
            
        # Переключаем игрока
        current_player = "computer" if current_player == "human" else "human"

def start_game():
    print("--- Космические кристаллы ---")
    crystals = 21  # Стартовое количество
    turn = input("Хотите ходить первым? (да/нет): ").lower().strip()
    
    human_first = (turn == "да")
    play_game(human_first, crystals)

if __name__ == "__main__":
    start_game()
