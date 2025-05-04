class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.rented_by = None

    def rent(self, customer):
        if self.rented_by is None:
            self.rented_by = customer
            return "You rented the movie"
        return "Movie already rented"

    def return_movie(self, customer):
        if self.rented_by == customer:
            self.rented_by = None
            return "You returned the movie"
        elif self.rented_by is None:
            return "Movie is not rented"
        else:
            return "Movie was rented by someone else"
