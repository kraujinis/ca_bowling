
from calculation import values_of_frame, result_of_frames


class Game:
    def __init__(self, player_name: str,) -> None:
        self.player_name = player_name


class Result:

    def __init__(self, **kwargs):
        self.values = kwargs


    def dictionary_of_throw_values(self):
        print()


Result(**result_of_frames())

# SimpleNamespace(**{0:0})