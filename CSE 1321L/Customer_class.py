class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie in self.rented_movies:
            return "Movie already rented by this customer"
        if len(self.rented_movies) >= 2:
            return "Rental limit reached"
        if movie.rented_by is not None and movie.rented_by != self:
            return "Movie already rented by someone else"
        result = movie.rent(self)
        if result == "You rented the movie":
            self.rented_movies.append(movie)
            return "Movie rented successfully"
        return result

    def return_movie(self, movie):
        if movie not in self.rented_movies:
            return "Movie not rented by this customer"
        result = movie.return_movie(self)
        if result == "You returned the movie":
            self.rented_movies.remove(movie)
            return "Movie returned successfully"
        return result
