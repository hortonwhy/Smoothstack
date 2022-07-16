def main():
    bookshop_data = [
        [34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3, 32.95],
        [88112, "Einführung in Python3, Bernd Klein", 3, 24.99],
    ]

    return_tuple = (
        lambda data: (data[0], data[2] * data[3] + 10)
        if data[2] * data[3] < 100
        else (data[0], data[2] * data[3])
    )
    result = map(return_tuple, bookshop_data)
    print("Question 1.")
    print(list(result))
    print()

    bookshop_data = [
        [34587, ("Learning Python, Mark Lutz", 4, 40.95)],
        [98762, ("Programming Python, Mark Lutz", 5, 56.80)],
        [77226, ("Head First Python, Paul Barry", 3, 32.95)],
        [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)],
    ]
    return_tuple = (
        lambda data: (data[0], data[1][1] * data[1][2] + 10)
        if data[1][1] * data[1][2] < 100
        else (data[0], data[1][1] * data[1][2])
    )
    result = map(return_tuple, bookshop_data)
    print("Question 2.")
    print(list(result))
    print()


if __name__ == "__main__":
    main()
