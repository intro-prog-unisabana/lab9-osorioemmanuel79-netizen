# Write your code here!
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"


def main():
    title = input("Enter the movie title: ")
    director = input("Enter the director: ")
    year = input("Enter the year: ")

    movie = Movie(title, director, year)
    print(movie)


if __name__ == "__main__":
    main()