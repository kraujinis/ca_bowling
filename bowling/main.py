
from calculation import number_of_throws


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score


class Result:

    def __init__(self, **kwargs) -> None: # TODO: reikia sutvarkyti čia kažkaip paduoti į funkciją
        
        frame_score = {}
    
        for x, y in kwargs.items():
            
            if len(y) == 2: # SPARE
                if sum(y) == 10:
                    spare_value = []
                    for i in y:
                        spare_value.append(i)
                    a = kwargs.get(x + 1)

                    spare_value.append(a[0])
                    frame_score[x] = sum(spare_value)
                    
                else:
                    frame_score[x] = sum(y)
                    
            elif len(y) == 3:
                frame_score[x] = sum(y)
                
            elif len(y) == 1: # STRIKE
                strike_value =[]
                
                for i in range(3):
                    a = kwargs.get(x + i)
                    for s in a:
                        strike_value.append(s)
                        
                print(x, strike_value)
                frame_score[x] = sum(strike_value[:3])
        
        print(frame_score)




print(number_of_throws())
