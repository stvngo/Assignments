"""
DSC 20 Winter 2025 Homework 06
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

#Question 1
def randomize(*args):
    """ 
    Takes a series of arguments and returns a dictionary where the keys are
    the data types and the values are lists of items, organized according to
    some rules.

    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> randomize(0, 3.1415, 'Hello', [], {}, True, -7)
    {'int': [True, False], 'float': [3], 'str': ['Hlo'], 'list': [0], \
'garbage': [{}, True]}
    >>> randomize(0, -100, 'HELLO', [5, 6], None, 3.14)
    {'int': [True, True], 'str': ['HLO'], 'list': [2], 'garbage': [None], \
'float': [3]}
    >>> randomize(-1, -2, -3, -4, -5, -6, -7, -8)
    {'int': [False, True, False, True, False, True, False, True]}
    """
    new_dct = {}
    step = 2
    for arg in args:
        if isinstance(arg, str):
            if "str" not in new_dct:
                new_dct["str"] = []
            new_dct["str"].append("".join([arg[i] \
                for i in range(0, len(arg), step)]))
        elif type(arg) == int:
            if "int" not in new_dct:
                new_dct["int"] = []
            if arg % step == 0:
                new_dct["int"].append(True)
            else:
                new_dct["int"].append(False)
        elif isinstance(arg, float):
            if "float" not in new_dct:
                new_dct["float"] = []
            if arg < 0:
                new_dct["float"].append(-1 * arg)
            else:
                new_dct["float"].append(int(arg))
        elif isinstance(arg, list):
            if "list" not in new_dct:
                new_dct["list"] = []
            new_dct["list"].append(len(arg))
        else:
            if "garbage" not in new_dct:
                new_dct["garbage"] = []
            new_dct["garbage"].append(arg)
    return new_dct


#Question 2
def rearrange_args(*args, **kwargs):
    """
    Rearranges positional and keyword arguments into a list of tuples.
    Positional arguments are labeled as "positional_<index>",
    and keyword arguments are labeled as "keyword_<index>_<key>".

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> rearrange_args(42, 'Hello', 3.14, test='Python', count=5)
    [('positional_0', 42), ('positional_1', 'Hello'), ('positional_2', 3.14), \
('keyword_0_test', 'Python'), ('keyword_1_count', 5)]
    >>> rearrange_args()
    []
    >>> rearrange_args(True, None, [], a=1, b=2, c=3)
    [('positional_0', True), ('positional_1', None), ('positional_2', []), \
('keyword_0_a', 1), ('keyword_1_b', 2), ('keyword_2_c', 3)]
    """
    new_lst = []
    for index, item in enumerate(args):
        new_lst.append((f"positional_{index}", item))
    for index, items in enumerate(kwargs.items()):
        new_lst.append((f"keyword_{index}_{items[0]}", items[1]))
    return new_lst

#Question 3.1
def count_the_password(lst, password):
    """
    Counts the number of times the given password appears in the list.

    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> count_the_password(["dragon", "dragon", "dragon", ""], "dragon")
    3
    >>> count_the_password(["Dragon"], "drago")
    0
    >>> count_the_password([" "], " ")
    1
    """
    if len(lst) == 0:
        return 0
    else:
        if lst[0] == password:
            return 1 + count_the_password(lst[1:], password)
        else:
            return 0 + count_the_password(lst[1:], password)

#Question 3.2  
def corrupt_password(input, to_insert):
    """
    Corrupts the given string by inserting the new string after each character
    of the given string.

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_password('password', '*')
    'p*a*s*s*w*o*r*d*'
    >>> corrupt_password('1234', '+')
    '1+2+3+4+'
    >>> corrupt_password('A', '!')
    'A!'
    """
    if len(input) == 0:
        return ""
    else:
        return input[0] + to_insert + corrupt_password(input[1:], to_insert)

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    Takes a list of strings, a password as a string, and a character, 
    corrupting all strings (the same way as in the previous problem)
    in the list except those that match the password exactly. 

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> outsmart_dragon(['dragon', 'dragons', 'DRAGON'], 'dragon', '*')
    ['dragon', 'd*r*a*g*o*n*s*', 'D*R*A*G*O*N*']
    >>> outsmart_dragon(['drag'], 'dragon','@')
    ['d@r@a@g@']
    >>> outsmart_dragon(['secret', 'password'], 'password', '?')
    ['s?e?c?r?e?t?', 'password']
    """
    if len(lst) == 0:
        return []
    if lst[0] == password:
        return [lst[0]] + outsmart_dragon(lst[1:], password, to_insert)
    else:
        return [corrupt_password(lst[0], to_insert)] + \
            outsmart_dragon(lst[1:], password, to_insert)

# Question 4
def corrupt_with_vowels(input):
    """
    Removes all vowels ('a', 'e', 'i', 'o', 'u', both uppercase and lowercase)
    from the given input string and returns the modified string without them.

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels('Python Programming')
    'Pythn Prgrmmng'
    >>> corrupt_with_vowels('HELLO WORLD')
    'HLL WRLD'
    >>> corrupt_with_vowels('AEIOUaeiou')
    ''
    """
    if len(input) == 0:
        return ""
    else:
        if input[0].lower() in "aeiou":
            return corrupt_with_vowels(input[1:])
        else:
            return input[0] + corrupt_with_vowels(input[1:])

# Question 5
def where_to_go(point1, point2, separator):
    """
    Generates a sequence of numbers from point1 to point2, separated by 
    separator string. If the points are the same, it returns
    one of the points as a string.

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(3, 5, ':')
    '3:4:5'
    >>> where_to_go(10, 7, '|')
    '10|9|8|7'
    >>> where_to_go(4, 4, '-')
    '4'
    """
    if point1 == point2:
        return str(point1)
    elif point1 < point2:
        return str(point1) + separator + \
            where_to_go(point1 + 1, point2, separator)
    else:
        return str(point1) + separator + \
            where_to_go(point1 - 1, point2, separator)
