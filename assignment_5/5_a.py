def bmi_calculate(stats):
    weight = stats[0]
    height = stats[1]
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "under"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "over"
    elif bmi > 30:
        return "obese"


def main():
    data = [(80, 1.73), (55, 1.58), (49, 1.91), (100, 1.73)]
    result = map(bmi_calculate, data)
    print("answer:")
    for value in result:
        print(value, end=" ")


if __name__ == "__main__":
    main()
