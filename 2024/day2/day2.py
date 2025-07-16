def get_sample_data():
    '''returns sample data to test functions with before using text file'''
    return ['7 6 4 2 1\n',
            '1 2 7 8 9\n',
            '9 7 6 2 1\n',
            '1 3 2 4 5\n',
            '8 6 4 4 1\n',
            '1 3 6 7 9\n']


def read_input(filename: str) -> list[str]:
    '''returns a list of strings'''
    with open(filename, "r") as f:
        return f.readlines()


def get_clean_data(f: list[str]) -> list[list[int]]:
    '''turns each string into a list of ints'''
    clean_data = []
    for report_string in f:
        report_str_list = report_string.strip().split()
        report_int_list = [int(num) for num in report_str_list]
        clean_data.append(report_int_list)
    return clean_data


def is_all_increasing(report: list[int]) -> bool:
    '''checks numbers in a report are all increasing'''
    for i in range(1, len(report)):
        if report[i] <= report[i-1]:
            return False
    return True


def is_all_decreasing(report: list[int]) -> bool:
    '''checks numbers in a report are all decreasing'''
    for i in range(1, len(report)):
        if report[i] >= report[i-1]:
            return False
    return True


def correct_level_difference(report: list[int]) -> bool:
    '''checks if safe difference between levels'''
    safe_difference = [1, 2, 3, -1, -2, -3]
    for i in range(1, len(report)):
        if (report[i] - report[i-1]) not in safe_difference:
            return False
    return True


def is_safe(report: list[int]) -> bool:
    '''checks that report meets all conditions to be considered safe'''
    if (is_all_decreasing(report) or is_all_increasing(report)) and correct_level_difference(report):
        return True
    return False


def star_one():
    # data = get_sample_data()
    data = read_input('day2.txt')
    clean_data = get_clean_data(data)
    safe_report_count = 0
    for report in clean_data:
        if is_safe(report):
            safe_report_count += 1
    return safe_report_count


def create_report_iteration(report: list[int]) -> list[list[int]]:
    '''creates a several iterations of each report where a different level is removed'''
    iterations = []
    for i in range(len(report)):
        new_ver = report[:i] + report[i+1:]
        iterations.append(new_ver)
    return iterations


def one_ver_safe(iterations: list[list[int]]) -> int:
    '''checks that there is at least one safe iteration'''
    for iteration in iterations:
        if is_safe(iteration):
            return True
    return False


def star_two():
    # data = get_sample_data()
    data = read_input('day2.txt')
    clean_data = get_clean_data(data)
    safe_report_count = 0
    for report in clean_data:
        if is_safe(report):
            safe_report_count += 1
        else:
            iterations = create_report_iteration(report)
            if one_ver_safe(iterations):
                safe_report_count += 1
    return safe_report_count


if __name__ == "__main__":
    print(star_one())
    print(star_two())
