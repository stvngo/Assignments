"""
DSC 20 Winter 2025 Lab 06
Name: Steven Ngo
PID: A18461865
"""

# Question 1
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. You don't need to add new doctests for this function.
    
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 10 for ans in answers])
    True
    """
    return [6, 1, 5, 6, 4, 6, 4, 3, 6, 6]

# Question 2.1
def number_of_adults_1(lst, age = 18):
    """
    For every three children younger than the given age 
    threshold, one adult is needed.
    ---
    Parameters:
        - lst (list of ints): Ages of individuals.
        - age (int): Age threshold, defaulted to 18.
    ---
    Returns:
        int: Number of adults needed.
    
    >>> number_of_adults_1([1,2,3,4,5,6,7])
    3
    >>> number_of_adults_1([1,2,3,4,5,6,7], 5)
    2
    >>> number_of_adults_1([1,2,3,4,5,6,7], age = 2)
    1
    """
    # def helper(lst):
    #     adults = sum(lst) // 3
    #     if sum(lst) % 3 > 0:
    #         adults += 1
    #     return adults
    # return helper([1 if num < age else 0 for num in lst])
    def helper(num_children):
        return (num_children + 2) // 3

    return helper(sum([1 for num in lst if num < age]))

# Question 2.2
def number_of_adults_2(*args):
    """
    For every three children younger than the given age 
    threshold, one adult is needed.
    --- 
    Parameters:
        *args (int): A variable number of integer
        ages to check. Each integer represents the 
        age of an individual.
    ---
    Returns:
        int: Number of adults needed.

    >>> number_of_adults_2(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_2(10,20,13,4)
    1
    >>> number_of_adults_2(19, 20)
    0
    """
    # def helper(tup):
    #     adults = sum(tup) // 3
    #     if sum(tup) % 3 > 0:
    #         adults += 1
    #     return adults
    # return helper([1 if arg < 18 else 0 for arg in args])
    def helper(num_children):
        return (num_children + 2) // 3  

    return helper(sum([1 for arg in args if arg < 18]))

# Question 2.3
def number_of_adults_3(*args, age = 18):
    """
    For every three children younger than the given age 
    threshold, one adult is needed.
    --- 
    Parameters:
        *args (int): A variable number of integer
        ages to check. Each integer represents the 
        age of an individual.
        age (int): Age threshold, defaulted to 18.
    ---
    Returns:
        int: Number of adults needed.
    
    >>> number_of_adults_3(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 5)
    2
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 2)
    1
    """
    # def helper(tup):
    #     adults = sum(tup) // 3
    #     if sum(tup) % 3 > 0:
    #         adults += 1
    #     return adults
    # return helper([1 if arg < age else 0 for arg in args])
    def helper(num_children):
        return (num_children + 2) // 3 

    return helper(sum([1 for arg in args if arg < age]))

# Question 3
def activities_of_children(activity, **kwargs):
    """
    Determines which children will participate in the proposed activity.
    ---
    Parameters:
        - activity (str): The activity to check participation for.
        - **kwargs: Variable keyword arguments where each key is a
        child's name and each value is a list of activities the 
        child is interested in.
    ---
    Returns:
    list of tuples: Each tuple contains the child's name
    and a boolean indicating whether the child will participate
    in the specified activity.

    >>> activities_of_children("soccer", Marina = ['soccer', \
    'basketball', 'tennis'], Rob = ['swimming', 'tennis'], \
    Adrian = ['tennis', 'soccer', 'volleyball'])
    [('Marina', True), ('Rob', False), ('Adrian', True)]

    >>> activities_of_children("swimming", Sam = ['soccer', \
    'swimming', 'tennis'], \
    Yue = ['volleyball', 'tennis'], \
    Pooja = ['badminton', 'running'])
    [('Sam', True), ('Yue', False), ('Pooja', False)]

    >>> activities_of_children("tennis", Karina = [], \
    Else=['soccer', 'swimming'], \
    David=['basketball', 'running'], \
    Yacun=['tennis', 'badminton'])
    [('Karina', False), ('Else', False), ('David', False), ('Yacun', True)]

    >>> activities_of_children("basketball")
    []
    """
    # return [(name, True) if activity in activities else (name, False) \
    #         for name, activities in kwargs.items()]
    return [(name, True) if activity.lower() in [act.lower() for act in activities] \
            else (name, False) \
            for name, activities in kwargs.items()]


# Question 4
def files_target_count(target, *args):
    """
    Get count of the target character across all files.
    Not case sensitive.
    ---
    Parameters:
        - target (str): the target character
        - *args: unspecified number of file names as strings
    ---
    Returns:
        - int: Target character count across all files.

    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('\\n', 'files/file1.txt', 'files/file2.txt')
    10
    >>> files_target_count('E', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('', 'files/file1.txt', 'files/file2.txt')
    0
    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt',\
     'files/file3.txt', 'files/file4.txt')
    99
    >>> files_target_count('\\n', 'files/file2.txt', 'files/file4.txt',\
     'files/file3.txt')
    26
    """
    count = 0
    for arg in args:
        with open(arg, 'r') as input:
            characters = [*input.read().lower()]
            for char in characters:
                if target.lower() == char:
                    count += 1
                if target == '\\n' and char == '\n':
                    count += 1
    return count

# Question 5
def field_trip(age_limit, **kwargs):
    """
    Determines the number of adults needed for each group based
    on the age limit. For every three children younger than the
    specified age limit, one adult is needed.
    ---
    Parameters:
        - age_limit (int): The maximum age considered as a child.
        - **kwargs: Variable keyword arguments where each key is 
        a group ID, and the value is a list of children's ages in 
        that group.
    ---
    Returns:
        dict: A dictionary where each key is a group ID, and the 
        value is the number of adults required for that group.

    >>> field_trip(14, group1 = [1, 2, 3], group2 = [4, 5, 6, 7], \
    group3=[15, 16])
    {'group1': 1, 'group2': 2, 'group3': 0}
        
    >>> field_trip(14, group1 = [21, 3], group2 = [41, 1, 2, 24, 6], \
    group3=[30, 3, 1, 7, 88])
    {'group1': 1, 'group2': 1, 'group3': 1}
        
    >>> field_trip(100, group1 = [21, 3], group2 = [41, 1000, 2, 24, 6], \
    group3 = [3, 1, 7, 88])
    {'group1': 1, 'group2': 2, 'group3': 2}
    """
    dct = {}
    for k, w in kwargs.items():
        dct[k] = number_of_adults_3(*w, age = age_limit)
    return dct