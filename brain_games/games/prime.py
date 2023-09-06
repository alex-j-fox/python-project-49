from random import randint

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number < 2:
        return False
    var = 2
    square_root = number ** 0.5
    while var <= square_root:
        if number % var == 0:
            return False
        var += 1
    return True


def get_question_and_answer():
    question = randint(0, 100)
    answer = 'yes' if is_prime_number(question) else 'no'
    return question, answer
