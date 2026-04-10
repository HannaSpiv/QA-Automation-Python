def sum_ignore_non_numbers(items):
    sum_ignore = 0

    for item in items:
        if isinstance(item, (int, float)):
            sum_ignore += item

    return sum_ignore



def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False



def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)



def common_strings(list1, list2, ignore_case=True):
    result = []

    for i in list1:
        for j in list2:
            if ignore_case:
                if i.lower() == j.lower():
                    result.append(i.lower())
                    break
            else:
                if i == j:
                    result.append(i)
                    break

    unique_result = []
    for item in result:
        if item not in unique_result:
            unique_result.append(item)

    return unique_result