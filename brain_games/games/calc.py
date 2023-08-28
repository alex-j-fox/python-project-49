from random import randint, choice
from operator import add, mul, sub


def get_random_number():
    return randint(0, 100)


def get_random_operator():
    return choice('+-*')


def get_question_and_answer():
    number_1 = get_random_number()
    number_2 = get_random_number()
    operator = get_random_operator()
    expression = f'{number_1} {operator} {number_2}'
    question = expression
    answer = None
    if operator == '+':
        answer = add(number_1, number_2)
    elif operator == '-':
        answer = sub(number_1, number_2)
    elif operator == '*':
        answer = mul(number_1, number_2)
    return question, answer


def show_question():
    return 'What is the result of the expression?'
