"""
DSC 20 Winter 2024 Homework 02
Name: Steven Ngo
PID: A18461865
Source: Assigned readings
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    Puts given and preferred names into a tuple and returns a list of
    those tuples, with 'NO NAME PROVIDED' as the first element if there is no 
    given name provided.
    --
    Parameters:
        given_names: list of given names as strings
        preferred_names: list of preferred names as strings
    --
    Returns:
        A list of tuples, pairing given and preferred names

    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff')]

    >>> given_names = ['']
    >>> preferred_names = ['Mandy', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('', 'Mandy'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = []
    >>> name_mapping(given_names, preferred_names)
    []

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = []
    >>> name_mapping(given_names, preferred_names)
    []
    """
    new_lst = []
    missing_num = 0
    given = given_names
    if len(given_names) < len(preferred_names):
        missing_num = len(preferred_names) - len(given_names)
        for i in range(missing_num):
            given.append('NO NAME PROVIDED')
    for i in range(len(preferred_names)):
        new_lst.append((given[i], preferred_names[i]))
    return new_lst


# Question 2
def valid_pairs(keys, values):
    """
    Takes two lists of keys and values and creates tuples containing
    corresponding elements from the lists in the same order, where keys 
    must be valid dictionary keys (immutable).
    --
    Parameters:
        keys: list of various data types
        values: list of various data types
    --
    Returns:
        A list of tuples pairing the keys and values, where the first element
        is a string 'not valid' if the key is an invalid dictionary key
    
    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    >>> keys = [{}, []]
    >>> values = [{}, []]
    >>> valid_pairs(keys, values)
    [('not valid',), ('not valid',)]

    >>> keys = [(), '']
    >>> values = [{}, True]
    >>> valid_pairs(keys, values)
    [((), {}), ('', True)]

    >>> keys = [True]
    >>> values = [False]
    >>> valid_pairs(keys, values)
    [(True, False)]
    """
    new_pairs = []
    for i in range(len(keys)):
        if (type(keys[i]) is list) or (type(keys[i]) is dict):
            new_pairs.append(('not valid', ))
        else:
            new_pairs.append((keys[i], values[i]))
    return new_pairs


# Question 3
def dict_of_names(name_tuples):
    """
    Converts a list of tuples containing paired given and preferred names
    into a dictionary with given names as keys and preferred as values
    in a list. If there are multiple given names, append the corresponding 
    preferred name to the associated values as a list.
    --
    Parameters:
        names_tuples: list of tuples containing names
    --
    Returns:
        A dictionary with key-value pairs from tuple elements based on rules
        above

    >>> dict_of_names([('Richard', 'Rick'), \
('Roxanne', 'Rose'), ('Roxanne', 'Ann'), \
('Richard', 'Ricky'), ('Roxanne', 'Roxie'), \
('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'), \
('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick')])
    {'NO NAME PROVIDED': ['Derrick']}

    >>> dict_of_names([('Steven', 'Vincent'), ('Steven', ''), \
('Robert', 'Paul')])
    {'Steven': ['Vincent', ''], 'Robert': ['Paul']}

    >>> dict_of_names([('', 'Derrick'), ('', 'Jacob')])
    {'': ['Derrick', 'Jacob']}

    >>> dict_of_names([])
    {}
    """
    dict_nicknames = {}
    for name in name_tuples:
        if name[0] not in dict_nicknames:
            dict_nicknames[name[0]] = [name[1]]
        else:
            dict_nicknames[name[0]].append(name[1])
    return dict_nicknames


# Question 4.1
def contractor_payment(suggestions):
    """
    Calculates the rounded average pay for each contractor and assigns it 
    to each contractor as a key-value pair in a dictionary.
    --
    Parameters:
        suggestions: list of lists, each inner list containing a pay 
        for the three contractors
    --
    Returns:
        A dictionary where the keys are contractor labels as strings, and 
        the values are the average payment for each contractor as a float
    
    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    >>> contractor_payment([[0, 0, 0], [1, 1, 1]])
    {'1': 0.5, '2': 0.5, '3': 0.5}

    >>> contractor_payment([[0, 0, 0], [1, 1, 1], [1, 1, 1]])
    {'1': 0.67, '2': 0.67, '3': 0.67}

    >>> contractor_payment([[0, 1, 2], [3, 2, 1], [0, 0, 0]])
    {'1': 1.0, '2': 1.0, '3': 1.0}
    """
    cont1, cont2, cont3 = 0, 0, 0
    averages_dct = {}
    decimal_places = 2
    third_cont_index = 2
    for inner in suggestions:
        cont1 += inner[0]
        cont2 += inner[1]
        cont3 += inner[third_cont_index]
    averages_dct['1'] = round(cont1/len(suggestions), decimal_places)
    averages_dct['2'] = round(cont2/len(suggestions), decimal_places)
    averages_dct['3'] = round(cont3/len(suggestions), decimal_places)
    return averages_dct

# Question 4.2
def new_pay(hours):
    """
    Calculates the pay for each contractor based on a formula and 
    updates the given dictionary with a new key-value pair representing
    either bonus, penalty, or no pay.
    --
    Parameters:
        hours: a dictionary of hours as values associated with 
        each contractor represented as strings as keys
    --
    Returns:
        An integer representing the bonus pay

    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    >>> case4 = {'1': 150, '2': 150, '3': 150}
    >>> round(new_pay(case4), 2)
    -0.25
    >>> case4
    {'1': 150, '2': 150, '3': 150, 'pay': 'Penalty'}

    >>> case5 = {'1': 0, '2': 0, '3': 0}
    >>> new_pay(case5)
    -5.0
    >>> case5
    {'1': 0, '2': 0, '3': 0, 'pay': 'Penalty'}

    >>> case6 = {'1': 100, '2': 100, '3': 100}
    >>> round(new_pay(case6), 2)
    -2.5
    >>> case6
    {'1': 100, '2': 100, '3': 100, 'pay': 'Penalty'}
    """
    penalty = -10
    bonus_pay = (
        0.01 * hours['1'] + 
        0.015 * hours['2'] + 
        min(0.02 * abs(100 - hours['3']), 0.025 * hours['3']) - 5
        )
    for i in hours.values():
        if i < 0:
            bonus_pay = penalty
            break
    if bonus_pay > 0:
        hours.update({'pay': 'Bonus'})
    elif bonus_pay == 0:
        hours.update({'pay': 'No'})
    else:
        hours.update({'pay': 'Penalty'})
    return bonus_pay

# Question 5
def potential_ideas_for_business(items):
    """
    Takes unique items from a dictionary and adds them to a new list 
    containing those items in alphabetical order.
    --
    Parameters:
        items: A dictionary in which the values are the supplier labels as
        strings and the keys are a list of items.
    --
    Returns:
        A list of unique items from the supplier lists
    
    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []
    >>> items = {'supplier 1': ['Bananas', 'Grapes'], \
'supplier 2': ['Oranges', 'Bananas'], 'supplier 3': ['Grapes', 'Apples']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Bananas', 'Grapes', 'Oranges']

    >>> items = {'supplier 1': ['Books', 'Magazines'], \
'supplier 2': ['Newspapers', 'Journals'], \
'supplier 3': ['Magazines', 'Journals']}
    >>> potential_ideas_for_business(items)
    ['Books', 'Journals', 'Magazines', 'Newspapers']

    >>> items = {'supplier 1': ['Pencils', 'Erasers'], \
'supplier 2': ['Markers', 'Notebooks'], \
'supplier 3': ['Erasers', 'Markers']}
    >>> potential_ideas_for_business(items)
    ['Erasers', 'Markers', 'Notebooks', 'Pencils']
    """
    unique = []
    for item_lst in items.values():
        for item in item_lst:
            if item not in unique:
                unique.append(item)
    unique.sort()
    return unique

# Question 6.1
def count_lines_1(filepath):
    """
    Uses the for keyword to count the number of lines in the given file.
    --
    Parameters:
        filepath: file path as a string to a non-empty file
    --
    Returns:
        Number of lines in the file as an integer
    
    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24
    >>> count_lines_1('files/test3.txt')
    15
    >>> count_lines_1('files/test4.txt')
    7
    >>> count_lines_1('files/test5.txt')
    19
    """
    count = 0
    with open(filepath, 'r') as f:
        for line in f:
            count += 1
    return count


# Question 6.2
def count_lines_2(filepath):
    """
    Uses the read() function to count the number of lines in the given file.
    --
    Parameters:
        filepath: file path as a string to a non-empty file
    --
    Returns:
        Number of lines in the file as an integer

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24
    >>> count_lines_2('files/test3.txt')
    15
    >>> count_lines_2('files/test4.txt')
    7
    >>> count_lines_2('files/test5.txt')
    19
    """
    with open(filepath, 'r') as f:
        return len(f.read().split('\n'))


# Question 6.3
def count_lines_3(filepath):
    """
    Uses the readlines() functionto count the number of lines in the given 
    file.
    --
    Parameters:
        filepath: file path as a string to a non-empty file
    --
    Returns:
        Number of lines in the file as an integer

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24
    >>> count_lines_3('files/test3.txt')
    15
    >>> count_lines_3('files/test4.txt')
    7
    >>> count_lines_3('files/test5.txt')
    19
    """
    with open(filepath, 'r') as f:
        return len(f.readlines())


# Question 7
def collected_items(filepath):
    """
    Puts the item from each line in the given file into a list.
    --
    Parameters:
        filepath: file path as a string
    --
    Returns:
        A list of items as strings in the same order as in the input file

    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []
    >>> collected_items('files/ings3.txt')
    ['chips', 'jeans', 'jeans']
    >>> collected_items('files/ings4.txt')
    ['keychain', 'figure', 'hoodie']
    >>> collected_items('files/ings5.txt')
    ['charger', 'combo1']
    """
    items = []
    item_index = 2
    with open(filepath, 'r') as f:
        for line in f.readlines():
            items.append(line.split(',')[item_index])
    return items


# Question 8
def case_letters(filepath):
    """
    Writes the number of uppercase and lowercase letters in the given file 
    path string into the file itself.
    --
    Parameters:
        filepath: file path as a string
    --
    Returns:
        None

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19
    >>> case_letters('files/HelloWorld.txt')
    >>> with open('files/HelloWorld.txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    2
    16
    >>> case_letters('files/HowAreYouDoing.txt')
    >>> with open('files/HowAreYouDoing.txt', 'r') as outfile4:
    ...    print(outfile4.read().strip())
    4
    18
    >>> case_letters('files/IMGREAT.txt')
    >>> with open('files/IMGREAT.txt', 'r') as outfile5:
    ...    print(outfile5.read().strip())
    7
    8
    """
    upper = 0
    lower = 0
    for letter in filepath:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    with open(filepath, 'w') as f:
        f.write(f"{upper}\n{lower}")
    return


# Question 9
def map_office(filepath):
    """
    Maps each office number from n>0 lines from a given file onto a new 
    file as strings, based on the office number, returning a sum of valid
    office numbers.
    --
    Parameters:
        filepath: file path as a string
    --
    Returns:
        The sum of all valid office numbers, ignoring the negative ones

    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor

    >>> map_office('files/offices3.txt')
    798
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    second floor
    third floor and above
    not a valid office number

    >>> map_office('files/offices4.txt')
    400
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    second floor
    ground floor

    >>> map_office('files/offices5.txt')
    301
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    not a valid office number
    not a valid office number
    third floor and above
    """
    valid_sum = 0
    last_floor_1 = 199
    first_floor_2 = 200
    last_floor_2 = 299
    third_floor_and_up = 300
    with open(filepath, 'r') as f:
        ints_as_lst = f.read().split('\n')
        with open('files/floors.txt', 'w') as floors:
            for num in ints_as_lst:
                if int(num) < 1:
                    floors.write('not a valid office number\n')
                else:
                    valid_sum += int(num)
                    if int(num) >= 1 and int(num) <= last_floor_1:
                        floors.write('ground floor\n')
                    elif int(num) >= first_floor_2 \
                        and int(num) <= last_floor_2:
                        floors.write('second floor\n')
                    elif int(num) >= third_floor_and_up:
                        floors.write('third floor and above\n')
    return valid_sum
