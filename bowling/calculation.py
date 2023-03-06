import random
import keyboard
import logging


logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def one_throw() -> int:
    keyboard.wait('space')  # wait 'space' push
    rnd_number = random.randint(0, 10)  # start generate random number
    return rnd_number


def throws() -> list:

    throw_points = []

    while True:

        keyboard.wait('space')  # wait 'space' push
        rnd_number = random.randint(0, 10)
        print(f'1-as metimas. Gauti taškai: {rnd_number}')

        if rnd_number == 10:
            print('^ ^ STRIKE ^ ^')
            throw_points.append(rnd_number)
            logging.info(f"Catched STRIKE ! {rnd_number}")
            return throw_points
        else:
            throw_points.append(rnd_number)
            logging.info(f"Catched first throw if not STRIKE ! {rnd_number}")
            keyboard.wait('space')
            second_random = random.randint(0, 10 - rnd_number)
            print(f'2-as metimas. Gauti taškai: {second_random}')
            throw_points.append(second_random)
            logging.info(f"Catched second throw if not STRIKE ! {second_random}")
            spare = rnd_number + second_random

            if spare == 10:
                print('_ _ SPARE _ _')
                logging.info(f"Catched SPARE ! {spare}")
            return throw_points


def number_of_throws() -> None:
    i = 0
    result = {}
    while i < 10:
        print(f"> {i + 1} < BANDYMAS")
        i += 1
        value_of_throw = throws()
        result[i] = value_of_throw

        if i == 10:
            if result[i][0] == 10:
                last_throw = []
                last_throw.append(result[i][0])

                for x in range(2):
                    x += 2
                    a = one_throw()
                    print(f'{x}-as metimas. Gauti taškai: {a}')
                    last_throw.append(a)

                result[i] = last_throw
                break

            elif sum(result[i]) == 10:
                a = value_of_throw
                b = one_throw()
                print(f'3-as metimas. Gauti taškai: {b}')
                a.append(b)
                result[i] = a
                break

    print(result)



    
    
if __name__ == "__main__":

    number_of_throws()
