from random import randint, choice
from operator import add, sub, mul
from brain_games.games.game_template import game_template


def calc():
    requirement = 'What is the result of the expression?'
    operators = ["+", "-", "*"]
    operator1 = choice(operators)
    operator2 = choice(operators)
    operator3 = choice(operators)
    operand1_1 = randint(1, 100)
    operand1_2 = randint(1, 100)
    operand2_1 = randint(1, 100)
    operand2_2 = randint(1, 100)
    operand3_1 = randint(1, 100)
    operand3_2 = randint(1, 100)
    random_expression_1 = str(operand1_1) + ' ' + \
        operator1 + ' ' + str(operand1_2)
    random_expression_2 = str(operand2_1) + ' ' + \
        operator2 + ' ' + str(operand2_2)
    random_expression_3 = str(operand3_1) + ' ' + \
        operator3 + ' ' + str(operand3_2)

    if operator1 == "+":
        correct_answer_1 = str(add(operand1_1, operand1_2))
    elif operator1 == "-":
        correct_answer_1 = str(sub(operand1_1, operand1_2))
    else:
        correct_answer_1 = str(mul(operand1_1, operand1_2))

    if operator2 == "+":
        correct_answer_2 = str(add(operand2_1, operand2_2))
    elif operator2 == "-":
        correct_answer_2 = str(sub(operand2_1, operand2_2))
    else:
        correct_answer_2 = str(mul(operand2_1, operand2_2))

    if operator3 == "+":
        correct_answer_3 = str(add(operand3_1, operand3_2))
    elif operator3 == "-":
        correct_answer_3 = str(sub(operand3_1, operand3_2))
    else:
        correct_answer_3 = str(mul(operand3_1, operand3_2))

    game_template(requirement,
                  random_expression_1,
                  random_expression_2,
                  random_expression_3,
                  correct_answer_1,
                  correct_answer_2,
                  correct_answer_3)
