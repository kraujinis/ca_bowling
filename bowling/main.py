
from calculation import values_of_throw


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score


class Result:

    def __init__(self, *args: list):
        self.args = args
        print(self.args)
        
    def dictionary_of_throw_values(self):
        
        i = 0
        print(self.args)
        #while i < 3:  # TODO: pakeisti į 10
            

    

a = Result.dictionary_of_throw_values(*values_of_throw())
print(a)
