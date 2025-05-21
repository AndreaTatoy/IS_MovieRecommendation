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