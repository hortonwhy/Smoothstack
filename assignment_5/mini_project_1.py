from report import Report


def main():
    report = Report() # no path given, uses cwd
    report.query_path()
    report.load_filenames()
    # print("Report filenames:", report.get_filenames())
    report.load_sheets()


if __name__ == "__main__":
    main()
