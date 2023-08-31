from random import randint


def get_question_and_answer():
    question = randint(0, 100)
    if question < 2:
        answer = 'no'
    elif question == 2:
        answer = 'yes'
    else:
        var = 2
        square_root = question ** 0.5
        while var <= square_root:
            if question % var == 0:
                answer = 'no'
                break
            var += 1
        else:
            answer = 'yes'
    return question, answer


def show_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'

