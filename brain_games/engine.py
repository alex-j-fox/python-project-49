import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def check_user_answer(user_answer, solution, user_name):
    if user_answer == str(solution):
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
              f"'{solution}'.")
        print(f'Let\'s try again, {user_name}!')
        return True


def run_game(game_module):
    name = greet_user()
    print(game_module.GAME_TASK)
    count = 0
    while count < 3:
        question, answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        if check_user_answer(get_user_answer(), answer, name):
            break
        count += 1
    else:
        print(f'Congratulations, {name}!')
