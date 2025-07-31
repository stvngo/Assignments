"""
DSC 20 Winter 2025 Homework 07
Name: Steven Ngo
PID: A18461865
Source: Lecture Slides
"""

# Question 1
def type_with_number(message):
    """
    Creates a sequence of digits as a string based on each character in 
    the given message string.

    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add at least 3 doctests below here #
    >>> type_with_number('HELLO WORLD')
    '43556096753'
    >>> type_with_number('StEvEn,')
    '7838361'
    >>> type_with_number('...Where am I?')
    '11194373026041'
    """
    if len(message) == 0:
        return ''
    first_char = message[0].lower()
    if first_char in ',.?!':
        return '1' + type_with_number(message[1:])
    elif first_char in 'abc':
        return '2' + type_with_number(message[1:])
    elif first_char in 'def':
        return '3' + type_with_number(message[1:])
    elif first_char in 'ghi':
        return '4' + type_with_number(message[1:])
    elif first_char in 'jkl':
        return '5' + type_with_number(message[1:])
    elif first_char in 'mno':
        return '6' + type_with_number(message[1:])
    elif first_char in 'pqrs':
        return '7' + type_with_number(message[1:])
    elif first_char in 'tuv':
        return '8' + type_with_number(message[1:])
    elif first_char in 'wxyz':
        return '9' + type_with_number(message[1:])
    elif first_char == ' ':
        return '0' + type_with_number(message[1:])
        

# Question 2
def make_palindrome(start, stop):
    """
    Recursively creates a palindrome using the given a starting/ending integer
    and a center integer that the palindrome 'moves towards and away from'.

    >>> make_palindrome(1, 1)
    '1'
    >>> make_palindrome(3, 5)
    '34543'
    >>> make_palindrome(5, 2)
    '5432345'

    # Add at least 3 doctests below here #
    >>> make_palindrome(8, 10)
    '891098'
    >>> make_palindrome(10, 13)
    '10111213121110'
    >>> make_palindrome(14, 12)
    '1413121314'
    """
    
    if start == stop:
            return str(stop)
    if start < stop:
        return str(start) + make_palindrome(start+1, stop) + str(start)
    elif start > stop:
        return str(start) + make_palindrome(start-1, stop) + str(start)


# Question 3
def doctests_q3():
    """
    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Spotify')
    'App installed'
    >>> my_phone.apps
    {'Spotify'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    >>> my_phone.install(1000, 'Spotify')
    'App already installed'

    # Add your own doctests below

    >>> phone2 = Phone('Samsung', 5000, 128000)
    >>> phone2.use(100)
    >>> phone2.charge
    1700
    >>> phone2.recharge(100)
    >>> phone2.charge
    3700
    >>> phone2.install(64000, 'Netflix')
    'App installed'
    >>> phone2.install(70000, 'YouTube')
    'Not enough storage'
    
    >>> phone3 = Phone('OnePlus', 4500, 256000)
    >>> phone3.use(50)
    >>> phone3.charge
    1650
    >>> phone3.install(50000, 'Instagram')
    'App installed'
    >>> phone3.install(50000, 'Instagram')
    'App already installed'
    
    >>> phone4 = Phone('Google', 4800, 200000)
    >>> phone4.use(170)
    'Out of charge'
    >>> phone4.charge
    0
    >>> phone4.recharge(50)
    >>> phone4.charge
    1000
    >>> phone4.recharge(191)
    >>> phone4.charge
    4800
    >>> phone4.install(100000, 'Google Maps')
    'App installed'
    >>> phone4.install(150000, 'Gmail')
    'Not enough storage'
    >>> phone4.install(100000, 'YouTube')
    'App installed'
    >>> phone4.storage
    0
    >>> phone4.install(1000, 'LinkedIn')
    'Not enough storage'
    >>> phone4.num_apps
    2
    """
    return

class Phone:
    """
    Implementation of Phone
    """
    def __init__(self, brand, max_battery, max_storage):
        """
        Initializes the instance attributes of the phone.
        Instance Attributes:
        brand (str): brand of the phone
        max_battery (int): maximum battery capacity 
        storage (int): maximum storage capacity
        charge (int): initial charge of the phone, half of the maximum charge
        charge_rate (int): how much the phone charges per minute when charging
        num_apps (int): number of apps on the phone
        apps (set): set of the names of the apps installed
        drain_rate (int): how much the charge of the phone uses per minute
        """
        self.brand = brand
        self.max_battery = max_battery
        self.storage = max_storage
        self.charge = max_battery // 2
        if brand == 'Apple':
            self.drain_rate = 10
        elif brand == 'OnePlus':
            self.drain_rate = 12
        elif brand == 'Samsung':
            self.drain_rate = 8
        else:
            self.drain_rate = 15
        self.charge_rate = 20
        self.num_apps = 0
        self.apps = set()
    
    def use(self, minutes):
        """
        Updates the phone's charge based on how many minutes it is used and 
        what the phone's drain_rate is.
        """
        self.charge -= self.drain_rate * minutes
        if self.charge <= 0:
            self.charge = 0
            return "Out of charge"

    def recharge(self, minutes):
        """
        Updates the phone's charge based on how many minutes it is charged for
        and the charge rate of the phone.
        """
        self.charge += self.charge_rate * minutes
        if self.charge >= self.max_battery:
            self.charge = self.max_battery

    def install(self, app_size, app_name):
        """
        Installs an app with the given app name and app_size, updating the 
        number of apps installed and the apps on the phone, based on the amount
        of storage available on the phone.
        """
        if self.charge == 0:
            return "Out of charge"
        if (self.storage - app_size) < 0:
            return "Not enough storage"
        if app_name in self.apps:
            return "App already installed"
        self.apps.add(app_name)
        self.num_apps += 1
        self.storage -= app_size
        return "App installed"


################ CLASS PART ##################

# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    #new doctests below
    >>> new_track1 = Song('Blinding Lights', 3.20, 'After Hours', 'The Weeknd', 300000000)
    >>> new_track2 = Song('Levitating', 3.23, 'Future Nostalgia', 'Dua Lipa', 450000000)
    >>> new_track3 = Song('Peaches', 3.18, 'Justice', 'Justin Bieber', 200000000)
    >>> new_track4 = Song('Shake It Off', 4.02, '1989', 'Taylor Swift', 1500000000)
    >>> print(new_track1)
    'Blinding Lights' by The Weeknd on 'After Hours' is 3.2 minutes long with 300000000 streams
    >>> print(new_track2)
    'Levitating' by Dua Lipa on 'Future Nostalgia' is 3.23 minutes long with 450000000 streams
    >>> print(new_track3)
    'Peaches' by Justin Bieber on 'Justice' is 3.18 minutes long with 200000000 streams
    >>> print(new_track4)
    'Shake It Off' by Taylor Swift on '1989' is 4.02 minutes long with 1500000000 streams

    >>> new_playlist1 = Playlist('Top Hits', 'Alice')
    >>> new_playlist2 = Playlist('Party Mix', 'Bob')
    >>> new_playlist3 = Playlist('Chill Vibes', 'Carol')
    >>> print(new_playlist1)
    Playlist 'Top Hits' by Alice has 0 songs
    >>> print(new_playlist2)
    Playlist 'Party Mix' by Bob has 0 songs
    >>> print(new_playlist3)
    Playlist 'Chill Vibes' by Carol has 0 songs

    >>> new_playlist1.add_song(new_track1)
    True
    >>> new_playlist1.add_song(new_track2)
    True
    >>> new_playlist1.add_song(new_track3)
    True
    >>> new_playlist1.add_song(new_track1)
    False
    >>> new_playlist1.remove_song(new_track1)
    True
    >>> new_playlist1.remove_song(new_track2)
    True
    >>> new_playlist1.remove_song(new_track3)
    True
    >>> new_playlist1.remove_song(new_track3)
    False
    >>> new_track1.add_to_playlist(new_playlist1)
    True
    >>> new_track2.add_to_playlist(new_playlist1)
    True
    >>> new_playlist1.get_total_streams()
    750000000
    >>> new_playlist1.get_total_length()
    6.43
    >>> new_playlist1.get_most_played_song()
    'Levitating'
    >>> new_track3.add_to_playlist(new_playlist1)
    True
    >>> new_track2.add_to_playlist(new_playlist1)
    False
    >>> new_playlist1.get_total_streams()
    950000000
    >>> new_playlist1.get_total_length()
    9.61
    >>> new_playlist1.get_most_played_song()
    'Levitating'
    >>> new_playlist1.sort_songs('name')
    >>> [x.get_name() for x in new_playlist1.get_songs()]
    ['Blinding Lights', 'Levitating', 'Peaches']
    >>> new_playlist1.sort_songs('streams')
    >>> [x.get_name() for x in new_playlist1.get_songs()]
    ['Peaches', 'Blinding Lights', 'Levitating']
    >>> new_playlist1.sort_songs('length')
    >>> [x.get_name() for x in new_playlist1.get_songs()]
    ['Peaches', 'Blinding Lights', 'Levitating']
    >>> new_playlist1.sort_songs('artist')
    >>> [x.get_name() for x in new_playlist1.get_songs()]
    ['Levitating', 'Peaches', 'Blinding Lights']
    >>> new_track1.listen()
    "Listening to 'Blinding Lights' by The Weeknd"
    >>> new_track2.listen()
    "Listening to 'Levitating' by Dua Lipa"
    >>> new_track3.listen()
    "Listening to 'Peaches' by Justin Bieber"
    >>> new_playlist1.get_total_streams()
    950000003
    >>> print(new_playlist1.play())
    Listening to 'Levitating' by Dua Lipa
    Listening to 'Peaches' by Justin Bieber
    Listening to 'Blinding Lights' by The Weeknd
    >>> new_playlist2.add_song(new_track1)
    True
    >>> new_playlist2.add_song(new_track2)
    True
    >>> new_playlist1.combine_playlists(new_playlist2)
    2
    >>> new_track4.add_to_playlist(new_playlist3)
    True
    >>> new_playlist2.combine_playlists(new_playlist3)
    True
    >>> new_playlist1.combine_playlists(new_playlist2)
    2
    >>> new_playlist1.get_total_streams()
    2450000006
    >>> new_playlist1.get_total_length()
    13.629999999999999
    >>> print(new_playlist1.play())
    Listening to 'Levitating' by Dua Lipa
    Listening to 'Peaches' by Justin Bieber
    Listening to 'Blinding Lights' by The Weeknd
    Listening to 'Shake It Off' by Taylor Swift
    >>> new_playlist1.sort_songs('length')
    >>> [x.get_name() for x in new_playlist1.get_songs()]
    ['Peaches', 'Blinding Lights', 'Levitating', 'Shake It Off']
    >>> new_playlist3.remove_song(new_track1)
    False
    >>> new_playlist3.remove_song(new_track4)
    True
    >>> new_playlist3.sort_songs('artist')
    >>> [x.get_name() for x in new_playlist3.get_songs()]
    []
    >>> new_playlist3.play()
    'Empty'
    >>> new_playlist1.get_total_streams()
    2450000010
    >>> new_playlist3.combine_playlists(new_playlist1)
    True
    >>> new_playlist3.remove_song(new_track1)
    True
    >>> print(new_playlist3.play())
    Listening to 'Peaches' by Justin Bieber
    Listening to 'Levitating' by Dua Lipa
    Listening to 'Shake It Off' by Taylor Swift
    >>> new_playlist3.get_total_streams()
    2150000010

    #end of new doctests

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman', 'Ariana Grande', 56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US', 'Windaco God', 99999999)
    >>> BM = Song('Talking to the Moon', 3.38, 'Doo-Wops & Hooligans', 'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy', 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]

    """
    return


class Song:
    """
    Implementation of a song
    """

    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        assert isinstance(name, str) and len(name) > 0
        assert isinstance(length, float) and length > 0
        assert isinstance(album, str) and len(album) > 0
        assert isinstance(artist, str) and len(artist) > 0
        assert isinstance(streams, int) and streams >= 0
        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams


    def get_name(self):
        """ Getter for name attribute """
        return self.name


    def get_length(self):
        """ Getter for length attribute """
        return self.length


    def get_album(self):
        """ Getter for album attribute """
        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams


    def __str__(self):
        """
        String representation of Song
        """
        return f"'{self.name}' by {self.artist} on '{self.album}' is " \
            f"{self.length} minutes long with {self.streams} streams"


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return f"Listening to '{self.name}' by {self.artist}"


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(playlist, Playlist)
        return playlist.add_song(self)

# Question 5

class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        assert isinstance(title, str) and len(title) > 0
        assert isinstance(user, str) and len(user) > 0
        self.title = title
        self.user = user
        self.songs = []
        pass


    def get_title(self):
        """ Getter for title attribute """
        return self.title


    def get_user(self):
        """ Getter for user attribute """
        return self.user
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs


    def __str__(self):
        """
        String representation of Playlist
        """
        return f"Playlist '{self.title}' by {self.user} has " \
            f"{len(self.songs)} songs"


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)
        if any(s.get_name() == song.get_name() for s in self.songs):
            return False
        else:
            self.songs.append(song)
            return True


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song) 
        for s in self.songs:
            if s.get_name() == song.get_name():
                self.songs.remove(s)
                return True
        return False


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert isinstance(sort_by, str) and \
            sort_by in ['name', 'length', 'album', 'artist', 'streams']
        if sort_by == 'length':
            self.songs.sort(key=lambda song: song.get_length())
        elif sort_by == 'streams':
            self.songs.sort(key=lambda song: song.get_streams())
        elif sort_by == 'name':
            self.songs.sort(key=lambda song: song.get_name())
        elif sort_by == 'album':
            self.songs.sort(key=lambda song: song.get_album())
        elif sort_by == 'artist':
            self.songs.sort(key=lambda song: song.get_artist())


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.get_streams() for song in self.songs])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.get_length() for song in self.songs])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if len(self.songs) == 0:
            return "Empty"
        else:
            return "".join([f"{song.listen()}\n" \
                            for song in self.songs]).strip()
    

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)
        assert all([isinstance(song, Song) \
                    for song in other_playlist.get_songs()])
        num_of_fails = sum([1 if song in self.songs else 0 \
                            for song in other_playlist.get_songs()])
        add_songs = [self.add_song(song) \
                     for song in other_playlist.get_songs()]
        if all(add_songs):
            return True
        else:
            return num_of_fails
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        if len(self.songs) == 0:
            return ""
        most_played = max(self.songs, key=lambda song: song.get_streams())
        return most_played.get_name()