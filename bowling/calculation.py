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
    while i < 4: # TODO: buvo 10
        i += 1
        value_of_throw = throw()
        print(f'Got value from throw: {value_of_throw}')
        #if value_of_throw[0] == 10:  # paskui itraukti i apskaičiuojant koks tai metimas arba i įtraukti į [i][i]
        result[i] = value_of_throw
        if i == 4:  # TODO: buvo 10
            
            if value_of_throw[0] == 10:  # []: haha
                last_throw = []
 
                for i in range(2):
                    a = throw()
                    last_throw.append(a)
                    print('IF last throw: ', {a[0]})
                result[i] = last_throw
                break
            elif sum(value_of_throw) == 10:
                a = value_of_throw
                b = one_throw()
                a.append(b)
                result[i] = a  # TODO: pakeisti į [i]
                break
                
        print(f" {i} metimas")
    print(result)


if __name__ == "__main__":

    #print(number_of_throws())
    result = {}
    value_of_throw = [10, 5]
    if value_of_throw[0] == 10:
        last_throw = []
        last_of_throw.append()
        for _ in range(2):
            a = one_throw()
            last_throw.append(a)
            
            
        result[1] = last_throw
    print(result)
