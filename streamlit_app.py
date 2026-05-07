import streamlit as st
import src.helpers.setup_database as db

# --- CONFIG ---
st.set_page_config()
db.initialize_db()

if "username" not in st.session_state:
    st.session_state.username = ""

if "admin" not in st.session_state:
    st.session_state.admin = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

sidebar_logo = "src/images/redesign.png"
main_body_logo = "src/images/redesign_small.png"

st.logo(sidebar_logo, icon_image=main_body_logo, size="large")

# --- HOME ---
home_page = st.Page("src/pages/home.py", title="Home", icon=":material/home:")
login_page = st.Page("src/pages/login.py", title="Login", icon=":material/login:")
join_page = st.Page(
    "src/pages/join.py", title="Join SCLA", icon=":material/person_add:"
)

# --- ABOUT (SCLA) ---
about_page = st.Page(
    "src/pages/about/about.py", title="About SCLA", icon=":material/info:"
)
history_of_the_association_page = st.Page(
    "src/pages/about/history_of_the_association.py",
    title="History of the Association",
    icon=":material/history_edu:",
)
executive_officers_page = st.Page(
    "src/pages/about/executive_officers.py",
    title="Executive Officers",
    icon=":material/work:",
)

# --- ORGANIZATION ---
about_org_page = st.Page(
    "src/pages/organization/about_organization.py",
    title="About the Organization",
    icon=":material/account_tree:",
)
sections_page = st.Page(
    "src/pages/organization/sections.py", title="Sections", icon=":material/groups:"
)
round_tables_page = st.Page(
    "src/pages/organization/round_tables.py",
    title="Round Tables",
    icon=":material/table_bar:",
)
committees_page = st.Page(
    "src/pages/organization/committees.py",
    title="Committees",
    icon=":material/diversity_2:",
)

pages = {
    "": [home_page, login_page, join_page],
    "SCLA": [about_page, history_of_the_association_page, executive_officers_page],
    "Organization": [
        about_org_page,
        sections_page,
        round_tables_page,
        committees_page,
    ],
}

# --- ADMIN ---
if st.session_state.admin:
    add_to_home_page = st.Page(
        "src/pages/admin/admin.py",
        title="Add to Home",
        icon=":material/shield_person:"
    )
    pages["Admin"] = [add_to_home_page]

pg = st.navigation(
    pages,
    position="top",
)

pg.run()
