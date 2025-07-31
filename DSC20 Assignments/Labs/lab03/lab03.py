"""
DSC 20 Winter 2025 Lab 03
Name: Steven Ngo
PID: A18461865
"""

# Problem 1.1
def keep_a_secret(filename):
    """
    Decodes message from the given input file.

    >>> print(keep_a_secret('files/encoded_1.txt').strip())
    jack reacher
    23@4 b#l31oo%m@^ way
    FSD@si%m3~on fis#he%r
    121 rockefeller avenue
    32'1 fulleH##r "dr^i~v@e
    @@4:)5#0p1m#
    7/29 06.45
    >>> print(keep_a_secret('files/encoded_2.txt').strip())
    kurt hendricks
    simon 1p@egg
    @kremlin office
    b%i>%g@ be>n @lond#o&&n
    moscow
    @reykj@av>>ik:/
    12:50 23/11
    >>> print(keep_a_secret('files/encoded_3.txt').strip())
    <BLANKLINE>
    >>> keep_a_secret('files/encoded_4.txt').strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    new_string = ''
    with open(filename, 'r') as f:
        for line in f.readlines():
            new_string += line.replace('!', '').replace('?', '') \
                .replace(';', '').replace('$', '').strip() + '\n'
    return new_string


# Problem 1.2
def skipped_lines(filename, skip):
    """
    Decodes message from the given input file by skipping some lines

    >>> print(skipped_lines('files/encoded_1.txt', 1).strip())
    jack reacher
    FSD@si%m3~on fis#he%r
    32'1 fulleH##r "dr^i~v@e
    7/29 06.45
    >>> print(skipped_lines('files/encoded_2.txt', 2).strip())
    kurt hendricks
    b%i>%g@ be>n @lond#o&&n
    12:50 23/11
    >>> print(skipped_lines('files/encoded_3.txt', 1).strip())
    <BLANKLINE>
    >>> skipped_lines('files/encoded_4.txt', 0).strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    new_string = ''
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), skip+1):
            new_string += lines[i].replace('!', '').replace('?', '') \
                .replace(';', '').replace('$', '').strip() + '\n'
    return new_string


# Problem 2.1
def loose_change(lst):
    """
    Converts each integer to dollars and cents format

    >>> loose_change([200, 456])
    ['2 dollar(s) and 0 cents', '4 dollar(s) and 56 cents']
    >>> loose_change([9])
    ['0 dollar(s) and 9 cents']
    >>> loose_change([])
    []
    >>> loose_change([7, 77, 777, 7777])
    ['0 dollar(s) and 7 cents', '0 dollar(s) and 77 cents', '7 dollar(s) \
and 77 cents', '77 dollar(s) and 77 cents']
    """
    return [f'{int(item / 100)} dollar(s) and {item % 100} cents' for item in lst ]


# Problem 2.2
def ignore_cents(lst):
    """
    >>> ignore_cents([20, 46, 24])
    0
    >>> ignore_cents([])
    0
    >>> ignore_cents([120, 746, 3224, 15])
    40
    """
    return sum([int(item / 100) for item in lst])


# Problem 2.3
def ignore_cents_and_small_amount(lst):
    """
    Finds total of changes, ignoring those less than $50 and cents

    >>> ignore_cents_and_small_amount([34, 245, 6678, 16608])
    232
    >>> ignore_cents_and_small_amount([120, 746, 3224, 15])
    0
    >>> ignore_cents_and_small_amount([])
    0
    >>> ignore_cents_and_small_amount([12345, 50000, 4999])
    623
    """
    return sum([int(item / 100) if int(item / 100) >= 50 else 0 for item in lst])


# Problem 2.4
def keep_dollars_only(lst):
    """
    Returns a list of dollar amount, or 'skip' for other currencies

    >>> keep_dollars_only([(150, "dollars"), (80, "euros"), (120, "euros")])
    [150, 'skip', 'skip']
    >>> keep_dollars_only([(133, "euros"), (72, "rubles"), (120, "renminbi")])
    ['skip', 'skip', 'skip']
    >>> keep_dollars_only([(19, "dollars"), (275, "dollars"), (100, "dollars")])
    [19, 275, 100]
    """
    return [tup[0] if tup[1] == "dollars" else 'skip' for tup in lst]


# Problem 3
def combine_the_strings(names):
    """
    Returns a list of each name individually

    >>> combine_the_strings([("Tom", "Cruise"), ("Jon", "Voight"),("Henry",)])
    ['Tom', 'Cruise', 'Jon', 'Voight', 'Henry']
    >>> combine_the_strings([()])
    []
    >>> combine_the_strings([])
    []
    >>> combine_the_strings([("Marina", "Langlois")])
    ['Marina', 'Langlois']
    """
    return [item for tup in names for item in tup ]


# Problem 4
def selected_name(names, char):
    """
    Return the first name for names with char in its last name

    >>> selected_name(['Marina Langlois', 'James Bond', 'Austin Madden'], 'E')
    ['Austin']
    >>> selected_name(['Martina Sampson', 'Jill Gordon', 'Cary Barber'], 's')
    ['Martina']
    >>> selected_name(['Dana Donaldson', 'Selma Owen'], 'Z')
    []
    """
    return [name.split(' ')[0] for name in names if char.upper() in name.split(' ')[1].upper()]


# Problem 5
def pay_reaction(proposed_salaries):
    """
    >>> pay_reaction([2200, 1400, 55, 1991])
    ['Will take it', 'Thinking', 'Not enough', 'Thinking']
    >>> pay_reaction([])
    []
    >>> pay_reaction([0.01, 100000])
    ['Not enough', 'Will take it']
    """
    return ['Not enough' if i <= 1000 else 'Thinking' if 1000 <= i <= 2000 else 'Will take it' for i in proposed_salaries]


# Question 6.1
def months_to_years(ages):
    """
    Converts each age in months from the input to the whole numbers of years

    >>> ages = [[110, 154, 345], [4, 61]]
    >>> months_to_years(ages)
    [[9, 12, 28], [0, 5]]
    >>> ages = [[], []]
    >>> months_to_years(ages)
    [[], []]
    >>> ages = [[200], [615, 0]]
    >>> months_to_years(ages)
    [[16], [51, 0]]
    """
    return [[int(item/12) for item in age] for age in ages]


# Question 6.2
def harder_convert(ages):
    """
    Converts each age in months from the input to the whole numbers of years
    Replace with 0 if an age is negative

    >>> ages = [[119, 14, -34], [5, -177, -232, 362]]
    >>> harder_convert(ages)
    [[9, 1, 0], [0, 0, 0, 30]]
    >>> ages = [[], []]
    >>> harder_convert(ages)
    [[], []]
    >>> ages = [[132], [-65, 0]]
    >>> harder_convert(ages)
    [[11], [0, 0]]
    """
    return [[int(item/12) if item >= 0 else 0 for item in age] for age in ages]


# Question 6.3
def older_than_30(ages):
    """
    Counts the number of people at least as old as 30 years

    >>> ages = [[120, -154, 245], [145, -360, -615, 306]]
    >>> older_than_30(ages)
    0
    >>> ages = [[8848], [779, 0]]
    >>> older_than_30(ages)
    2
    >>> ages = [[80, -854, 900], [45, 360, 15]]
    >>> older_than_30(ages)
    2
    """
    return len([int(item/12) for age in ages for item in age if int(item/12) >= 30])
