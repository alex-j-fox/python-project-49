from random import randint

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(a, b):
    while a != b:
        if min(a, b) == 0:
            return max(a, b)
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a
    return max(a, b)


def get_question_and_answer():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    question = f'{number_1} {number_2}.'
    answer = get_greatest_common_divisor(number_1, number_2)
    return question, answer
