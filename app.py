import streamlit as st
from ontology.query_ontology import find_by_actor, find_by_genre, find_by_theme

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

    # st.write(f"Query: {query}")
    # st.write(f"Results count: {len(results)}")

    if results:
        st.success(f"Found {len(results)} result(s):")
        for m in results:
            st.write(f"🎬 {m.name.replace('_', ' ')}")
    else:
        st.warning("No results found.")