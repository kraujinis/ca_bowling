from getkey import getkey, keys


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score




key = getkey()
if key == keys.UP:
    print('keys UP')

