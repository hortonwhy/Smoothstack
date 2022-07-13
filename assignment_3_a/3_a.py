import math


def question_1(n) -> bool:
    return n % 7 == 0 and n % 5 == 0


def question_2(temp, convert_to):
    if convert_to == "Farenheit":
        return int((temp / 5) * 9 + 32)
    elif convert_to == "Celsius":
        return int((temp - 32) / 9 * 5)
    else:
        return "Please enter a valid number and measure: Celsius or Farenheit"


def question_3():
    answer = "2"
    guess = input("Guess a random number between 1 and 9: ")

    while guess != answer:
        guess = input("Try again!: ")
    print("well guessed!")
    return


def question_4_print(length):
    peak = math.ceil(length / 2)
    symbol = "*"
    for i in range(length + 1):
        if i < peak:
            for j in range(i):
                print(symbol, end="")
        else:
            for j in range(peak, i % peak, -1):
                print(symbol, end="")

        print()


def question_5():
    # reverse a string
    strng = input("enter a string to be reversed: ")
    return strng[::-1]


def question_6_print(nums):
    # count even and odds from nums list
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)


def question_7_print(data_list):
    print(data_list)
    for elem in data_list:
        print(type(elem))


def question_8_print():
    for i in range(6 + 1):
        if i == 3 or i == 6:
            continue
        print(i, end=" ")
    print()


def main():
    print("Question 1.")
    for i in range(1500, 2700 + 1):
        if question_1(i):
            print(i)
    print()

    print("Question 2.")
    print(question_2(60, "Farenheit"))
    print(question_2(45, "Celsius"))
    print()

    print("Question 3.")
    question_3()
    print()

    print("Question 4.")
    length = 9
    question_4_print(length)
    print()

    print("Question 5.")
    print(question_5())
    print()

    print("Question 6.")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    question_6_print(nums)
    print()

    print("Question 7.")
    data_list = [
        1452,
        11.23,
        1 + 2j,
        True,
        "w3resource",
        (0, -1),
        [5, 12],
        {"class": "V", "section": "A"},
    ]
    question_7_print(data_list)
    print()

    print("Question 8.")
    question_8_print()


if __name__ == "__main__":
    main()
