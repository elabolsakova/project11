def human_turn(sticks_left):
    while True:
        try:
            take=int(input(f"Ваш ход. Осталось {sticks_left} спичек. Сколько возьмете? (1-3)"))
            if 1<= take <= min(3, sticks_left):
                return take
            else:
                print("Ошибка! Можно взять от 1 до 3 спичек")
        except ValueError:
            print("Ошибка, введите целое число")

def computer_turn(sticks_left):
    if sticks_left >= 4 and sticks_left % 4 != 0:
        comp_take = sticks_left % 4
    else:
        comp_take = random.randint(1, min(3, sticks_left))
    print(f"Компьютер берет {comp_take} спичек")
