from random import randint

GAME_TASK = 'What number is missing in the progression?'


def get_random_sequence():
    first_number = randint(0, 50)
    range_step = randint(1, 10)
    sequence_length = randint(5, 10)
    sequence = []
    for i in range(first_number, 150, range_step):
        sequence.append(str(i))
    return sequence[:sequence_length]


def get_question_and_answer():
    sequence = get_random_sequence()
    random_index = randint(0, len(sequence) - 1)
    answer = sequence[random_index]
    sequence[random_index] = '..'
    question = ' '.join(sequence)
    return question, answer
