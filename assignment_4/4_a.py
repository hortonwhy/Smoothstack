def q1_print():
    print("Question 1.")
    print("Hello World")
    print()


def q2_print(name):
    print("Question 2.")
    print("Hi my name is", name)
    print()


def q3(x, y, z):
    if z:
        return x
    return y


def q4(x, y):
    return x * y


def q5_is_even(n):
    if n % 2 == 0:
        return True
    return False


def q6(x, y):
    if x <= y:
        return False
    return True


def q7(*n):
    return sum(n)


def q8(*n):
    even_list = []
    for value in n:
        if value % 2 == 0:
            even_list.append(value)
    return even_list


def q10(x, y):
    if x % 2 != 0 or y % 2 != 0:
        return max(x, y)
    return min(x, y)


def q9(strng):
    new_string = ""
    for i in range(len(strng)):
        if i % 2 == 0:
            new_string += strng[i].upper()
        else:
            new_string += strng[i].lower()
    return new_string


def q11(strng1, strng2):
    if len(strng1) > 0 and len(strng2) > 0:
        if strng1[0].lower() == strng2[0].lower():
            return True
    return False


def q12(n):
    # This is a simplified approach that Miguel suggested
    # as I did not understand the question
    return 21 - 2 * n


def q13(strng):
    if len(strng) > 3:
        new_string = ""
        for i in range(len(strng)):
            if i == 0 or i == 3:
                new_string += strng[i].upper()
            else:
                new_string += strng[i]
        return new_string
    return


def main():
    q1_print()

    name = "Google"
    q2_print(name)

    x = "hello"
    y = "goodbye"
    z = True
    print("Question 3.")
    print(q3(x, y, z))
    z = False
    print(q3(x, y, z))
    print()

    x = 4
    y = 12
    print("Question 4.")
    print(q4(x, y))
    print()

    print("Question 5.")
    x = 4
    print(q5_is_even(x))
    x = 5
    print(q5_is_even(x))
    print()

    print("Question 6.")
    x = 6
    y = 5
    print(q6(x, y))
    x = 5
    print(q6(x, y))
    print()

    print("Question 7.")
    print(q7(3, 8, 12))
    print()

    print("Question 8.")
    print(q8(3, 8, 12))
    print()

    print("Question 9.")
    strng = "I HAVE not stripped punc[]#$tuation!"
    print(q9(strng))
    print()

    x = 11
    y = 20
    print("Question 10.")
    print(x, y, "as inputs:", q10(x, y))
    x = 12
    print(x, y, "as inputs:", q10(x, y))
    y = 19
    print(x, y, "as inputs:", q10(x, y))
    print()

    strng1 = "Hello"
    strng2 = "hallo"
    print("Question 11.")
    print(q11(strng1, strng2))
    print()

    print("Question 12.")
    print(q12(2))
    print()

    strng = "this is a going to capitalize"
    print("Question 13.")
    print(q13(strng))
    print()


if __name__ == "__main__":
    main()
