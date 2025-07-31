"""
DSC 20 Winter 2025 Lab 05
Name: Steven Ngo
PID: A18461865
"""

# PRE-DEFINED FUNCTIONS
def identity(x):
    return x

def squared(x):
    return x**2

def cubed(x):
    return x**3

def root(x):
    return round(x ** 0.5, 2)

# Question 1
def vector_op(lst, func):
    """
    Applies function to each element in the list
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1, 2, 3]
    >>> vector_op(lst, squared)
    [1, 4, 9]
    >>> lst = [1, 2, 3, 5]
    >>> vector_op(lst, lambda x: -x)
    [-1, -2, -3, -5]
    >>> vector_op(lst, identity)
    [1, 2, 3, 5]
    >>> lst = [10, 20, 30]
    >>> vector_op(lst, cubed)
    [1000, 8000, 27000]
    """
    return [func(num) for num in lst]


# Question 2
def matrix_op(lsts, func):
    """
    Applies function to each element in the 2D list
    --
    Parameters:
        lsts: list of lists of numbers
        func: a function to be applied
    --
    Returns:
        List of lists of transformed numbers

    >>> lsts = [[1,2], [3,4]]
    >>> matrix_op(lsts, squared)
    [[1, 4], [9, 16]]
    >>> lsts = [[10, 20], [30, 40]]
    >>> matrix_op(lsts, lambda x: x / 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> lsts = [[5,15], [25,35]]
    >>> matrix_op(lsts, identity)
    [[5, 15], [25, 35]]
    """
    return [vector_op(lst, func) for lst in lsts]

# Question 3
def hop_hop(lst, func):
    """
    Applies function to each element in list twice
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_hop(lst, squared)
    [1, 16, 81]
    >>> lst = [5,6,7,8]
    >>> hop_hop(lst, lambda x:x+1)
    [7, 8, 9, 10]
    >>> lst = [10,20,30]
    >>> hop_hop(lst, cubed)
    [1000000000, 512000000000, 19683000000000]
    """
    return [func(num) for num in [func(num) for num in lst]]

# Question 4
def hop_many(lst, func, iterations):
    """
    Applies function to each element in list specified number of times
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
        iterations: number of times to perform operation
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_many(lst, squared, 2)
    [1, 16, 81]
    >>> hop_many(lst, squared, 3)
    [1, 256, 6561]
    >>> hop_many(lst, identity, 100)
    [1, 2, 3]
    >>> hop_many(lst, lambda x: x - 1, 4)
    [-3, -2, -1]
    """
    new_lst = vector_op(lst, func)
    for i in range(iterations-1):
        new_lst = vector_op(new_lst, func)
    return new_lst 

# Question 5
def grades_stats(input_lst, choice):
    """
    Calculates mean, median, or both stats for input list. `choice` is 
    1 for median, 2 for mean, and any other for both stats.
    --
    Parameters:
        input_lst: list of integers
        choice: positive integer representing each stat
    --
    Returns:
        Stats of the input list

    >>> lst = [3, 2, 1]
    >>> grades_stats(lst, 1)
    2
    >>> grades_stats(lst, 2)
    2.0
    >>> grades_stats(lst, 0)
    (2, 2.0)
    >>> lst = [1, 2, 4]
    >>> grades_stats(lst, 2)
    2.33
    >>> grades_stats(lst, -1)
    (2, 2.33)
    """
    def find_median(): # Calculate median
        sorted_lst = sorted(input_lst)
        if len(sorted_lst) % 2 == 1:
            return sorted_lst[len(input_lst) // 2]
        else:
            return (sorted_lst[len(input_lst) // 2] + sorted_lst[len(input_lst) // 2 - 1]) / 2

    def find_mean(): # Calculate mean
        return round(sum(input_lst) / len(input_lst), 2)

    if choice == 1:
        return find_median()
    elif choice == 2:
        return find_mean()
    else:
        return (find_median(), find_mean())
    

# Question 6
def calculate_final_price(original_price, category, season):
    """
    Calculates price of item after discount.
    --
    Parameters:
        original_price: number representing price of item
        category: string category of item that category discount is based on
        season: string season that seasonal discount is based on
    --
    Returns:
        The final price of item after applying potential discounts
    
    >>> calculate_final_price(120, 'electronics', 'Spring')
    108.0
    >>> calculate_final_price(45, 'clothing', 'Winter')
    30.6
    >>> calculate_final_price(100, 'appliance', 'Spring')
    100
    """

    def apply_category_discount():
        if category == 'electronics':
            return original_price * 0.9
        elif category == 'clothing':
            return original_price * 0.8
        elif category == 'home':
            return original_price * 0.9
        else:
            return original_price

    def apply_seasonal_discount(amount):
        if season == 'Winter':
            return amount * 0.85
        elif season == 'Summer':
            return amount * 0.9
        elif season == 'Fall':
            return amount * 0.95
        else:
            return amount

    final_price = apply_category_discount()
    final_price = round(apply_seasonal_discount(final_price), 2)
    return final_price
