"""
DSC 20 Winter 2025 Homework 04
Name: Steven Ngo
PID: A18461865
Source: W3Schools
"""

# Question 1
def place_of_birth(file_in):
    """
    Creates a dictionary where the keys are the city names and the values are 
    lists of people who are born in that city from the given file.

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}
    >>> place_of_birth('files/info_3.txt')
    {'San Diego': ['Sue'], 'London': ['Ben']}
    >>> place_of_birth('files/info_4.txt')
    {'Paris': ['Kate']}
    >>> place_of_birth('files/info_5.txt')
    {'paris': ['Ron', 'Harry', 'Harry'], 'Paris': ['Ron'], 'Chicago': ['Rob']}
    """
    cleaned_dct = {}
    with open(file_in, 'r') as f:
        lines = f.readlines()
        if len(lines) <= 1:
            return cleaned_dct
        for line in lines[1:]:
            name, city, dob = \
                [word.strip() for word in line.strip().split(", ")]
            if city not in cleaned_dct:
                cleaned_dct[city] = []
            cleaned_dct[city].append(name) 
    return cleaned_dct


# Question 2
def age_groups(file_in, file_out):
    """
    Writes into a new file the name and their categorization of either older
    than 35, younger than 35, or exactly 35, taken from each line of the input
    file.

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    >>> age_groups('files/info_3.txt', 'files/age_3_out.txt')
    >>> with open('files/age_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,older than 35
    Sue,-1
    Ben,1

    >>> age_groups('files/info_4.txt', 'files/age_4_out.txt')
    >>> with open('files/age_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,older than 35
    Kate,1

    >>> age_groups('files/info_5.txt', 'files/age_5_out.txt')
    >>> with open('files/age_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,older than 35
    Ron,0
    Harry,0
    Ron,0
    Rob,-1
    Harry,0
    """
    new_string = 'name,older than 35\n'
    current_year = 2024
    year_limit = 35
    dob_i = 2
    with open(file_in, 'r') as f_in:
        lines = f_in.readlines()
        for line in lines[1:]:
            name, city, dob = \
                [word.strip() for word in line.strip().split(", ")]
            if (current_year - int(dob.split('/')[dob_i])) > year_limit:
                new_string += name + ',1\n'
            elif (current_year - int(dob.split('/')[dob_i])) < year_limit:
                new_string += name + ',-1\n'
            else:
                new_string += name + ',0\n'
    with open(file_out, 'w') as f_out:
        f_out.write(new_string.strip())
    
                

# Question 3
def several_files(files_lst, file_out):
    """
    Writes into a new file a combined and modified version of the lines of the
    given files, where the  date of birth is modified on each line to fit the
    format: Month (name) DD YYYY.

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt')
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt')
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989

    >>> lst_3 = ['files/info_3.txt','files/info_2.txt']
    >>> several_files(lst_3, 'files/several_3_out.txt')
    >>> with open('files/several_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,city,DOB
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989

    >>> lst_4 = ['files/header.txt']
    >>> several_files(lst_4, 'files/several_4_out.txt')
    >>> with open('files/several_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,city,DOB

    >>> lst_5 = ['files/info_1.txt', 'files/info_1.txt']
    >>> several_files(lst_5, 'files/several_5_out.txt')
    >>> with open('files/several_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    """
    months_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',\
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    new_string = 'name,city,DOB\n'
    dob_i = 2
    for file in files_lst:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                name, city, dob = \
                    [word.strip() for word in line.strip().split(", ")]
                new_string += \
                    f"{name},{city},{months_dict[int(dob.split('/')[0])]} " \
                    f"{dob.split('/')[1]} {dob.split('/')[dob_i]}\n"
    with open(file_out, 'w') as f_out:
        f_out.write(new_string)
    


# Question 4
def postcards(info_list):
    """
    Generates postcards by taking the first three letters of the person's first
    name, their age, the person's last name, the last digit of the price, and 
    the reversed price, and putting them into a list as a value of a dictionary
    with the full name as a key, only for prices lower than 75.

    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios')
    ... ])
    {'Cleo Patra': 'cle32patra0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram'),
    ...     ('Gwen Am', 34, 54, 'Venetian'),
    ...     ('Freya Dog', 34, 1, 'The Strip')
    ... ])
    {'Gwen Am': 'gwe54am4naitenev', 'Freya Dog': 'fre1dog4pirts eht'}
    >>> postcards([
    ...     ('Lara Croft', 76, 27, 'Pyramid'),
    ...     ('John Doe', 80, 42, 'Mirage')
    ... ])
    {}
    >>> postcards([
    ...     ('Alice Wonder', 20, 99, 'Paris'),
    ...     ('Bob Builder', 74, 15, 'New York')
    ... ])
    {'Alice Wonder': 'ali99wonder0sirap', 'Bob Builder': \
'bob15builder4kroy wen'}
    >>> postcards([
    ...     ('Ye West', 60, 47, 'Beverly Hills'),
    ... ])
    {'Ye West': 'ye47west0sllih ylreveb'}
    """
    price_limit = 75
    index = 3
    third_item_i = 2
    assert isinstance(info_list, list)
    assert all([isinstance(item[0], str) and isinstance(item[3], str) \
                for item in info_list])
    assert all([isinstance(item[1], int) and isinstance(item[2], int) \
                for item in info_list])
    assert all([item[1] >= 0 and item[2] >= 0 for item in info_list])
    return dict(list(map(lambda input: (input[0], \
        f"{input[0].split(' ')[0][0:index]}{str(input[third_item_i])}" \
        f"{input[0].split(' ')[1]}{str(input[1])[-1]}{input[index][::-1]}" \
        .lower()), list(filter( \
            lambda items: items[1] < price_limit, info_list)))))


# Question 5
def win_or_lose(lst, operations):
    """
    Performs the given operations below from the dictionary onto the given list
    and returns a new list with those operations performed on each item.

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]
    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']
    >>> operations_3 = [('advance', 10), ('tie', 100)]
    >>> win_or_lose(lst, operations_3)
    [133, 1244, 12355, 123466]
    >>> operations_4 = [('lost', 2), ('eliminate', 'Squad ')]
    >>> win_or_lose(lst, operations_4)
    ['Squad lost', 'Squad won', 'Squad won', 'Squad won', 'Squad won', \
'Squad won']
    >>> operations_5 = [('win', 'Final Score')]
    >>> win_or_lose(lst, operations_5)
    'Final Score'
    
    >>> lst = [10, 20, 30, 40, 50]
    >>> operations_6 = [('advance', 10), ('lost', 5)]
    >>> win_or_lose(lst, operations_6)
    [15, 25, 35, 45, 55]
    
    >>> lst = [100, 200, 300, 400, 500]
    >>> operations_7 = [('tie', 250), ('eliminate', 'Champion ')]
    >>> win_or_lose(lst, operations_7)
    ['Champion won', 'Champion won', 'Champion won']
    """
    commands = {
        'advance': lambda lst, amount: \
            list(map(lambda x: x + amount, lst)), \
        'lost': lambda lst, amount: list(map(lambda x: x - amount, lst)), \
        'tie': lambda lst, threshold: \
            list(filter(lambda x: x >= threshold, lst)), \
        'eliminate':  lambda lst, symbol: \
            list(map(lambda x: symbol + ('won' if x > 0 else 'lost'), lst)), \
        'win': lambda lst, message: message
    }
    assert isinstance(lst, list)
    assert isinstance(operations, list)
    assert all([isinstance(item, tuple) for item in operations])
    updated_lst = lst
    for action in operations:
        if action[0] == 'win':
            return commands[action[0]](updated_lst, action[1])
        updated_lst = commands[action[0]](updated_lst, action[1])
    return updated_lst
