import streamlit as st
import src.helpers.setup_database as db

# --- CONFIG ---
st.set_page_config()
db.initialize_db()

if "username" not in st.session_state:
    st.session_state.username = ""

if "full_name" not in st.session_state:
    st.session_state.full_name = ""

if "admin" not in st.session_state:
    st.session_state.admin = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "login_text" not in st.session_state:
    st.session_state.login_text = "Log In"


sidebar_logo = "src/images/redesign.png"
main_body_logo = "src/images/redesign_small.png"

st.logo(sidebar_logo, icon_image=main_body_logo, size="large")

# --- HOME ---
home_page = st.Page("src/pages/home.py", title="Home", icon=":material/home:")
account_page = st.Page("src/pages/login.py", title=st.session_state.login_text, icon=":material/login:")
jobs_page = st.Page("src/pages/jobs.py", title="Jobs", icon=":material/business_center:")

# --- ABOUT (SCLA) ---
about_page = st.Page(
    "src/pages/about/about.py", title="About SCLA", icon=":material/info:"
)
join_page = st.Page(
    "src/pages/about/join.py", title="Join SCLA", icon=":material/person_add:"
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
meetings_page = st.Page(
    "src/pages/about/meetings.py",
    title="Meetings",
    icon=":material/meeting_room:"
)
libraries_journal_page = st.Page(
    "src/pages/about/libraries_journal.py",
    title="Libraries Journal",
    icon=":material/book_5:"
)
contact_page = st.Page(
    "src/pages/about/contact.py",
    title="Contact Us",
    icon=":material/contact_support:"
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

# --- GET INVOLVED ---
awards_page = st.Page(
    "src/pages/get_involved/awards.py",
    title="Awards",
    icon=":material/editor_choice:"
)
volunteer_page = st.Page(
    "src/pages/get_involved/volunteer.py",
    title="Volunteer",
    icon=":material/hand_gesture:"
)

pages = {
    "": [home_page, account_page, jobs_page],
    "SCLA": [about_page, join_page, history_of_the_association_page, executive_officers_page, meetings_page, libraries_journal_page, contact_page],
    "Organization": [
        about_org_page,
        sections_page,
        round_tables_page,
        committees_page,
    ],
    "Get Involved": [awards_page, volunteer_page],
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
