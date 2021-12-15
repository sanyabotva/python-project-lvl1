import prompt
from random import randint


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def even():
    counter = 0

    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print('Hello, ' + name + '!\nAnswer "yes" if the number is even, otherwise answer "no".')

    while counter <= 2:
        random_number = randint(1, 100)
        correct_answer = is_even(random_number)

        print('Question: ' + str(random_number))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            return print("'" + user_answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'\nLet's try again, " + name + "!")
    return print('Congratulations, ' + name + '!')
