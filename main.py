def get_longest_subsequence_with_property(lst, list_property_predicate):
    result = []
    length = len(lst)
    width = 1
    while width <= length:
        for start in range(0, length - width + 1):
            sub_sequence = lst[start:start + width]
            if list_property_predicate(sub_sequence):
                result = sub_sequence
                break
        width += 1
    return result
    """
    Determines the longest sub-sequence with a given property for a list.
    :param lst: The input list of numbers.
    :param property_predicate: The list predicate representing the given property. Should be a function (list[]) -> bool type.
    :return: The longest sub-sequence with that property. If multiple longest sub-sequences with the same length exist only the first from left to right is returned.
    """


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False
    if number != 2 and is_even(number):
        return False
    for factor in range(3, number // 2 + 1, 2):
        if number % factor == 0:
            return False
    return True


def is_list_of_primes(lst):
    for el in lst:
        if not is_prime(el):
            return False
    return True


def get_longest_all_primes(lst):
    """
        Determines the longest sub-sequence of primes for 'lst' list.
        :param lst: The input list of numbers.
        :return: The longest sub-sequence of primes if exits, [] otherwise.
    """
    return get_longest_subsequence_with_property(lst, is_list_of_primes)


def test_get_longest_all_primes():
    assert get_longest_all_primes([2]) == [2]
    assert get_longest_all_primes([2, 3]) == [2, 3]
    assert get_longest_all_primes([1]) == []
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1, 6, 8]) == []
    assert get_longest_all_primes([2, 4, 6, 5, 7, 1, 6, 12]) == [5, 7]
    assert get_longest_all_primes([1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 19, 23, 17]) == [11, 13, 19, 23, 17]


def is_below_average(lst, average):
    el_sum = 0
    for el in lst:
        el_sum += el
    return float(el_sum / len(lst)) <= average


def get_longest_average_below(lst, average):
    return get_longest_subsequence_with_property(lst, (lambda l_lst: is_below_average(l_lst, average)))
    """
    Determines the longest sub-sequence of lst whose numbers have their average not above 'average'.
    :param lst: The input list of numbers. 
    :param average: The average threshold.
    :return: The longest sub-sequence with average not above 'average' threshold if exists, [] otherwise.
    """


def test_get_longest_average_below():
    assert get_longest_average_below([], 4.0) == []
    assert get_longest_average_below([4], 4.0) == [4]
    assert get_longest_average_below([3, 6], 4.0) == [3]
    assert get_longest_average_below([5], 4.0) == []
    assert get_longest_average_below([1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 19, 23, 17], 4.0) == [1, 2, 3, 5, 6, 7]
    assert get_longest_average_below([8, 9, 11, 1, 2, 3, 5, 6, 7, 13, 19, 23, 17], 4.0) == [1, 2, 3, 5, 6, 7]
    assert get_longest_average_below([8, 9, 11, 13, 19, 23, 17, 1, 2, 3, 5, 6, 7], 4.0) == [1, 2, 3, 5, 6, 7]
    assert get_longest_average_below([5, 6, 7, 8, 3, 12, 2, 3, 88], 4.0) == [2, 3]
    assert get_longest_average_below([1, 9, 2, 8, 3, 7, 4, 6, 5, 5], 5.0) == [1, 9, 2, 8, 3, 7, 4, 6, 5, 5]


def all_elements_divisible_with_factor(lst, k):
    for element in lst:
        if element % k != 0:
            return False
    return True


def test_all_elements_divisible_with_factor():
    assert all_elements_divisible_with_factor([2, 4, 6], 2) is True
    assert all_elements_divisible_with_factor([], 2) is True
    assert all_elements_divisible_with_factor([2, 4, 6], 3) is False


def get_longest_div_k(lst, factor):
    '''
    Finds the longest subsequence where all elements are divisible with factor 'factor'.
    :param lst: Input lst of integers.
    :param factor: The factor to test divisibility against.
    :return: The longest subsequence where all elements are divisible with factor 'factor' if exists, [] otherwise.
    '''
    return get_longest_subsequence_with_property(lst,
                                                 (lambda l_list: all_elements_divisible_with_factor(l_list, factor)))


def test_get_longest_div_k():
    assert get_longest_div_k([], 2) == []
    assert get_longest_div_k([2], 2) == [2]
    assert get_longest_div_k([2, 4, 6, 8, 12, 18], 2) == [2, 4, 6, 8, 12, 18]
    assert get_longest_div_k([2, 4, 6, 8, 12, 18], 3) == [12, 18]
    assert get_longest_div_k([2, 4, 6, 8, 12, 18], 4) == [8, 12]
    assert get_longest_div_k([2, 4, 6, 8, 12, 18], 5) == []


def test_all():
    test_all_elements_divisible_with_factor()
    test_get_longest_all_primes()
    test_get_longest_average_below()
    test_get_longest_div_k()


test_all()


def show_options():
    print('''
    1.Read input list elements.
    2.Find longest sub-sequence of primes.
    3.Find longest sub-sequence of elements with average below threshold(inclusive).
    4.Find longest sub-sequence of elements divisible with a given factor.
    5.Exit the interactive menu.
    ''')


def read_input_elements():
    elements = []
    no_elements = int(input('Number of elements='))
    for index in range(0, no_elements):
        el = int(input(f'el[{index + 1}]='))
        elements.append(el)
    return elements


def show_longest_of_primes(lst):
    print(f"Longest subsequence of primes is:{get_longest_all_primes(lst)}.")


def show_longest_below_average(lst):
    avg_threshold = float(input("Average threshold is:"))
    print(f"Longest subsequence of numbers below average {avg_threshold} "
          f"is:{get_longest_average_below(lst, avg_threshold)}.")


def show_longest_of_divisible_with_factor(lst):
    factor = int(input("Divisibility factor is:"))
    print(f"Longest subsequence of numbers divisible with factor {factor} is: {get_longest_div_k(lst, factor)}")


def interactive_menu():
    lst_data = []
    while True:
        show_options()
        option = input("Your option is:")
        if option == '1':
            lst_data = read_input_elements()[:]
        elif option == '2':
            show_longest_of_primes(lst_data)
        elif option == '3':
            show_longest_below_average(lst_data)
        elif option == "4":
            show_longest_of_divisible_with_factor(lst_data)
        elif option == "5":
            break
        else:
            print("Unknown option, try again.")
    print("Exiting the menu.")


interactive_menu()
