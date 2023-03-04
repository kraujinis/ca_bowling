
from calculation import throw_calculation


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score


print(throw_calculation())
