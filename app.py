import os
import streamlit as st
from owlready2 import get_ontology
from ontology.query_ontology import (
    find_by_actor, find_by_genre, find_by_theme, visualize_ontology_graph
)
import streamlit.components.v1 as components

def lower_name(name: str) -> str:
    return name.strip().replace(" ", "_").lower()

st.set_page_config(page_title="🎬 Movie Recommender Using Ontology", layout="centered")

st.title("🎥 Movie Recommendations")
st.markdown("Get recommendations based on **actors**, **genres**, or **themes**!")

search_type = st.selectbox("Search by:", ["Actor", "Genre", "Theme"])
query = st.text_input(f"Enter {search_type.lower()} name:")

if query:
    with st.spinner("Searching..."):
        if search_type == "Actor":
            results = find_by_actor(query)
        elif search_type == "Genre":
            results = find_by_genre(query)
        else:
            results = find_by_theme(query)

    if results:
        st.success(f"Found {len(results)} result(s):")
        for m in results:
            st.write(f"🎬 {m.name.replace('_', ' ')}")
    else:
        st.warning("No results found.")

# Ontology visualization toggle
if st.checkbox("👁️ Visualize Ontology"):
    onto = get_ontology("ontology/movies.owl").load()
    graph_path = "ontology_graph.html"
    visualize_ontology_graph(onto, graph_path)
    with open(graph_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=600, scrolling=True)
