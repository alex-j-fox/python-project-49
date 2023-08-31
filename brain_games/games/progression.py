from random import randint


def get_random_sequence():
    first_number = randint(0, 50)
    range_step = randint(1, 10)
    sequence_length = randint(5, 9)
    sequence = [first_number]
    for i in range(sequence_length):
        expression = first_number + range_step
        first_number = expression
        sequence.append(expression)
    random_index = randint(0, sequence_length)
    return sequence, random_index


def get_question_and_answer():
    sequence, random_index = get_random_sequence()
    answer = sequence[random_index]
    sequence[random_index] = '..'
    question = ''
    for i in sequence:
        question += f'{i} '
    return question, answer


def show_question():
    return 'What number is missing in the progression?'
