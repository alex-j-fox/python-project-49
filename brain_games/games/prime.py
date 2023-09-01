from random import randint


def get_question_and_answer():
    question = randint(0, 100)
    if question < 2:
        return question, 'no'
    var = 2
    square_root = question ** 0.5
    while var <= square_root:
        if question % var == 0:
            return question, 'no'
        var += 1
    return question, 'yes'


def show_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
