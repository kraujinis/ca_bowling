import random
import keyboard
import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def throw_calculation() -> list:
    throw_points = []
    while True:

        rnd_number = random.randint(0, 10)  # start generate random number
        keyboard.wait('space')  # wait 'space' push

        if rnd_number == 10:
            throw_points.append(rnd_number)
            logging.info(f"Catched STRIKE !! {rnd_number}")
            print('STRIKE !')
            break

        keyboard.wait('space')
        throw_points.append(rnd_number)  # append first result of throw
        logging.info(f"Catched first throw if not STRIKE !! {rnd_number}")

        keyboard.wait('space')
        second_random = random.randint(0, 10 - rnd_number)
        throw_points.append(second_random)  # append second result of throw
        logging.info(f"Catched second throw if not STRIKE !! {second_random}")
        stride = rnd_number + second_random

        if stride == 10:
            print('STRIDE !')
            logging.info(f"Catched STRIDE !! {stride}")
            break
        break
    return throw_points


if __name__ == "__main__":
    throw_calculation()
