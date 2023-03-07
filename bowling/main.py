
from calculation import number_of_throws


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score


class Result:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    

a = Result.calculate_frame_score(**number_of_throws())
print(a)
