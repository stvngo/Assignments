"""
DSC 20 Winter 2025 Homework 09
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

# Question 1
def question_1():
    """
    1 if a method mutates an object 
	0 otherwise

	>>> answer = question_1()
	>>> len(answer) == 10
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer])
	False
    """
    return [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]


# Question 2
def question_2():
    """
    1 if a method is in place
	0 otherwise

	>>> answer = question_2()
	>>> len(answer)==5
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer ])
	False
    """
    return [1, 0, 1, 0, 1]


# Question 3
def reverse_list(lst):
    """ 
    Reverses a given list in place only by mutating its contents, while
    returning None.

    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add at least 3 doctests below here #
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> reverse_list(x)
    >>> x
    [6, 5, 4, 3, 2, 1]

    >>> x = ['a', 'b', 'c', 'd']
    >>> reverse_list(x)
    >>> x
    ['d', 'c', 'b', 'a']

    >>> x = [True, False, True]
    >>> reverse_list(x)
    >>> x
    [True, False, True]
    """
    # iterate through half of the list or else it will reverse itself twice.
    split_num = 2
    for i in range(0, len(lst) // split_num): 
        lst[i], lst[-i-1] = lst[-i-1], lst[i]



# Question 4
def swap_lists(alist1, alist2):
    """
    Takes in two lists and swaps their elements in place.

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]

    # Add at least 3 doctests below here #
    >>> list1 = [7, 8, 9]
    >>> list2 = [1, 2, 3]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [1, 2, 3]
    >>> print(list2)
    [7, 8, 9]

    >>> list1 = [10, 20, 30, 40]
    >>> list2 = [50, 60, 70, 80]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [50, 60, 70, 80]
    >>> print(list2)
    [10, 20, 30, 40]

    >>> list1 = ['a', 'b', 'c']
    >>> list2 = ['x', 'y', 'z']
    >>> swap_lists(list1, list2)
    >>> print(list1)
    ['x', 'y', 'z']
    >>> print(list2)
    ['a', 'b', 'c']
    >>> swap_lists(list1, list2)
    >>> print(list1)
    ['a', 'b', 'c']
    >>> print(list2)
    ['x', 'y', 'z']
    """
    for i in range(len(alist1)):
        alist1[i], alist2[i] = alist2[i], alist1[i]