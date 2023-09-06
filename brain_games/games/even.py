from random import randint

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


def get_question_and_answer():
    random_number = randint(0, 100)
    question = random_number
    answer = 'yes' if is_even_number(random_number) else 'no'
    return question, answer
