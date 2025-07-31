"""
DSC 20 Winter 2025 Homework 08
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50
    
    # ADD DOCTESTS HERE #

    >>> fbroom1 = FlyingBroom()
    >>> fbroom2 = FlyingBroom()
    >>> fbroom3 = FlyingBroom()

    >>> nbroom1 = NormalBroom()
    >>> nbroom2 = NormalBroom()
    >>> nbroom3 = NormalBroom()

    >>> cbroom1 = CursedBroom()
    >>> cbroom2 = CursedBroom()
    >>> cbroom3 = CursedBroom()

    # Test FlyingBroom boost method (done)
    >>> fbroom1.boost(10)
    True
    >>> fbroom1.speed
    72
    >>> fbroom1.magic_power
    2
    >>> fbroom1.high_score()
    8700
    >>> fbroom1.boost(20)
    True
    >>> fbroom1.boost(30)
    True
    >>> fbroom1.boost(40)
    False
    >>> fbroom1.magic_power
    0
    >>> fbroom1.speed
    154
    >>> fbroom1.high_score()
    16900

    # Test FlyingBroom duel with FlyingBroom (done)
    >>> fbroom2.duel(fbroom3)
    False
    >>> fbroom2.speed
    50
    >>> fbroom2.set_size(6)
    >>> fbroom2.duel(fbroom3)
    True
    >>> fbroom2.speed
    100
    >>> fbroom3.speed
    50
    >>> fbroom3.lives
    2
    >>> fbroom2.size
    7
    >>> fbroom2.duel(fbroom3)
    True
    >>> fbroom3.speed
    50
    >>> fbroom3.lives
    1
    >>> fbroom2.speed
    150
    >>> fbroom2.lives
    3
    >>> fbroom2.duel(fbroom3)
    True
    >>> fbroom2.duel(fbroom3)
    True
    >>> fbroom3.lives
    -1
    >>> fbroom2.speed
    250
    >>> fbroom3.high_score()
    4500

    # Test NormalBroom duel with FlyingBroom (done)
    >>> nbroom1.duel(fbroom2)
    False
    >>> nbroom1.speed
    50
    >>> fbroom2.speed
    300
    >>> fbroom2.lives
    3
    >>> nbroom1.lives
    2

    # Test NormalBroom duel with CursedBroom
    >>> nbroom2.duel(cbroom1)
    False
    >>> nbroom2.lives
    2
    >>> nbroom2.speed
    30
    >>> cbroom1.size
    8
    >>> cbroom1.speed
    120
    >>> nbroom2.duel(cbroom1)
    False
    >>> nbroom2.lives
    1
    >>> nbroom2.speed
    30
    >>> cbroom1.size
    9
    >>> cbroom1.speed
    170

    # Test CursedBroom high score
    >>> cbroom2.high_score()
    15750
    >>> cbroom2.boost(30)
    True
    >>> cbroom2.high_score()
    23150
    >>> cbroom2.lives
    5
    >>> cbroom2.set_lives(False)
    >>> cbroom2.high_score()
    22850

    # Test CursedBroom duel with another CursedBroom
    >>> cbroom1.duel(cbroom3)
    True
    >>> cbroom1.size         
    9
    >>> cbroom3.size
    7
    >>> cbroom3.lives
    5
    >>> cbroom3.speed
    20
    >>> cbroom1.duel(cbroom3)
    True
    >>> cbroom1.size         
    10
    >>> cbroom3.size
    7
    >>> cbroom3.lives
    4
    >>> cbroom3.speed
    50

    >>> broom_1.lives
    3
    >>> broom_1.boost(10000)
    True
    >>> broom_1.lives
    4
    """
    return

class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        self.speed = 50 
        self.size = 5 
        self.magic_power = 3 
        self.lives = 3 

    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        num_to_double = 2
        new_speed = int(((self.speed + charm_power)**2 + \
                         (self.speed - charm_power)**2)**0.5)
        old_score = self.high_score()
        if self.magic_power > 0:
            self.speed = new_speed
            self.magic_power -= 1
            if self.high_score() >= num_to_double * old_score:
                self.lives += 1
            return True
        else:
            return False

    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains:
            self.lives += 1
        else:
            self.lives -= 1

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        self.size = new_size

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        speed_gain_or_loss = 50
        if self.size > other_broom.size:
            other_broom.speed -= speed_gain_or_loss
            self.speed += speed_gain_or_loss
            if other_broom.speed <= 0:
                other_broom.lives -=1
                other_broom.speed = speed_gain_or_loss
                self.size += 1
            return True
        elif other_broom.size > self.size:
            other_broom.speed += speed_gain_or_loss
            self.speed -= speed_gain_or_loss
            if self.speed <= 0:
                self.lives -= 1
                self.speed = speed_gain_or_loss
                other_broom.size += 1
            return False
        else:
            return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        score = self.speed * 100 + self.lives * 500
        return score

class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        speed_gain = 50
        if isinstance(other_broom, CursedBroom):
            self.lives -= 1
            self.speed = 30
            other_broom.size += 1
            other_broom.speed += speed_gain
            return False
        else:
            return super().duel(other_broom)

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        self.speed = 70
        self.size = 7
        self.magic_power = 5
        self.lives = 5

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        score = self.speed * 200 + self.lives * 300 + 250
        return score


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    Divides each element in lst1 by each element in lst2, 
    avoiding division by zero.

    - If a divisor in lst2 is zero, that division is skipped.

    Parameters:
    - lst1 (list): A list of numbers (dividends).
    - lst2 (list): A list of numbers (divisors).

    Returns:
    - A new list with the results of division.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    >>> fix_1([4, 8, 16], [2, 4, 0])
    [2.0, 4.0, 8.0, 1.0, 2.0, 4.0]
    >>> fix_1([5, 10, 15], [5, 0, 1])
    [1.0, 2.0, 3.0, 5.0, 10.0, 15.0]
    >>> fix_1([-6, -12], [-3, 0, 2])
    [2.0, 4.0, -3.0, -6.0]

    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div) # add try-catch block
            except ZeroDivisionError:
                continue
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    Open multiple files and prints whether or not they can be opened.

    - If a file exists, it prints "<filename> opened".
    - If missing, it prints "<filename> not found".
    
    Parameters:
    - filepaths (str): One or more file paths.

    Returns:
    - None (prints file statuses).

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")
            print(f"{filepath} opened")
            cur_file.close() # add try-catch block
        except FileNotFoundError:
            print(f"{filepath} not found")

# Q2, Part 3
def fix_3(lst):
    """
    Processes a list by summing adjacent pairs of elements. 

    - If elements are incompatible for addition, a TypeError is printed.
    - If an index error occurs at the last element, an IndexError is printed.
    - Returns a list of summed adjacent pairs.

    Parameters:
    - lst (list): A list containing elements of any type.

    Returns:
    - list: A new list containing the sums of adjacent numeric elements.

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
        except TypeError as t:
            print(type(t))
            continue
        except IndexError as e:
            print(type(e))
            continue
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    Validates `input1` as a list of numbers and `input2` as a numeric value 
    present in `input1`.

    Parameters:
    - input1 (list): A list containing only integers and floats.
    - input2 (int | float): A numeric value to check if it exists in `input1`.

    Returns:
    - str: "Input validated" if all conditions are met.

    Raises:
    - TypeError: If `input1` is not a list.
    - TypeError: If any element in `input1` is not a numeric type.
    - TypeError: If `input2` is not a numeric type.
    - TypeError: If `input2` is not found in `input1`.

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here #
    >>> check_inputs([-1, -2.5, 3], -2.5)
    'Input validated'
    >>> check_inputs([1, 2.5, 3.0, 4], 2.5)
    'Input validated'
    >>> check_inputs([1, 2, 3], 3.0)
    'Input validated'
    >>> check_inputs([10, 20, 30], 25)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    """
    if not isinstance(input1, list):
        raise TypeError("input1 is not the correct type")
    for index, num in enumerate(input1):
        if not isinstance(num, (int, float)):
            raise TypeError(f"The element at index {index} is not numeric")
    if not isinstance(input2, (int, float)):
        raise TypeError("input2 is not the correct type")
    if input2 not in input1:
        raise TypeError("input2 not in input1")
    return "Input validated"
    
    


# Question 4
def load_file(filepath):
    """
    Loads a file, counts the number of words, and handles errors gracefully.

    - If `filepath` is not a string, raises `TypeError`.
    - If the file does not exist, raises `FileNotFoundError`.
    - If the file is empty, raises `ValueError`.
    - Otherwise, returns the number of words in the file.

    Parameters:
    - filepath (str): Path to the file.

    Returns:
    - int: Number of words in the file.

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here #
    >>> load_file('files/a.txt')
    1
    >>> load_file('files/twelve_words.txt')
    12
    >>> load_file('files/words.txt')
    4
    >>> load_file('files/newlines.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath is not a string")
    try:
        with open(filepath, 'r') as f:
            num_words = len(f.read().strip().split())
            if num_words == 0:
                raise ValueError("File is empty")
            else:
                return num_words
    except FileNotFoundError:
        raise FileNotFoundError(f"{filepath} does not exist")