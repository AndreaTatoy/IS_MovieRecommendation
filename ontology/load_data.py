from owlready2 import get_ontology
import pandas as pd

def load_movies(csv_path="data/movies.csv"):
    onto = get_ontology("ontology/movies.owl").load()
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        title = row["Title"].replace(" ", "_")
        genre = onto.search_one(iri="*" + row["Genre"]) or onto.Genre(row["Genre"])
        actor = onto.search_one(iri="*" + row["Actor"].replace(" ", "_")) or onto.Actor(row["Actor"].replace(" ", "_"))
        theme = onto.search_one(iri="*" + row["Theme"]) or onto.Theme(row["Theme"])

        movie = onto.Movie(title)
        movie.has_genre.append(genre)
        movie.has_actor.append(actor)
        movie.has_theme.append(theme)
        movie.Year = int(row["Year"])
        movie.Rating = float(row["Rating"])

    onto.save(file="ontology/movies.owl")
    print("Data loaded and ontology updated.")

    for movie in onto.Movie.instances():
        print(movie.name, movie.has_genre, movie.has_actor, movie.has_theme, movie.Year, movie.Rating)


if __name__ == "__main__":
    load_movies()
