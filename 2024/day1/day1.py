def get_example_lists() -> list:
    '''returns smaller lists to test functions with before using text file'''
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    return list1, list2


def read_input(filename: str) -> list[str]:
    '''returned a list of strings'''
    with open(filename, "r") as f:
        return f.readlines()


def clean_output(f: list[str]) -> list:
    '''turns list of strings into two separate lists'''
    list1 = []
    list2 = []
    for line in f:
        strip_line = line.strip()
        split_line = strip_line.split()
        a, b = map(int, split_line)
        list1.append(a)
        list2.append(b)
    return list1, list2


def reorder_list(location_id_list: list) -> list:
    '''reorders the list in ascending order'''
    sorted_list = sorted(location_id_list)
    return sorted_list


def combine_lists(list1, list2: list) -> list[tuple]:
    '''combines two reordered lists'''
    combined = list(zip(list1, list2))
    return combined


def find_bigger_number(location_id1, location_id2: int) -> int:
    '''finds the larger of two numbers'''
    if location_id1 > location_id2:
        biggest = location_id1
        smallest = location_id2
    else:
        biggest = location_id2
        smallest = location_id1
    return biggest, smallest


def difference_between_ids(location_id1, location_id2: int) -> int:
    '''finds the difference between corresponding ids'''
    biggest, smallest = find_bigger_number(location_id1, location_id2)
    difference = biggest - smallest
    return difference


def get_num_count(num: int, list2: list) -> int:
    '''checks how many times a number from list1 occurs in list 2'''
    num_count = list2.count(num)
    return num_count


def get_similarity_score(num, num_count: int) -> int:
    '''calculates similarity score'''
    return num * num_count


def star_one():
    f = read_input('day1.txt')
    list1, list2 = clean_output(f)
    list1_reordered = reorder_list(list1)
    list2_reordered = reorder_list(list2)
    combined_list = (combine_lists(list1_reordered, list2_reordered))
    sum = 0
    for combination in combined_list:
        difference = difference_between_ids(combination[0], combination[1])
        sum += difference
    return sum


def star_two():
    f = read_input('day1.txt')
    list1, list2 = clean_output(f)
    similarity_score = 0
    for num in list1:
        num_count = get_num_count(num, list2)
        similarity_score += get_similarity_score(num, num_count)
    return similarity_score


if __name__ == "__main__":
    print(star_one())
    print(star_two())
