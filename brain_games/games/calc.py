from random import randint, choice
from operator import add, mul, sub


def get_question_and_answer():
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    operator = choice('+-*')
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
