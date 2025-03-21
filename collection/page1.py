#https://st-pages.streamlit.app/ reference from this person
from st_pages import add_page_title, get_nav_from_toml
import streamlit as st

# Set the layout to wide for a better view
st.set_page_config(layout="wide")

# Toggle to show sections in the sidebar (if needed)
#sections = st.sidebar.toggle("Sections", value=True,# key="use_sections")

# Choose the TOML file based on the toggle
nav = get_nav_from_toml(".streamlit/sidebar.toml")

# Display your logo (adjust the path if necessary)
st.logo("naruto1.jpg")

# Initialize navigation using the st_pages library
pg = st.navigation(nav)

# Add a title to the page based on the navigation selection
add_page_title(pg)

# Run the selected page
pg.run()
