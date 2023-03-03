import random

frame_score = []

throw = random.randint(0, 10)


if throw == 10:
    print('STRIKE')
    frame_score.append(throw)
elif throw != 10:
    frame_score.append(throw)
    print(f'Points for first throw: {throw}')
    if throw < 10:
        y = random.randint(0, 10 - throw)
        print(f'Points for second throw: {y}')
        frame_score.append(y)
    stride = throw + y
    if stride == 10:
        print('STRIDE')
        if stride == 0:
            print('!! 0 !!')


print(frame_score)