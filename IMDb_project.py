import matplotlib.pyplot as plt
from imdb import IMDb

ia = IMDb()

#Get movie detail by input name
def get_movie_details(movie_title):
    # Initialize IMDb object
    ia = IMDb()

    # Search for the movie title
    search_results = ia.search_movie(movie_title)

    if search_results:
        # Get the first search result (the most relevant)
        movie = search_results[0]

        # Fetch full details for the movie
        ia.update(movie)

        # Print movie details
        print("Title:", movie.get('title', 'None'))
        print("Year:", movie.get('year', 'None'))
        print("Genres:", ', '.join(movie.get('genres', ['None'])))
        print("Plot:", movie.get('plot outline', 'None'))
        print("Rating:", movie.get('rating', 'None'))
        print("Directors:", ', '.join([director.get('name', 'None') for director in movie.get('directors', [])]))
        print("Cast:")
        for actor in movie.get('cast', [])[:10]:
            print(actor.get('name', 'None'))
    else:
        print("Movie not found.")

# Input the movie title
movie_title = input("Enter the movie title: ")

# Call the function to get movie details
get_movie_details(movie_title)
