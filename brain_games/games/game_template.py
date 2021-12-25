import prompt


def game_template(requirement,
                  random_expression_1,
                  random_expression_2,
                  random_expression_3,
                  correct_answer_1,
                  correct_answer_2,
                  correct_answer_3):

    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print('Hello, ' + name + '!\n' + requirement)

    print('Question: ' + str(random_expression_1))
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer_1:
        print('Correct!')
    else:
        return print("'" + user_answer + "' is wrong answer ;(. Correct answer was '" + str(correct_answer_1) + "'\nLet's try again, " + name + "!")

    print('Question: ' + str(random_expression_2))
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer_2:
        print('Correct!')
    else:
        return print("'" + user_answer + "' is wrong answer ;(. Correct answer was '" + str(correct_answer_2) + "'\nLet's try again, " + name + "!")

    print('Question: ' + str(random_expression_3))
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer_3:
        print('Correct!')
    else:
        return print("'" + user_answer + "' is wrong answer ;(. Correct answer was '" + str(correct_answer_3) + "'\nLet's try again, " + name + "!")

    return print('Congratulations, ' + name + '!')
