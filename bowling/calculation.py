import random
import keyboard
import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def throw() -> list:

    throw_points = []

    while True:

        keyboard.wait('space')  # wait 'space' push
        rnd_number = random.randint(0, 10)  # start generate random number

        if rnd_number == 10:
            throw_points.append(rnd_number)
            logging.info(f"Catched STRIKE ! {rnd_number}")
            return throw_points

        throw_points.append(rnd_number)
        logging.info(f"Catched first throw if not STRIKE ! {rnd_number}")

        keyboard.wait('space')
        second_random = random.randint(0, 10 - rnd_number)
        throw_points.append(second_random)
        logging.info(f"Catched second throw if not STRIKE ! {second_random}")

        stride = rnd_number + second_random

        if stride == 10:
            print('STRIDE !')
            logging.info(f"Catched STRIDE !! {stride}")
            break
        break
    return throw_points


def number_of_throws():
    a = throw()
    print(a)
    for _ in range(10):
        if a[0] == 10:
            print(a)
            print("STIKE")
            
    
if __name__ == "__main__":
    
    print(number_of_throws())
