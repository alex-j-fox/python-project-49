from random import randint


def get_random_number():
    return randint(0, 100)


def get_question_and_answer():
    a = get_random_number()
    b = get_random_number()
    question = f'{a}, {b}.'
    if a == b:
        return question, a
    else:
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
