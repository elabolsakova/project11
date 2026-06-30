def check_winner(crystals_left, last_mover):
    if crystals_left == 0:
        return 'computer' if last_mover == 'human' else 'human'
    return None
