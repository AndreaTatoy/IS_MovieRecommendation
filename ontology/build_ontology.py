from owlready2 import *

def build_ontology():
    onto = get_ontology("http://tatoy-lacorte-project/movies.owl")

    with onto:
        class Movie(Thing): pass
        class Genre(Thing): pass
        class Actor(Thing): pass
        class Theme(Thing): pass

        class has_genre(ObjectProperty): domain = [Movie]; range = [Genre]
        class has_actor(ObjectProperty): domain = [Movie]; range = [Actor]
        class has_theme(ObjectProperty): domain = [Movie]; range = [Theme]
        class Year(DataProperty, FunctionalProperty): domain = [Movie]; range = [int]
        class Rating(DataProperty, FunctionalProperty): domain = [Movie]; range = [float]

    onto.save(file="ontology/movies.owl")
    print("Ontology created and saved.")

if __name__ == "__main__":
    build_ontology()