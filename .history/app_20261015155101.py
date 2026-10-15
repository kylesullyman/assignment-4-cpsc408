# imports
from helper import helper
from db_operations import db_operations

# global variables
db_ops = db_operations("playlist.db")


# functions
def startScreen():
    print("Welcome to your playlist!")
    # Create table if it doesn't exist
    if not db_ops.does_table_exist("songs"):
        db_ops.create_songs_table()
    # Populate table from CSV (only inserts if table is empty)
    db_ops.populate_songs_table("songs.csv")


# show user menu options
def options():
    print("""Select from the following menu options: 
    1. Find songs by artist
    2. Find songs by genre
    3. Find songs by feature
    4. Exit""")
    return helper.get_choice([1, 2, 3, 4])


# search for songs by artist
def search_by_artist():
    # get list of all artists in table
    query = """
    SELECT DISTINCT ARTIST from songs;
"""
    artists = db_ops.single_attribute(query)

    # show all artists, create dictionary of options, and let user choose
    choices = {}
    for i in range(len(artists)):
        print(i, artists[i])
        choices[i] = artists[i]

    choice = helper.get_choice(choices.keys())

    # user can ask to see 1, 5, or all songs
    print("How many results per artist? (1, 5, all?)")
    num = helper.get_choice([1, 5, 0])

    # choices['artists']=artists[choice]

    # print results
    song_query = """
    SELECT Name from songs
    WHERE Artist = :artist
    """

    params = {"artist": choices[choice]}
    if num:
        song_query += " LIMIT :num"
        params["num"] = num

    results = db_ops.select_query_params(song_query, params)
    helper.pretty_print(results)

    pass


# search songs by genre
def search_by_genre():
    # get list of genres
    genre_query = '''
    SELECT DISTINCT Genre
    FROM songs;
    '''

    print("Available genres: ")
    genres = db_ops.select_query(genre_query)

    # show genres in table and create dictionary
    choices = {}
    for i in range(len(genres)):
        print(i, genres[i])
        choices[i] = genres[i]

    index = helper.get_choice(choices.keys())

    if num:
        song_query += " LIMIT :num"
        params["num"] = num

    results = db_ops.select_query_params(song_query, params)
    helper.pretty_print(results)

    # user can ask to see 1, 5, or all songs
    print("How many songs? (1, 5, 0=All")
    num = helper.get_choice([1, 5, 0])

    song_query = '''
    SELECT name FROM songs
    WHERE Genre =:genre ORDER BY RANDOM()    
    '''
    params = {"genre": genres[index]}

    # print results
    pass


# search songs table by features
def search_by_feature():
    # features we want to search by

    # show features in table and create dictionary

    # user can ask to see 1, 5, or all songs

    # what order does the user want this returned in?

    # print results
    pass


if __name__ == "__main__":
    # main method
    startScreen()

    # program loop
    while True:
        user_choice = options()
        if user_choice == 1:
            search_by_artist()
        if user_choice == 2:
            search_by_genre()
        if user_choice == 3:
            search_by_feature()
        if user_choice == 4:
            print("Goodbye!")
            break

    db_ops.destructor()
