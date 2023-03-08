import random
import keyboard
import logging


logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


# Generuojamas atsitiktinis skaičius, pirmas metimas
def random_number() -> int:
    rnd_nmb = random.randint(0, 10)
    logging.info(f'Random number value: {rnd_nmb}')
    return rnd_nmb


# Generuojamas sekantis metimas
def throw(thr: int) -> int:
    '''
    Paduodama reikšmė iš random number
    '''
    rnd_nmb = random.randint(0, 10 - thr)
    logging.info(f'Second throw value: {rnd_nmb}')
    return rnd_nmb


# Generuojami du metimai, naudojama iki 9 Frame
def values_of_throw() -> list:

    throw_list = []
    keyboard.wait('space')
    rnd_nmb = random_number()
    print(f'You knock down {rnd_nmb} pin, -s')
    throw_list.append(rnd_nmb)
    logging.info(f'values_of_throws, first throw {rnd_nmb}')
    
    if throw_list[0] == 10:
        print('>>>> STRIKE <<<<')

    elif throw_list[0] != 10:
        keyboard.wait('space')
        second_throw = throw(rnd_nmb)
        logging.info(f'values_of_throws, second throw {rnd_nmb}')
        print(f'You knock down {second_throw} pin, -s')
        throw_list.append(second_throw)

        if sum(throw_list) == 10:
            print('--- SPARE ---')

    return throw_list


# Generuojami du arba trys paskutinio Frame metimai
def last_throw() -> list:

    throw_list = []

    while True:
        keyboard.wait('space')
        rnd_nmb = random_number()
        logging.info(f'last_throws, first throw {rnd_nmb}')
        
        if rnd_nmb == 10:
            print('>>>> STRIKE <<<<')
            print(f'You knock down {rnd_nmb} pin, -s')
            logging.info(f'last_throws, STRIKE {rnd_nmb}')
            throw_list.append(rnd_nmb)

        elif rnd_nmb < 10:
            print(f'You knock down {rnd_nmb} pin, -s')
            logging.info(f'last_throws, < 10 first throw {rnd_nmb}')
            throw_list.append(rnd_nmb)

            if len(throw_list) == 3:
                break
            keyboard.wait('space')
            second_rnd = throw(rnd_nmb)
            throw_list.append(second_rnd)
            logging.info(f'last_throws, < 10 second throw {rnd_nmb}')
            print(f'You knock down {second_rnd} pin, -s')

            if second_rnd + rnd_nmb == 10:
                print('--- SPARE ---')
            else:
                break

            if len(throw_list) == 3:
                break

            keyboard.wait('space')
            third_rnd = random_number()
            throw_list.append(third_rnd)
            logging.info(f'last_throws, < 10 third throw {rnd_nmb}')
            print(f'You knock down {third_rnd} pin, -s')

            break

    return throw_list


# Sugeneruojamas dictionary tipo masyvas, key: str, value: list
def values_of_frame() -> dict:

    dic_val_of_frm = {}
    i = 0

    while i < 10:
        print(f'| {i + 1} FRAME |')
        i += 1
        values = []

        if i <= 9:
            val_of_throw = values_of_throw()
            for n in val_of_throw:
                values.append(n)

        if i == 10:
            last_throws = last_throw()
            for n in last_throws:
                values.append(n)

        dic_val_of_frm[str(i)] = values
    print(f'Values in frame of throws: {dic_val_of_frm}')
    return dic_val_of_frm


# Apskaičiuojamas Framų rezultatas
def result_of_frames() -> dict:

    frame_score = {}

    nmb_of_thrw = values_of_frame()

    for key, value in nmb_of_thrw.items():
        if len(value) == 2:  # SPARE
            if sum(value) == 10:
                spare_value = []
                for i in value:

                    spare_value.append(i)
                int_key = int(key) + 1
                a = nmb_of_thrw.get(str(int_key))

                spare_value.append(a[0])
                frame_score[key] = sum(spare_value)

            else:
                frame_score[key] = sum(value)

        elif len(value) == 3:
            frame_score[key] = sum(value)

        strike_value = []

        if value[0] == 10:  # STRIKE
            for i in range(0, 3):
                if len(strike_value) == 3:
                    break
                int_x = int(key) + i
                a = nmb_of_thrw.get(str(int_x))

                if a == 10:
                    strike_value.append(a[0])
                else:
                    h = nmb_of_thrw.get(str(int_x))
                    for r in h:
                        if len(strike_value) == 3:
                            break
                        strike_value.append(r)

            frame_score[key] = sum(strike_value)
    print(f'Score of frames: {frame_score}')
    return frame_score


if __name__ == "__main__":

    result_of_frames()
