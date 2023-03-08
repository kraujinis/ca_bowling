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


def throws() -> list:  # Metimai

    throw_points = []

    while True:

        keyboard.wait('space')  # wait 'space' push
        rnd_number = random.randint(0, 10)
        print(f'Gauti taškai: {rnd_number}')

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
            print(f'Gauti taškai: {second_random}')
            throw_points.append(second_random)
            logging.info(f"Catched second throw if not STRIKE ! {second_random}")
            spare = rnd_number + second_random

            if spare == 10:
                print('_ _ SPARE _ _')
                logging.info(f"Catched SPARE ! {spare}")
            return throw_points


# def number_of_throws() -> None:
#     i = 0
#     result = {}
#     while i < 10:
#         print(f"> {i + 1} < BANDYMAS")
#         i += 1
#         value_of_throw = throws()
#         result[i] = value_of_throw

#         if i == 10:
#             if result[i][0] == 10:
#                 last_throw = []
#                 last_throw.append(result[i][0])

#                 for x in range(2):
#                     x += 2
#                     a = one_throw()
#                     print(f'{x}-as metimas. Gauti taškai: {a}')
#                     last_throw.append(a)

#                 result[i] = last_throw
#                 break

#             elif sum(result[i]) == 10:
#                 a = value_of_throw
#                 b = one_throw()
#                 print(f'3-as metimas. Gauti taškai: {b}')
#                 a.append(b)
#                 result[i] = a
#                 break

#     print(result)  # DEL


def number_of_throws() -> dict:  # Užėjimai ir metimai, metimo vertės užrašymas
    i = 0
    result = {}
    while i < 10:
        print(f"> {i + 1} < BANDYMAS")
        i += 1

        result[str(i)] = throws()

        if i == 10:
            if result[str(i)][0] == 10:  # STRIKE
                last_throw = []
                last_throw.append(result[str(i)][0])
                for _ in range(1):
                    a = throws()
                    print(f'Gauti taškai: {a}')
                    last_throw.append(a)
                
                result[str(i)] = last_throw
                break

            elif sum(result[str(i)]) == 10:  # SPARE
                spare_list = []

                for n in result[str(i)]:
                    spare_list.append(n)

                b = one_throw()
                print(f'Gauti taškai: {b}')
                spare_list.append(b)
                result[str(i)] = spare_list
                break

    return result


def calculate_frame_score() -> dict:

    nmb_of_thrw = number_of_throws()
   
    frame_score = {}

    for key, value in nmb_of_thrw.items():

        if len(value) == 2:  # SPARE
            if sum(value) == 10:
                spare_value = []
                for i in value:
                    logging.info(f"SPARE area, i value ! {i}")
                    spare_value.append(i)
                int_key = int(key) + 1
                a = nmb_of_thrw.get(str(int_key))
                logging.info(f"SPARE area, a value ! {a}")
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
    print(frame_score)
    return frame_score


if __name__ == "__main__":

    # calculate_frame_score()
    #number_of_throws()
    
    def throw():
        
        while True:
            i = []
            keyboard.wait('space')
            rnd_first = random.randint(9, 10)
            i.append(rnd_first)
            if i[0] == 10:
                return i
            else:
                keyboard.wait('space')
                rnd_second = random.randint(0, 10 - rnd_first)
                i.append(rnd_second)
            #print(i)
            return i
    print(throw())

