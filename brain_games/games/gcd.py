from random import randint


def get_question_and_answer():
    a = randint(0, 100)
    b = randint(0, 100)
    question = f'{a}, {b}.'
    while a != b:
        if a == 0 or b == 0:
            break
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a
    answer = max(a, b)
    return question, answer


def show_question():
    return 'Find the greatest common divisor of given numbers.'
