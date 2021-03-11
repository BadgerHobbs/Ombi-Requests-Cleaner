import sqlite3
import time

try:
    # Get all movies currently within plex
    conn = sqlite3.connect('ombi/OmbiExternal.db')
    cur = conn.cursor()
    cur.execute('SELECT TheMovieDbId from PlexServerContent')
    plexRecords = cur.fetchall()
    conn.close()

    # Get all requested movies currently within ombi
    conn = sqlite3.connect('ombi/Ombi.db')
    cur = conn.cursor()
    cur.execute('SELECT TheMovieDbId from MovieRequests WHERE MarkedAsAvailable NOT NULL')
    ombiRecords = cur.fetchall()
    conn.close()

    plexMovies = []

    # Get and clean all movies in plex
    for plexRecord in plexRecords:

        plexMovies.append(str(plexRecord[0]))

    ombiMovies = []

    # Get and clean all movie requests in ombi
    for ombiRecord in ombiRecords:

        ombiMovies.append(str(ombiRecord[0]))

    moviesToRemove = []

    # Go through all movie requests in ombi and add to list to remove if not in plex
    for ombiMovie in ombiMovies:

        if ombiMovie not in plexMovies:

            moviesToRemove.append(str(ombiMovie))

    print("Checking",len(moviesToRemove),"Movie Requests!")

    conn = sqlite3.connect('ombi/Ombi.db')
    cur = conn.cursor()

    # If movie is requested in ombi and marked as availible but not on plex (ie deleted), remove the request
    for movie in moviesToRemove:

        if movie.strip() != "":

            sqlString = 'DELETE from MovieRequests WHERE MarkedAsAvailable NOT NULL AND TheMovieDbId = ' + movie
            cur.execute(sqlString)
            conn.commit()

    conn.close()

    print("Ombi Requests Updated to Match Plex!")
    '''

    conn = sqlite3.connect('ombi/OmbiExternal.db')

    cur = conn.cursor()
    cur.execute('DELETE from PlexServerContent')

    conn.commit()
    conn.close()

    print("Ombi Plex Cache Cleared in DB!")
    '''

except Exception as e:
    print(e)
    pass

# time.sleep(seconds)
