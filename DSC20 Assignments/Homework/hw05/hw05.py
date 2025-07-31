"""
DSC 20 Winter 2025 Homework 05
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    Takes in a dictionary of customer data and returns a list of customer
    ID's only if their average score is less than or equal to the given max
    average, and if their score range is greater than or equal to the given
    minimum range.

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    >>> data = { \
        "Alex": [4, 5, 6, 7, 8, 9, 10], \
        "Jamie": [15, 15, 15], \
        "Casey": [1, 1, 1, 1, 1] \
    }
    >>> get_qualified_customers(data, 10, 6)
    ['Alex']

    >>> data = { \
        "Morgan": [8, 8, 8, 8], \
        "Blake": [5, 6, 7, 8], \
        "Jordan": [10, 10, 10] \
    }
    >>> get_qualified_customers(data, 6, 1)
    []

    >>> data = { \
        "Riley": [2, 3, 5], \
        "Pat": [9, 10, 11], \
        "Quinn": [3, 3, 3, 3] \
    }
    >>> get_qualified_customers(data, 8, 2)
    ['Riley']
    """
    assert isinstance(data, dict)
    assert isinstance(max_avg, int)
    assert isinstance(min_range, int)
    assert all([isinstance(key, str) for key in data.keys()])
    assert all(isinstance(value, list) and all(isinstance(num, int) \
        for num in value) for value in data.values())

    valid_customers = {key: value for key, value in data.items() \
        if len(set(value)) == len(value)}
    score_range = lambda scores: max(scores) - min(scores) if scores else 0
    score_avg = lambda scores: sum(scores) / len(scores) if scores else 0

    return [customer for customer, scores in valid_customers.items() \
        if score_avg(scores) <= max_avg and score_range(scores) >= min_range]


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    Reads a text file in the format: company_name,person_in_charge,email,
    decision, and returns a list of string messages to send to the customers
    based on the given message and each line's respective decision.

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "W", msg)
    Traceback (most recent call last):
    AssertionError
    
    >>> msg = "we are sorry to decline your offer."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
we are sorry to decline your offer.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
we are sorry to decline your offer.']

    >>> message_to_customers("files/customers.txt", "s", [1, 2, 3])
    Traceback (most recent call last):
    AssertionError

    >>> message_to_customers(["files/customers.txt"], "w", msg)
    Traceback (most recent call last):
    AssertionError
    
    """
    email_index = 2
    assert isinstance(customer_file, str)
    assert decision == "s" or decision == "w"
    assert isinstance(message, str)
    with open(customer_file, 'r') as c:
        lines = c.readlines()
        messages = [f"(to: {line.split(',')[email_index]}) " \
            f"Dear {line.split(',')[1]} " \
            f"at {line.split(',')[0]}, {message}" for line in lines \
                if line.strip()[-1] == decision]
        return messages



# Question 3

def forge_votes(vote_file):
    """
    Takes a file of votes and changes the least amount of votes such that a 
    majority vote of greater than 50% is achieved, and such changes are written
    into a new file "forged.txt".

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    >>> forge_votes("files/vote4.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote5.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,1
    Clyde,1
    Andy,0

    >>> forge_votes("files/vote6.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,1
    Clyde,0
    Andy,1
    """
    half = 2
    with open(vote_file, 'r') as v:
        votes = v.readlines()
        names = [vote.strip().split(',')[0] for vote in votes]
        yes = [int(vote.strip().split(',')[1]) for vote in votes]
        total_yes = sum(yes)
        total_votes = len(votes)
        votes_needed = (total_votes // half + 1) - total_yes
        if votes_needed > 0:
            zero_indices = [i for i, vote in zip(range(total_votes), yes) \
                            if vote == 0][:votes_needed]
            forged_votes = [str(yes[i]) if i not in zero_indices else "1" \
                            for i in range(total_votes)]
        else:
            forged_votes = [str(y) for y in yes]

        forged_lines = [f"{names[i]},{forged_votes[i]}\n" \
                        for i in range(total_votes)]
    with open("files/forged.txt", 'w') as f:
            f.write("".join(forged_lines))
             
        
    


# Question 4

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    return [True, True, False, True, False, True, False, True, False, False]