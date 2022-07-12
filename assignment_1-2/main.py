import math


def question_1_print():
    print("Question 1:")
    print(50 + 50)
    print(100 - 10)
    print()


def question_2_print() -> int:
    # print output for each value that are comma separated
    # print(30+*6), is an invalid syntax error
    print(6 ** 6)
    print(6 ** 6)
    print(6 + 6 + 6 + 6 + 6 + 6)
    print()


def question_3_print():
    print("Question 3:")
    print("Hello World")
    print("Hello World : 10")
    print()


def question_4(P, R, L) -> int:
    # input takes loan size: P, interest rate: R%, time to pay in months: L
    # Return M, number of monthly payments
    # used this equation:
    # https://www.calculatorsoup.com/calculators/financial/mortgage-calculator.php
    R = (R / 100) / 12  # monthly interest
    numerator = (P * R) * ((1 + R) ** L)
    denominator = (1 + R) ** L - 1
    return math.ceil(numerator / denominator)


def main():
    question_1_print()

    print("Question 2:")
    question_2_print()
    print()

    question_3_print()

    P = 800000
    R = 6
    L = 103
    print("Question 4:")
    print(question_4(P, R, L))


if __name__ == "__main__":
    main()
