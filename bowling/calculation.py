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
        else:
            throw_points.append(rnd_number)
            logging.info(f"Catched first throw if not STRIKE ! {rnd_number}")

            keyboard.wait('space')
            second_random = random.randint(0, 10 - rnd_number)
            throw_points.append(second_random)
            logging.info(f"Catched second throw if not STRIKE ! {second_random}")

            spare = rnd_number + second_random

            if spare == 10:
                print('SPARE !')
                logging.info(f"Catched SPARE ! {spare}")
                pass
            return throw_points
    


def number_of_throws():
    i = 0
    result = {}
    while i < 10:
        i += 1
        value_of_throw = throw()
        print(f'Got value from throw: {value_of_throw}')
        #if value_of_throw[0] == 10:  # paskui itraukti i apskaičiuojant koks tai metimas arba i įtraukti į [i][i]
        result[i] = value_of_throw
            
        print(f"Jau buvo {i} metimų")
    print(result)


if __name__ == "__main__":

    print(number_of_throws())
