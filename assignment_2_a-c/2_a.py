import re


def question_1_print():
    s = "Hello World"
    print("Question 1")
    print(s[-3])
    print()


def question_2_print():
    s = "thinker"
    print("Question 2")
    print(s[2:5])
    print("output of s='hello'[1] is 'e'")
    s = "hello"
    print(s[1])
    print()


def question_3_print():
    s = "Sammy"
    print("Question 3")
    print(s[2:])
    print()


def question_4_print():
    s = "Mississippi"
    s = set(s)
    print("Question 4")
    print(s)
    print()


def question_5(s) -> str:
    new_s = re.sub(r"[^\w]", "", s)  # replace anything not a word with ""
    new_s = new_s.lower()
    if new_s[::-1] == new_s:
        print("Y")
        return
    print("N")


def main():
    question_1_print()
    question_2_print()
    question_3_print()
    question_4_print()

    string_list = [
        "Stars",
        "O, a kak Uwakov lil vo kawu kakao!",
        "Some men interpret nine memos",
    ]

    print("Question 5")
    for element in string_list:
        question_5(element)

    print()


if __name__ == "__main__":
    main()
