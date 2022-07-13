def crowd_test_part_3(people):
    if len(people) > 5:
        print("There is a mob")
    elif len(people) >= 3 and len(people) <= 5:
        print("the room is crowded")
    elif len(people) >= 1 and len(people) <= 2:
        print("the room is not crowded")
    else:
        print("the room is empty")


def crowd_test_part_2(people):
    if len(people) > 3:
        print("the room is crowded")
    else:
        print("the room is not crowded")


def crowd_test(people):
    if len(people) > 3:
        print("the room is crowded")


def main():
    people = ["Jim", "Jeff", "John", "Jerry"]
    crowd_test(people)
    people.pop()
    people.pop()
    crowd_test(people)

    print()
    crowd_test_part_2(people)

    print()
    people.append("Jerry")
    people.append("John")
    people.append("Jones")
    people.append("Jimmy")

    crowd_test_part_3(people)
    people.pop()
    crowd_test_part_3(people)
    people.pop()
    people.pop()
    people.pop()
    crowd_test_part_3(people)
    people.pop()
    people.pop()
    crowd_test_part_3(people)


if __name__ == "__main__":
    main()
