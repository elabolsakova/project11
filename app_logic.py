
import random

def human_turn(crystals_left):
    while True:
        try:
            take = int(input(f"Ваш ход. Осталось {crystals_left} кристаллов. Сколько заберёте? (1–3): "))
            if 1 <= take <= min(3, crystals_left):
                return take
            else:
                print("Ошибка! Можно взять от 1 до 3 кристаллов.")
        except ValueError:
            print("Ошибка, введите целое число.")

def computer_turn(crystals_left):
    # Если можно оставить игроку кратное 4 — делаем это (это проигрышная для него позиция)
    if crystals_left > 4 and crystals_left % 4 != 0:
        comp_take = crystals_left % 4
    else:
        # Иначе ходим случайно, чтобы не выглядеть слишком предсказуемо
        comp_take = random.randint(1, min(3, crystals_left))
    print(f"Компьютер забирает {comp_take} кристаллов.")
    return comp_take

def play_game():
    total_crystals = 21  # Можно менять начальное количество
    print("Добро пожаловать в «Космические кристаллы»!")
    print("Правила: за ход можно взять 1–3 кристалла. Кто заберёт последний — проигрывает.")
    
    crystals_left = total_crystals
    
    while crystals_left > 0:
        print(f"\nОсталось кристаллов: {crystals_left}")
        
        # Ход игрока
        player_take = human_turn(crystals_left)
        crystals_left -= player_take
        if crystals_left == 0:
            print("Ой… Вы забрали последний кристалл! Реактор перегружен. Вы проиграли.")
            break
        
        # Ход компьютера
        comp_take = computer_turn(crystals_left)
        crystals_left -= comp_take
        if crystals_left == 0:
            print("Компьютер забрал последний кристалл… Реактор перегружен у него! Вы победили!")
            break

if __name__ == "__main__":
    play_game()
