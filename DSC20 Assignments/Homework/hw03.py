"""
DSC 20 Winter 2024 Homework 03
Name: Steven Ngo
PID: A18461865
Source: Stack Overflow, W3Schools
"""
# Question 1.1
def operate_nums(lst):
    """
    Takes a list of integers and returns a new list with doubled odd
    integers and tripled even integers.

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]
    >>> operate_nums([1, 2, 3, 4, 5])
    [2, 6, 6, 12, 10]
    >>> operate_nums([2, [1], -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 0, -5])
    [6, 0, -10]
    """
    times_three = 3
    times_two = 2
    assert isinstance(lst, list)
    assert all([isinstance(i, int) for i in lst])
    return [i*times_three if i % 2 == 0 else i*times_two for i in lst]

# Question 1.2
def string_lengths(text, nums):
    """
    Returns a list of booleans where True indicates that the length of 
    the string is greater than the corresponding integer in the second list,
    and false otherwise.

    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]
    >>> string_lengths(['', ''], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(1.0, [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['i', 'we', 'love'], [2, 3, 4])
    [False, False, False]
    >>> string_lengths(['i', 1, 'love'], [2, 3, 4])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(text, list)
    assert isinstance(nums, list)
    assert len(text) == len(nums)
    assert all([isinstance(i, int) for i in nums])
    assert all([isinstance(s, str) for s in text])
    assert all(text)
    assert all([True if i > 0 else False for i in nums])
    return [True if len(text[i]) > nums[i] else False \
            for i in range(len(nums))]


# Question 1.3
def process_dict(input_dict):
    """
    Returns a list of integers, each representing the sum of the length of the
    key (tuple) and the total length of the strings in the value (list of 
    strings) of an input dictionary.
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
['b']})
    [15, 2]
    >>> process_dict({(1, 2): ['hello', 'nice', 'to', 'meet', 'you'], \
(2, 3, 'wow'): ['welcome', 'home']})
    [20, 14]
    >>> process_dict(['welcome home'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1,): ['a', 'b', 'c'], (1, 2): 'a'})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(input_dict, dict)
    assert all([isinstance(key, tuple) for key in input_dict.keys()])
    assert all([isinstance(value, list) \
                for value in input_dict.values()])
    assert all([isinstance(item, str) for value in input_dict.values() \
                for item in value]) 
    return [len(key) + sum(len(string) for string in value) \
            for key, value in input_dict.items()]


# Question 2
def unusual_sort(indices, items):
    """
    Sorts a list of items such that the i-th element of the new list is
    the indices's i-th element in items, where both the indices and items
    are the same size.

    >>> unusual_sort([0, 4, 2, 3, 1], \
["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 1, 2, 3, 6], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
("zero", "four", "two", "three", "one"))
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> unusual_sort([0, 1, 2, 3, 4], \
["zero", "one", "two", "three", "four"])
    [('zero', 0, 0), ('one', 1, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 4, 4)]

    >>> unusual_sort([0, 4, 2, 3, 1], \
["zero", "four", "two", "three", True])
    [('zero', 0, 0), (True, 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]
    """
    assert isinstance(indices, list)
    assert isinstance(items, list)
    assert len(indices) == len(items)
    assert all([isinstance(i, int) for i in indices])
    assert all([i in indices for i in range(len(indices))])
    return [(items[indices[i]], indices[i], i) \
            for i in range(len(indices)) if len(indices) > 0]


# Question 3
def change_input(strange_list):
    """
    Takes a list of strings and decodes each string by multiplying
    each digit by two, converting lowercase vowels to uppercase,
    while keeping everything else the same.

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
"5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> change_input(["11My aGe iS"])
    ['22My AGE IS']
    >>> change_input([23.0])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> change_input(["1-need-help"])
    ['2-nEEd-hElp']
    """
    times_two = 2
    new_string = ''
    assert isinstance(strange_list, list)
    assert all([isinstance(item, str) for item in strange_list])
    return [new_string.join(str(int(char)*times_two) if char.isdigit() \
        else char.upper() if char in 'aeiou' \
        else char for char in s) for s in strange_list]

# Question 4
def change_input_even_more(strange_list):
    """
    Takes a list of strings and decodes each string by multiplying
    each digit by two and moving them to the end of the string, converting
    lowercase vowels to uppercase, and keeping everything else the same.

    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> change_input_even_more(["11My aGe iS"])
    ['My AGE IS22']
    >>> change_input_even_more([23.0])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> change_input_even_more(["1-need-help"])
    ['-nEEd-hElp2']
    """
    times_two = 2
    assert isinstance(strange_list, list)
    assert all(isinstance(item, str) for item in strange_list)
    return ["".join(char.upper() if char in "aeiou" else char \
            for char in s if not char.isdigit()) \
            + "".join(str(int(char)*times_two) \
            for char in s if char.isdigit()) for s in strange_list]

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    Finds the brand name with the lowest price among reachable gas stations
    if the distance is less than the given mileage.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'
    >>> cheapest_gas(gas_stations, 30)
    'Shell'
    >>> cheapest_gas(gas_stations, 50)
    'Shell'
    >>> cheapest_gas(gas_stations, 80)
    'Shell'
    """

    lowest_price = min([pair[1] for key in gas_stations \
        for pair in gas_stations[key] if pair[0] <= mileage])
    cheapest_station = [key for key in gas_stations \
        for pair in gas_stations[key] if pair[1] == lowest_price]
    return cheapest_station[0]

# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    Finds the brand name with the lowest average price among reachable gas
    stations if the distance is less than the given mileage.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'
    >>> cheapest_average_gas(gas_stations, 30)
    'Shell'
    >>> cheapest_average_gas(gas_stations, 50)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 60)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 80)
    'Arco'
    """
    lowest_prices = [[(pair[1], key) for pair in gas_stations[key] \
                     if pair[0] <= mileage] for key in gas_stations]
    lowest_avg_price = [sum([tup[0] for tup in brand])/len(brand) \
                        if len(brand) > 0 else float('inf') \
                        for brand in lowest_prices ]
    cheapest_brand = list(gas_stations.keys()) \
        [lowest_avg_price.index(min(lowest_avg_price))]
    return cheapest_brand

# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    Adds or subtracts a given amount of food from a specific dish in 
    a dictionary of orders where keys are strings and values are positive
    integers.

    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> new_orders(orders, 'remove', 'burger', 6)
    {'pizza': 10, 'burger': 0}

    >>> new_orders(orders, 'remove', 'pizza', 11)
    {'pizza': 0, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 1.0)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(orders, dict)
    assert all([isinstance(key, str) for key in orders.keys()])
    assert all([isinstance(value, int) for value in orders.values()])
    assert isinstance(action, str)
    assert isinstance(dish_name, str)
    assert isinstance(amount, int)
    assert amount >= 0 
    updated_orders = {
        key: (value + amount if action == 'add' and key == dish_name else \
              max(value - amount, 0) if action == 'remove' and key == \
                dish_name else value) for key, value in orders.items()
                    }
    return updated_orders