from random import randint
from brain_games.games.game_template import game_template


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def even():
    requirement = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_expression_1 = randint(1, 100)
    random_expression_2 = randint(1, 100)
    random_expression_3 = randint(1, 100)
    correct_answer_1 = is_even(random_expression_1)
    correct_answer_2 = is_even(random_expression_2)
    correct_answer_3 = is_even(random_expression_3)

    game_template(requirement,
                  random_expression_1,
                  random_expression_2,
                  random_expression_3,
                  correct_answer_1,
                  correct_answer_2,
                  correct_answer_3)
