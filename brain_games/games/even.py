from random import randint


def is_even_number(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_question_and_answer():
    random_number = randint(0, 100)
    question = random_number
    answer = is_even_number(random_number)
    return question, answer


def show_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
