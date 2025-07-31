"""
DSC 20 Winter 2025 Homework 01
Name: Steven Ngo
PID: A18461865
"""

# Question 1
def login(fname, lname):
    """
    Reconstructs the string parameters and returns them as a concatenated
    output string.
    ---
    Parameters:
        fname: first name, as a string
        lname: last name, as a string
    ---
    Returns:
        New login string

    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'
    >>> login("Orange", "County")
    'enrCn'
    >>> login("", "Adam")
    'Am'
    >>> login("Eve", "")
    'eE'
    """
    first_reversed = ''
    last_third = ''
    every_other = 2
    every_three = 3
    for i in range(len(fname)-1, -1, -every_other):
        first_reversed += fname[i]
    for i in range(0, len(lname), every_three):
        last_third += lname[i]
    return first_reversed + last_third


# Question 2
def ages(age1, age2):
    """
    Returns the greatest age under 23. If both ages are at least 23 or
    older, return a string describing ability of both ages to rent.
    ---
    Parameters:
        age1: First age as a positive integer
        age2: Second age as a positive integer
    ---
    Returns:
        Greatest age under 23 as an integer. String if both arguments are
        23 or greater

    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19
    >>> ages(23, 23)
    'You both can rent!'
    >>> ages(22, 17)
    22
    >>> ages(22, 24)
    22
    >>> ages(21, 21)
    21
    """
    threshold = 23
    if (age1 >= threshold) and (age2 >= threshold):
        return "You both can rent!"
    elif (age1 >= threshold) and (age2 < threshold):
        return age2
    elif (age1 < threshold) and (age2 >= threshold):
        return age1
    elif (age1 < threshold) and (age2 < threshold):
        if age1 > age2:
            return age1
        elif age1 < age2:
            return age2
        elif age1 == age2:
            return age1


# Question 3
def renter(name1, name2, name3):
    """
    Returns the longest name given. If name lengths are the same, returns
    the last name in the list of parameters.
    ---
    Parameters:
        name1: First name as a string
        name2: Second name as a string
        name3: Third name as a string
    ---
    Returns:
        A last name string with the most characters

    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'
    >>> renter("Joy", "BB", "Su")
    'Joy'
    >>> renter("Jake", "Brian", "Alex")
    'Brian'
    >>> renter("Jake", "Alex", "Jo")
    'Alex'
    >>> renter("Alex", "Jo", "Brian")
    'Brian'
    """
    if (len(name3) >= len(name2)) and (len(name3) >= len(name1)):
        return name3
    elif (len(name2) >= len(name1)) and (len(name2) > len(name3)):
        return name2
    elif (len(name1) > len(name2)) and (len(name1) > len(name3)):
        return name1


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    Calculates and returns the Euclidean distance between two given x and y
    coordinates.
    ---
    Parameters:
        lst: A list containing 2 floating point integers, representing
        x and y coordinates 
        x2: A floating point number representing the x starting point
        y2: A floating point number representing the y starting point
    ---
    Returns:
        The distance between the two coordinate points as a float
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance([100, 100], 100.5, 100)
    0.5
    >>> helper_distance([-1, -1], -1,-1)
    0.0
    >>> helper_distance([-4,20], 0, 20)
    4.0
    >>> helper_distance([20, 4], 20, 0)
    4.0
    """
    distance = ((x2 - lst[0])**2 + (y2 - lst[1])**2)**(1/2)
    return distance


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    Returns a list of lists containing the coordinates of each lunch place 
    with a distance less than or equal to the given threshold from the office
    ---
    Parameters:
        lunch_places: A list of lists, containing 2 floating point numbers
        office_x: The x-coordinate starting point as a floating point number
        office_y: The y-coordinate starting point as a floating point number
        threshold: A positive integer 
    ---
    Returns:
        A list of lists containing coordinates of each eligible lunch place

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch([[100, 100]], 100.5, 100, 0.2)
    []
    >>> lunch([[0, 0], [-3, -4]], 3, 4, 7.5)
    [[0, 0]]
    >>> lunch([[20, 4], [-4, 20]], 0, 20, 4)
    [[-4, 20]]
    >>> lunch([[0, 0]], 0, 0, 0)
    [[0, 0]]
    """
    distances = []
    for i in lunch_places:
        if helper_distance(i, office_x, office_y) <= threshold:
            distances.append(i)
    return distances


# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    Returns the places in which their distance from the office 
    coordinates are within the distance threshold.
    ---
    Parameters:
        lunch_places: A list of lists, containing 2 floating point numbers
        office_x: The x-coordinate starting point as a floating point number
        office_y: The y-coordinate starting point as a floating point number
        threshold: A positive integer 
        names: The name of the place as a string
    ---
    Returns:
        A list of the places as strings

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []
    >>> lunch_names([[0, 0], [-3, -4]], 3, 4, 7.5, ['place1', 'place2'])
    ['place1']
    >>> lunch_names([[20, 4], [-4, 20]], 0, 20, 4, ['place1', 'place2'])
    ['place2']
    >>> lunch_names([[0, 0]], 0, 0, 0, ['place1'])
    ['place1']
    """
    index = 0
    places = []
    for i in lunch(lunch_places, office_x, office_y, threshold):
        if i in lunch_places:
            index = lunch_places.index(i)
            places.append(names[index])
    return places


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    Creates a message with the given time, place, and names of the invitee
    and sender
    ---
    Parameters:
        i_name: Name of the invitee as a string
        time: Time of day as a string
        place: Location as a string
        s_name: Name of message creator as a string
    ---
    Returns:
        An invitation as a string
    
    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon
    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina
    >>> print(meeting_message("", "", "", ""))
    Dear ,
    Please join our meeting at , at the .
    <BLANKLINE>
    See you soon: 
    >>> print(meeting_message("William Shakespeare", "12:30pm sharp", \
    "Cathedral", "Steven"))
    Dear William Shakespeare,
    Please join our meeting at 12:30pm sharp, at the Cathedral.
    <BLANKLINE>
    See you soon: Steven
    >>> print(meeting_message(" ", " ", " ", "Frank"))
    Dear  ,
    Please join our meeting at  , at the  .
    <BLANKLINE>
    See you soon: Frank
    """
    return "Dear " + i_name + ",\nPlease join our meeting at " + time + \
        ", at the " + place + ".\n\nSee you soon: " + s_name


# Question 7
def seat_number(lst):
    """


    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]
    >>> seat_number(["Marina", "Andrew", "Sue", "Ben"])
    [6, 'taken', 3, 'taken']
    >>> seat_number(["Sue", "Ben", "Rey", "Frank", "Nik"])
    [3, 'taken', 'taken', 5, 'taken']
    >>> seat_number(["", "Ben", ""])
    [0, 3, 'taken']
    """
    seats = []
    for i in lst:
        if len(i) not in seats:
            seats.append(len(i))
        else:
            seats.append('taken')
    return seats


# Question 8
def computers(choices):
    """
    Calculates whether or not people chose desktop more than laptop.
    ---
    Parameters:
        choices: list of choices as strings
    Returns:
        A Boolean signifying more choices for desktop

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False
    >>> computers(["DESKtop", "desktop", "DESKtop"])
    True
    >>> computers(["LAPtop", "laptop"])
    False
    >>> computers(["DESKtop", "LAPtop"])
    False
    """
    if choices.count("DESKtop") > choices.count("LAPtop"):
        return True
    else:
        return False


# Question 9
def age_average(lst):
    """
    Calculates the average of all positive given ages,
    ommitting negative values.
    ---
    Parameters:
        lst: List of strings representing ages
    Returns:
        The age average as a string of only positive numbers, rounded
        to one decimal place
    
    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'
    >>> age_average(["-50", "41", "43", "43"])
    '42.3'
    >>> age_average(["-50", "-40", "-30"])
    '0.0'
    >>> age_average(["-50", "-300", "25"])
    '25.0'

    """
    total = 0
    average = 0
    positives = 0
    if len(lst) != 0:
        for i in lst:
            if int(i) > 0:
                total += int(i)
                positives += 1
        if positives == 0:
            return "0.0"
        else:
            average = total / positives
            return str(round(average, 1))
    else:
        return "0.0"


# Question 10
def supervision_teams(team, company_name):
    """
    Creates a team of odd indexed participants and one of even indexed
    participants, labeling each by the name of the painting company (at
    the beginning for the first, at the end for the second).
    ---
    Parameters:
        team: A list of participants as strings
        company_name: The company's name as a string
    ---
    Returns:
        A list of lists containing strings of the newly ordered team and 
        company name

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])
    >>> supervision_teams([], "Steven")
    (['Steven'], ['Steven'])
    >>> supervision_teams(["p1", "p2", "p3"], "")
    (['', 'p1', 'p3'], ['p2', ''])
    >>> supervision_teams([], "")
    ([''], [''])
    """
    team_1 = [str(company_name)]
    team_2 = []
    step = 2
    for i in range(0, len(team), step):
        team_1.append(team[i])
    for i in range(1, len(team), step):
        team_2.append(team[i])
    team_2.append(str(company_name))
    return (team_1 , team_2)
    