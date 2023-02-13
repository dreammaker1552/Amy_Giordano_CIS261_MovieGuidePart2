def display_menu():
    print("The Movie List Program")
    print("Command Menu")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def read_movies_from_file(movies):
    with open("movies.txt.", "r") as file:
        for line in file:
            movies.append(line.strip())

def write_movies_to_file(movies):
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_movies(movies):
    print("The list of movies:")
    for i, movie in enumerate(movies):
        print(f"{i + 1}. {movie}")

def add_movie(movies):
    movie = input("Enter a movie: ")
    movies.append(movie)
    write_movies_to_file(movies)
    print(f"{movie} was added to the list.")

def delete_movie(movies):
    number = int(input("Enter the number of the movie to delete: "))
    if number < 1 or number > len(movies):
        print("Invalid movie number.")
    else:
        movie = movies.pop(number - 1)
        write_movies_to_file(movies)
        print(f"{movie} was deleted from the list.")

def main():
    movies = []
    read_movies_from_file(movies)

    while True:
        display_menu()
        command = input("Enter command: ")
        if command == "list":
            display_movies(movies)
        elif command == "add":
            add_movie(movies)
            display_movies(movies)
        elif command == "del":
            delete_movie(movies)
            display_movies(movies)
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
