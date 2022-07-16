from report import Report


def main():
    path = "/home/wyatt/Projects/assignments/assignment_5"
    report = Report(path)
    report.load_filenames()
    # print("Report filenames:", report.get_filenames())
    report.load_sheets()


if __name__ == "__main__":
    main()
