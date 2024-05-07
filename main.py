def add_lists(list1, list2):
    if len(list1) == len(list2):
        return [list1[i] + list2[i] for i in range(len(list1))]


def sub_lists(list1, list2):
    if len(list1) == len(list2):
        return [list1[i] - list2[i] for i in range(len(list1))]
