import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movies = ["The Departed", "The Shining", "Toy Story", "Children of Men", "The Road"]

        # TODO: randomly choose one of the movies, and return it
        from random import randrange
        random_index = randrange(0, len(movies))
        random_movie = movies[random_index]

        #return "The Big Lebowski"
        return random_movie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        tom_movie = self.getRandomMovie()

        tom_content = "<h1>Tomorrow's Movie</h1>"
        tom_content += "<p>" + tom_movie + "</p>"

        self.response.write(content)
        self.response.write(tom_content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
