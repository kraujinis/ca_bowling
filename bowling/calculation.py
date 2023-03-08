import random
import keyboard
import logging


logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


# Generuojamas atsitiktinis skaičius, pirmas metimas
def random_number() -> int:
    rnd_nmb = random.randint(0, 10)
    return rnd_nmb


# Generuojamas sekantis metimas
def throw(thr: int) -> int:
    rnd_nmb = random.randint(0, 10 - thr)
    return rnd_nmb


# Generuojami du metimai, naudojama iki 9 Frame
def values_of_throw() -> list:

    throw_list = []
    keyboard.wait('space')
    rnd_nmb = random_number()
    print(f'You knock down {rnd_nmb} pins')
    throw_list.append(rnd_nmb)

    if throw_list[0] == 10:
        print('>>>> STRIKE <<<<')

    elif throw_list[0] != 10:
        keyboard.wait('space')
        second_throw = throw(rnd_nmb)
        print(f'You knock down {second_throw} pins')
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

        if rnd_nmb == 10:
            print('>>>> STRIKE <<<<')
            print(f'You knock down {rnd_nmb} pins')
            throw_list.append(rnd_nmb)

        elif rnd_nmb < 10:
            print(f'You knock down {rnd_nmb} pin, -s')
            throw_list.append(rnd_nmb)

            if len(throw_list) == 3:
                break
            keyboard.wait('space')
            second_rnd = throw(rnd_nmb)
            throw_list.append(second_rnd)
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

    return dic_val_of_frm


if __name__ == "__main__":

    values_of_frame()
    #last_throw()

# Paskaičiuoti rezultatą Framo
def values_of_frame():
    