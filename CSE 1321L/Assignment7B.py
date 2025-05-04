# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Assignment: 07

from Movie_class import Movie
from Customer_class import Customer

movie1 = Movie("Inception", "Christopher Nolan")
customer1 = Customer("Ethan")

# Scenario 1
print(customer1.rent_movie(movie1))
# Scenario 2
print(customer1.rent_movie(movie1))
# Scenario 3
print(customer1.return_movie(movie1))
# Scenario 4
print(customer1.return_movie(movie1))
# Scenario 5
customer2 = Customer("Olivia")
print(customer2.rent_movie(movie1))
# Scenario 6
movie2 = Movie("The Matrix", "Wachowskis")
movie3 = Movie("Interstellar", "Christopher Nolan")

print(customer1.rent_movie(movie2))
print(customer1.rent_movie(movie3))

movie4 = Movie("Avatar", "James Cameron")
print(customer1.rent_movie(movie4))
