from random import randint, choice
from operator import add, mul, sub

GAME_TASK = 'What is the result of the expression?'


def get_random_operator(number_1, number_2):
    operator = choice('+-*')
    if operator == '+':
        return operator, add(number_1, number_2)
    elif operator == '-':
        return operator, sub(number_1, number_2)
    elif operator == '*':
        return operator, mul(number_1, number_2)


def get_question_and_answer():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    operator, answer = get_random_operator(number_1, number_2)
    question = f'{number_1} {operator} {number_2}'
    return question, answer
