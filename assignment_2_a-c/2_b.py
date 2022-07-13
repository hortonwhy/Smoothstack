def question_1_print():
    my_list = [8, "a word", 1.4]
    print("1.", my_list)

    n_list = [1, 1, [1, 2]]
    print("2.", n_list[2][1])

    lst = ["a", "b", "c"]
    print("3.", lst[1:])

    d = dict()
    d["Monday"] = 0
    d["Tuesday"] = 0
    d["Wednesday"] = 0
    d["Thursday"] = 0
    d["Friday"] = 0
    d["Saturday"] = 0
    d["Sunday"] = 0
    print("4.", d)

    d = {"k1": [1, 2, 3]}
    print("5.", d["k1"][1])

    tup = tuple([1, [2, 3]])
    print("6.", tup)

    s = "Mississippi"
    s_set = set(s.lower())
    print("7.", s_set)

    s_set.update("x")
    print("8.", s_set)

    print("9.", set([1, 1, 2, 3]))


def question_2(n) -> int:
    # non-recursive approach
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total


def question_3(n) -> dict:
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i

    return d


def question_4_print():
    n = input()
    n = n.split(",")
    tup = tuple(n)
    print(n)
    print(tup)


class Question_5:
    def __init__(self):
        self.value = None

    def getString(self):
        self.value = input()

    def printString(self):
        print(self.value.upper())


def main():
    question_1_print()

    print()
    print(question_2(8))

    print()
    print(question_3(8))

    question_4_print()

    s = Question_5()
    s.getString()
    s.printString()


if __name__ == "__main__":
    main()
