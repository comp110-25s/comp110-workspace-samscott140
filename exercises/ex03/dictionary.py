"""Dictionary Code"""

__author__: str = "730650345"


def invert(set1: dict[str, str]) -> dict[str, str]:
    invert_set: dict[str, str] = {}
    for key in set1:
        if set1[key] in invert_set:
            raise KeyError("Appears more than once in the dictionary")
        invert_set[set1[key]] = key
    return invert_set


def count(list_to_count: list[str]) -> dict[str, int]:
    dict1: dict[str, int] = {}
    i: int = 0
    while i < len(list_to_count):

        if list_to_count[i] in dict1:
            dict1[list_to_count[i]] += 1
        else:
            dict1[list_to_count[i]] = 1
        i += 1
    return dict1


def favorite_color(d: dict[str, str]) -> str:
    list1: list[str] = list()
    for key in d:
        list1.append(d[key])
    color_dict: dict[str, int] = count(list1)

    most_frequent_color: str = ""
    max_count: int = 0
    first_color = None
    for key in color_dict:
        if color_dict[key] > max_count:
            max_count = color_dict[key]
            most_frequent_color = key
            first_color = most_frequent_color
        elif color_dict[key] == max_count and first_color is None:
            most_frequent_color = key
    return most_frequent_color


def bin_len(lis: list[str]) -> dict[int, set[str]]:
    bin: dict[int, set[str]] = {}
    i: int = 0
    while i < len(lis):
        length: int = len(lis[i])
        if length in bin:
            bin[length].add(lis[i])
        else:
            bin[length] = {lis[i]}
        i += 1
    return bin
