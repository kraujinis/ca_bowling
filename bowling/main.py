
from calculation import values_of_frame


class Player:
    def __init__(self, player_name: str,) -> None:
        self.player_name = player_name
        
    


class Result:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        print(self.kwargs)
        
    def dictionary_of_throw_values(self):
        
        print(self.kwargs)
        

          
calculate = Result()
calculate.dictionary_of_throw_values(**values_of_frame())

