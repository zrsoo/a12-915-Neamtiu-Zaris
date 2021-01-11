"""
13.) The sequence a1, ..., an of distinct integer numbers is given. Display all subsets with a mountain aspect.
A set has a mountain aspect if the elements increase up to a point and then they decrease. E.g. 10, 16, 27, 18, 14, 7.
"""


def max_number_index(list_numbers):
    """

    :param list_numbers:
    :return: The index of the greatest number in the list of numbers
    """
    maximum = 0
    maximum_index = None
    for nr in list_numbers:
        if nr > maximum:
            maximum = nr
            maximum_index = list_numbers.index(nr)

    return maximum_index


def sol(s, k):
    """
    Checks if the solution is a complete one
    :param s:
    :return: True if it is complete, false otherwise
    """

    # The solution is a complete one if it has at least 3 elements,
    # and the maximum number of the 3 is not on the first or last position.
    if k >= 2 and max_number_index(s[:k + 1]) != 0 and max_number_index(s[:k + 1]) != k:
        return True

    return False


def write(s, k):
    """
    Prints a solution
    :param s:
    :param k:
    :return:
    """
    print("A possible solution is: ", end="")
    print(s[:k + 1])


def ok(k, s):
    """
    Checks if the solution is correct up until the last inserted element.
    :param k:
    :param s:
    :return: True if it is correct, False otherwise
    """
    if k == 0:
        return True

    max_index = max_number_index(s)

    for index in range(k):
        if s[index] == s[k]:
            return False

    for index in range(max_index):
        if s[index] >= s[index + 1]:
            return False
    for index in range(max_index, k):
        if s[index] <= s[index + 1]:
            return False

    return True


def recursive_back(k, s, li_numbers):
    s = s[:k]
    for index in range(len(li_numbers)):
        s.insert(k, li_numbers[index])

        if ok(k, s) is True:
            if sol(s, k) is True:
                write(s, k)
            # else:
                # print(s)
            recursive_back(k + 1, s, li_numbers)
            s.pop()
        else:
            s.pop()


def next_element(li_numbers, index):
    if index + 1 < len(li_numbers):
        return li_numbers[index + 1], index + 1
    return None, None


def iterative_back(li_numbers):
    stack = [[]]
    while len(stack):
        index = 0
        element = li_numbers[index]
        result = stack.pop()
        result.append(element)

        while element is not None:
            result[-1] = element
            if ok(len(result) - 1, result):
                if sol(result, len(result) - 1):
                    write(result, len(result) - 1)
                    stack.append(result[:])
                else:
                    stack.append((result[:]))
            element, index = next_element(li_numbers, index)


if __name__ == "__main__":
    li_numbers = input("Numbers: ")

    # Converting each number to an integer
    # (they are being read as strings)
    li_numbers = li_numbers.split()
    li_numbers = [int(nr) for nr in li_numbers]

    s = []

    iterative_back(li_numbers)
