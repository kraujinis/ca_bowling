
from getkey import getkey, keys
import calculation as calc
import random
import time


class Player:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score



    


throw_points = []



while True:
    
    
    key = getkey()
    rnd_number = random.randint(0, 10)
    
    if key == keys.UP:
        if rnd_number == 10:
            throw_points.append(rnd_number)
            print('STRIKE')
            break
        while True:
            if key == keys.UP:
                if rnd_number != 10:
                    throw_points.append(rnd_number)
                    print(f'first number: {rnd_number}')
                    time.sleep(1)
                    key == 0
                if key == keys.UP:
                    a = random.randint(0, 10 - rnd_number)
                    throw_points.append(a)
                    print(f'second number: {a}')
                    if (rnd_number + a) == 10:
                        print('STRIDE')
                    break


print(throw_points)

