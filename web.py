import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page = "pages/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,

)

project_page = st.Page(
    page = "pages/projects.py",
    title = "Projects",
    icon = ":material/code_blocks:",

)

# --- NAVIGATION CONTENT ---
pg = st.navigation(
    {
    "Info": [about_page],
    "Projects": [project_page],
    }
)

# --- SHARED ON ALL PAGES ---
# st.logo("")
st.sidebar.text("Made by Sparrowium")

# --- RUN NAVIGATION ---
pg.run()
