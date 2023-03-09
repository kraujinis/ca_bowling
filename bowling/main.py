import random
import keyboard
import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


class Throws:
    def __init__(self, player_name: str) -> None:
        self.player_name: str = player_name

    def random_number(self) -> int:
        '''Generate one random number
        for first throw'''
        rnd_nmb = random.randint(0, 10)
        logging.info(f'Random number value: {rnd_nmb}')
        return rnd_nmb

    def throw(self, thr: int) -> int:
        '''Generate random number for second throw
            output:
                throw:int
                    second generated max number is minus
                    previous random'''
        rnd_nmb = random.randint(0, 10 - thr)
        logging.info(f'Second throw value: {rnd_nmb}')
        return rnd_nmb

    def values_of_throw(self) -> list:
        '''Generate at least two throws
        with STRIKE and SPARE output string
        also in values of throws or how pins
        was knocked out'''
        throw_list = []
        keyboard.wait('space')
        rnd_nmb = self.random_number()
        print(f'You knock down \u001b[44m{rnd_nmb}\u001b[0m pin, -s')
        throw_list.append(rnd_nmb)
        logging.info(f'values_of_throws, first throw {rnd_nmb}')

        if throw_list[0] == 10:
            print('    >>>> \u001b[31mSTRIKE\u001b[0m <<<<')

        elif throw_list[0] != 10:
            keyboard.wait('space')
            second_throw = self.throw(rnd_nmb)
            logging.info(f'values_of_throws, second throw {rnd_nmb}')
            print(f'You knock down \u001b[44m{second_throw}\u001b[0m pin, -s')
            throw_list.append(second_throw)

            if sum(throw_list) == 10:
                print('    ---- \u001b[33mSPARE\u001b[0m ----')

        return throw_list

    def last_throw(self) -> list:
        '''Last FRAME [10] throws
            that code generates last two or
            three throws. Its depends what was
            value of first throw in FRAME[10]'''
        throw_list = []

        while True:
            keyboard.wait('space')
            rnd_nmb = self.random_number()
            logging.info(f'last_throws, first throw {rnd_nmb}')

            if rnd_nmb == 10:
                print(f'You knock down \u001b[44m{rnd_nmb}\u001b[0m pin, -s')
                print('    >>>> \u001b[31mSTRIKE\u001b[0m <<<<')
                logging.info(f'last_throws, STRIKE {rnd_nmb}')
                throw_list.append(rnd_nmb)

            elif rnd_nmb < 10:
                print(f'You knock down \u001b[44m{rnd_nmb}\u001b[0m pin, -s')
                logging.info(f'last_throws, < 10 first throw {rnd_nmb}')
                throw_list.append(rnd_nmb)

                if len(throw_list) == 3:
                    break
                
                keyboard.wait('space')
                second_rnd = self.throw(rnd_nmb)
                throw_list.append(second_rnd)
                logging.info(f'last_throws, < 10 second throw {rnd_nmb}')
                print(f'You knock down \u001b[44m{second_rnd}\u001b[0m pin, -s')

                if second_rnd + rnd_nmb == 10:
                    print('    ---- \u001b[33mSPARE\u001b[0m ----')
                else:
                    break

                if len(throw_list) == 3:
                    break

                keyboard.wait('space')
                third_rnd = self.random_number()
                throw_list.append(third_rnd)
                logging.info(f'last_throws, < 10 third throw {rnd_nmb}')
                print(f'You knock down \u001b[44m{third_rnd}\u001b[0m pin, -s')
                break

        return throw_list


class Result(Throws):
    def __init__(self, player_name: str) -> None:
        super().__init__(player_name)

    def values_of_frame(self) -> dict:
        dic_val_of_frm = {}
        i = 0

        while i < 10:
            print(f'      |\u001b[40;1m {i + 1} FRAME |\u001b[0m')
            i += 1
            values = []
            if i <= 9:
                val_of_throw = self.values_of_throw()
                for n in val_of_throw:
                    values.append(n)

            if i == 10:
                last_throws = self.last_throw()
                for n in last_throws:
                    values.append(n)

            dic_val_of_frm[str(i)] = values
        print('      \u001b[4m\u001b[1mEND of GAME\u001b[0m')

        return dic_val_of_frm

    def result_of_frames(self) -> dict:
        '''Sum results of throws in Frames
            And return dictionary {str, int}
                                  {'1': 10}'''

        frame_score = {}

        nmb_of_thrw = self.values_of_frame()

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

    def format_result_of_frame(self) -> list:
        formated_result = []
        for value in self.values_of_frame().values():
            if value[0] != 10:
                if sum(value) == 10:  # SPARE
                    spare_convert = str(value[0]) + '|' + '/'
                    formated_result.append(spare_convert)
            if value[0] == 10:
                formated_result.append('X')
            if len(value) == 2:
                if value[0] + value[1] != 10:
                    formated_result.append(str(value[0]) + '|' + str(value[1]))
            if len(value) == 3:
                if value[0] == 10:  # STRIKE + SPARE
                    if value[1] + value[2] == 10:
                        last_throw_format_one = 'X' + '|' + str(value[1]) + '|' + '/'
                        formated_result.append(last_throw_format_one)
                if value[0] + value[1] == 10:  # SPARE + values
                    if value[2] != 10:
                        last_throw_format_two = str(value[0]) + '|' + '/' + str(value[2])
                        formated_result.append(last_throw_format_two)
        return formated_result

    def total_score_of_frames(self) -> int:
        total_score = []
        for n in self.result_of_frames().values():
            total_score.append(n)
        return sum(total_score)

    def player_name_and_total_score(self) -> None:

        print(f'\nScore of frames: {self.format_result_of_frame()}')
        print(f'\nPlayer name: \u001b[4m\u001b[44m{self.player_name}\u001b[0m')


name = input('Write you name and push ENTER: ')

r = Result(name)
r.player_name_and_total_score()