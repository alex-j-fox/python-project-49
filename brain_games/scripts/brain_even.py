#!/usr/bin/env python3
from random import randint

import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}! ')
    return name


def get_random_number():
    return randint(0, 1000)


def is_even_number(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = get_random_number()
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ').lower()
        if  answer == is_even_number(random_number):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even_number(random_number)}'.")
            break
        count += 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
