from random import randint


def get_question_and_answer():
    a = randint(0, 100)
    b = randint(0, 100)
    question = f'{a} {b}.'
    while a != b:
        if min(a, b) == 0:
            return question, max(a, b)
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a
    return question, max(a, b)


def show_question():
    return 'Find the greatest common divisor of given numbers.'
