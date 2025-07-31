"""
DSC 20 Winter 2025, Lab 07
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

# Question 1
def max_recursion(tup):
    """
    Find the maximum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
    Returns:
        The maximum number

    >>> max_recursion((1,2,3,4))
    4
    >>> max_recursion((13,2,3,4))
    13
    >>> max_recursion((13,2,33,4))
    33
    """
    if len(tup) == 1:
        return tup[0]
    max_remaining = max_recursion(tup[1:])
    if tup[0] >= max_remaining:
        return tup[0]
    else:
        return max_remaining



# Question 2
def max_or_min_recursion(tup, find_max = True):
    """
    Find the maximum or minimum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
        find_max (bool): whether to find max or min
    Returns:
        The maximum or minimum number

    >>> max_or_min_recursion((1,2,3,4))
    4
    >>> max_or_min_recursion((13,2,3,4), False)
    2
    >>> max_or_min_recursion((13,2,33,-4), True)
    33
    """
    if len(tup) == 1:
        return tup[0]
    remaining = max_or_min_recursion(tup[1:], find_max)
    if find_max is True:
        if tup[0] >= remaining:
            return tup[0]
        else:
            return remaining
    else:
        if tup[0] < remaining:
            return tup[0]
        else:
            return remaining



# Question 3
def find_winner(record, find_max = True):
    """
    Find the team with highest or lowest score recursively.

    Args:
        record (list): a list of tuples, where the first element in each tuple 
        is the team's name and the second element is the team's score
        find_max (bool): whether to find team with max or min score
    Returns:
        The team with highest or lowest score, and returns first if there is
        a tie

    >>> find_winner([('Red',23),('Green', 49), ('Blue', 32)])
    'Green'
    >>> find_winner([('UCSD', 12.88),('SDSU', 15)], find_max=False)
    'UCSD'
    >>> find_winner([('Panda', 10), ('Koala', 10), ('Hippo', 5)], find_max=True)
    'Panda'
    >>> find_winner([('Panda', 10), ('Koala', 10), ('Hippo', 11)])
    'Hippo'
    """

    def create_dct(lst):
        if len(lst) == 0:
           return {}
        else:
            dct = create_dct(lst[:-1])
            if lst[-1][1] not in dct:
                dct[lst[-1][1]] = lst[-1][0]
            return dct
        
    dct = create_dct(record)

    def find(record, find_max):
        if len(record) == 1:
            return record[0][1]
        remaining = find(record[1:], find_max)
        if find_max is True:
            if record[0][1] >= remaining:
                return record[0][1]
            else:
                return remaining
        else:
            if record[0][1] < remaining:
                return record[0][1]
            else:
                return remaining
    return dct[find(record, find_max)]



# Question 4
def from_list_to_dict(lst):
    """
    Converts a list of tuples into a dictionary recursively.

    Args:
        lst (list): a list of tuples, where the first element is the team name 
        (key) and second element is their score (value)
    Returns:
        A dictionary with each team name as keys and their score as values

    >>> lst = [(1,2),(3,4),(5,6)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6}

    >>> lst = [("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {'one': 1, 'two': 2}

    >>> lst = []
    >>> from_list_to_dict(lst)
    {}
    """
    if len(lst) == 0:
        return {}
    k, w = lst[-1]
    remaining = from_list_to_dict(lst[:-1])
    remaining.update({k: w})
    return remaining



# Question 5
class Mascot:
    """ 
    Creates a simple Mascot class with 1 class attribute (type)
    and 3 instance attributes (color, nickname, event)
    >>> mascot1 = Mascot("blue and white", "Shark", "West Athletic Conference")
    >>> Mascot.brings
    'Luck'
    >>> mascot1.color
    'blue and white'
    >>> mascot1.sing_song("Baby Shark")
    "Shark sings 'Baby Shark' at West Athletic Conference"
    >>> mascot1.change_nickname("Doo Doo")
    >>> mascot1.nickname
    'Doo Doo'
    >>> mascot1.event
    'West Athletic Conference'


    >>> mascot2 = Mascot('green', 'Stanford Tree',\
'Collegiate Football Conference')
    >>> Mascot.brings
    'Luck'
    >>> mascot2.color
    'green'
    >>> mascot2.sing_song("Deck the Halls")
    "Stanford Tree sings 'Deck the Halls' at Collegiate Football Conference"
    >>> mascot2.change_nickname("The Tree")
    >>> mascot2.nickname
    'The Tree'
    """
    brings = "Luck"
    
   
 # Initializer (Constructor) / Instance Attributes
    def __init__(self, color, nickname, event):
        self.color = color
        self.nickname = nickname
        self.event = event


    def sing_song(self, song):
        return "{0} sings '{1}' at {2}".format(self.nickname, song, self.event)


    def change_nickname (self, new_name):
        self.nickname = new_name



# Question 6
class Game:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Game.mascot
    'King Triton'
    >>> Game.starts()
    'Saturday, November 2'
    >>> Game.ends()
    'Sunday, November 17'
    """
    mascot = 'King Triton'

    def starts():
        return "Saturday, November 2"
    def ends():
        return "Sunday, November 17"