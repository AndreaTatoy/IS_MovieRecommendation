from owlready2 import get_ontology

def normalize_name(name: str) -> str:
    return name.strip().replace(" ", "_").lower()

def find_by_genre(genre_name: str):
    onto = get_ontology("ontology/movies.owl").load()
    normalized_query = normalize_name(genre_name)

    genre = None
    for g in onto.Genre.instances():
        if normalize_name(g.name) == normalized_query:
            genre = g
            break

    if not genre:
        return []

    return [movie for movie in onto.Movie.instances() if genre in movie.has_genre]

def find_by_actor(actor_name: str):
    onto = get_ontology("ontology/movies.owl").load()
    normalized_query = normalize_name(actor_name)

    actor = None
    for a in onto.Actor.instances():
        if normalize_name(a.name) == normalized_query:
            actor = a
            break

    if not actor:
        return []

    return [movie for movie in onto.Movie.instances() if actor in movie.has_actor]

def find_by_theme(theme_name: str):
    onto = get_ontology("ontology/movies.owl").load()
    normalized_query = normalize_name(theme_name)

    theme = None
    for t in onto.Theme.instances():
        if normalize_name(t.name) == normalized_query:
            theme = t
            break

    if not theme:
        return []

    return [movie for movie in onto.Movie.instances() if theme in movie.has_theme]

from pyvis.network import Network
import os

def visualize_ontology_graph(onto, output_path="ontology_graph.html"):
    net = Network(height="600px", width="100%", directed=True)
    
    for movie in onto.Movie.instances():
        movie_name = movie.name.replace("_", " ")
        net.add_node(movie_name, label=movie_name, shape="box", color="orange")

        # Add and link genres
        for genre in movie.has_genre:
            genre_name = genre.name
            net.add_node(genre_name, label=genre_name, color="lightblue")
            net.add_edge(movie_name, genre_name, label="genre")

        # Add and link actors
        for actor in movie.has_actor:
            actor_name = actor.name
            net.add_node(actor_name, label=actor_name, color="lightgreen")
            net.add_edge(movie_name, actor_name, label="actor")

        # Add and link themes
        for theme in movie.has_theme:
            theme_name = theme.name
            net.add_node(theme_name, label=theme_name, color="lightpink")
            net.add_edge(movie_name, theme_name, label="theme")

    net.save_graph(output_path)