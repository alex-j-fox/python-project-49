import prompt


user_name = ''


def greet_user():
    global user_name
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def get_user_answer():
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def check_user_answer(user_answer, solution):
    if user_answer == str(solution):
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
              f"'{solution}'.")
        print(f'Let\'s try again, {user_name}!')
        return exit()


def show_congratulations():
    print(f'Congratulations, {user_name}!')


def run_game(game_module):
    greet_user()
    print(game_module.show_question())
    count = 0
    while count < 3:
        question, answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        check_user_answer(get_user_answer(), answer)
        count += 1
    else:
        show_congratulations()
