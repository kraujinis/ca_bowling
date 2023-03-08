import random
import keyboard
import logging


logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


# def one_throw() -> int:
#     keyboard.wait('space')  # wait 'space' push
#     rnd_number = random.randint(0, 10)  # start generate random number
#     return rnd_number


# def throws() -> list:  # Metimai

#     throw_points = []

#     while True:

#         keyboard.wait('space')  # wait 'space' push
#         rnd_number = random.randint(0, 10)
#         print(f'Gauti taškai: {rnd_number}')

#         if rnd_number == 10:
#             print('^ ^ STRIKE ^ ^')
#             throw_points.append(rnd_number)
#             logging.info(f"Catched STRIKE ! {rnd_number}")
#             return throw_points
#         else:
#             throw_points.append(rnd_number)
#             logging.info(f"Catched first throw if not STRIKE ! {rnd_number}")
#             keyboard.wait('space')
#             second_random = random.randint(0, 10 - rnd_number)
#             print(f'Gauti taškai: {second_random}')
#             throw_points.append(second_random)
#             logging.info(f"Catched second throw if not STRIKE ! {second_random}")
#             spare = rnd_number + second_random

#             if spare == 10:
#                 print('_ _ SPARE _ _')
#                 logging.info(f"Catched SPARE ! {spare}")
#             return throw_points


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


# def number_of_throws() -> dict:  # Užėjimai ir metimai, metimo vertės užrašymas
#     i = 0
#     result = {}
#     while i < 10:
#         print(f"> {i + 1} < BANDYMAS")
#         i += 1

#         result[str(i)] = throws()

#         if i == 10:
#             if result[str(i)][0] == 10:  # STRIKE
#                 last_throw = []
#                 last_throw.append(result[str(i)][0])
#                 for _ in range(1):
#                     a = throws()
#                     print(f'Gauti taškai: {a}')
#                     last_throw.append(a)
                
#                 result[str(i)] = last_throw
#                 break

#             elif sum(result[str(i)]) == 10:  # SPARE
#                 spare_list = []

#                 for n in result[str(i)]:
#                     spare_list.append(n)

#                 b = one_throw()
#                 print(f'Gauti taškai: {b}')
#                 spare_list.append(b)
#                 result[str(i)] = spare_list
#                 break

#     return result


# def calculate_frame_score() -> dict:

#     nmb_of_thrw = number_of_throws()
   
#     frame_score = {}

#     for key, value in nmb_of_thrw.items():

#         if len(value) == 2:  # SPARE
#             if sum(value) == 10:
#                 spare_value = []
#                 for i in value:
#                     logging.info(f"SPARE area, i value ! {i}")
#                     spare_value.append(i)
#                 int_key = int(key) + 1
#                 a = nmb_of_thrw.get(str(int_key))
#                 logging.info(f"SPARE area, a value ! {a}")
#                 spare_value.append(a[0])
#                 frame_score[key] = sum(spare_value)

#             else:
#                 frame_score[key] = sum(value)

#         elif len(value) == 3:
#             frame_score[key] = sum(value)

#         strike_value = []

#         if value[0] == 10:  # STRIKE
#             for i in range(0, 3):
#                 if len(strike_value) == 3:
#                     break
#                 int_x = int(key) + i
#                 a = nmb_of_thrw.get(str(int_x))

#                 if a == 10:
#                     strike_value.append(a[0])
#                 else:
#                     h = nmb_of_thrw.get(str(int_x))
#                     for r in h:
#                         if len(strike_value) == 3:
#                             break
#                         strike_value.append(r)
                        
#             frame_score[key] = sum(strike_value)
#     print(frame_score)
#     return frame_score

def throw(thr: int) -> int:
    rnd_nmb = random.randint(1, 10 - thr)
    return rnd_nmb
    
    
def random_number() -> int:
    rnd_nmb = random.randint(9, 10)  # TODO: pakeisti 9 -> 1
    return rnd_nmb


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


def last_throw() -> list:
    
    throw_list = []
    
    i = 0
    while i < 3:
        
        i += 1
        #list_of_values = []
        keyboard.wait('space')
        rnd_nmb = random_number()
        
        if rnd_nmb == 10:
            print('>>>> STRIKE <<<<')
            print(f'You knock down {rnd_nmb} pins')
            throw_list.append(rnd_nmb)
            
        # else:
        #     throw_list.append(rnd_nmb)
        #     print(f'You knock down {rnd_nmb} pins')
        
        elif rnd_nmb < 10:
            second_throw = throw(rnd_nmb)
            print(f'You knock down {second_throw} pins ---')
            throw_list.append(second_throw)
            
        elif 
            
        
    print(throw_list)
    return throw_list

if __name__ == "__main__":

    # calculate_frame_score()
    #number_of_throws()
    
    def values_of_frame() -> dict:
        
        dic_val_of_frm = {}
        
        i = 0
        
        while i < 3:  # TODO: padaryti vėliau 10
            print(f'| {i + 1} FRAME |')
            print('įprastas metimas')
            i += 1
            values = []
            val_of_throw = values_of_throw()
            
            if len(dic_val_of_frm) <= 2:  # TODO: pakeisti į 9
                
                for n in val_of_throw:
                    values.append(n)
            
            if i == 3:  # TODO: pakeisti į 10
                last_throw_values = []
                
                
                if val_of_throw[0] == 10:  # TODO: str[3] pakeisti į 10
                    print('Pagavo STRIKE paskutiniame metime')
                    last_throw = values_of_throw()
                    for n in last_throw:
                        last_throw_values.append(n)
                    
                # if len(last_throw_values) == 3:
                #     break
                    
                elif sum(val_of_throw) == 10:
                    print('Pagavo SPARE paskutiniame metime')
                    last_throw = values_of_throw()
                    
                    for n in last_throw:
                        
                        last_throw_values.append(n)
                        print(last_throw)
                        break
                for n in last_throw_values:
                    values.append(n)
                
            dic_val_of_frm[str(i)] = values
            
# [x]: STRIKE po to SPARE bet dar prasisuka ir vienas STRIKE   BAD   
# [x]: Po pirmo SPARE dar prasisisuka antras SPARE BAD   
# [ ]: Po STRIKE ir spare neįsirašo į listą rezultatas     
                    
                
            
        print(dic_val_of_frm)
        return dic_val_of_frm
    
    #values_of_frame()
    last_throw()