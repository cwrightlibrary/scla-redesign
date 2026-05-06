import pandas as pd
import streamlit as st

st.markdown(
    """
    <style>
        /* Only apply these rules to screens wider than 768px (Desktops/Laptops) */
        @media (min-width: 768px) {
            /* Make the main content area wider */
            .block-container {
                max-width: 70%;
                padding-top: 2rem;
            }

            /* Make the Sidebar Logo larger */
            [data-testid="stSidebarHeader"] img {
                max-height: 100px;
                width: auto;
            }
        }
        
        /* Optional: CSS for all screens (Headers) */
        @import url('https://fonts.googleapis.com/css2?family=Darumadrop+One&display=swap');
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Darumadrop One', cursive;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Executive officers")

officers_table = [
    ("Jana Stevenson", "President", "sclapresident2025@gmail.com"),
    (
        "Sonaite Debebe-Kumssa",
        "1st Vice President/Conference Chair",
        "sclafirstvp@gmail.com",
    ),
    ("Amanda Myers", "2nd Vice President/Membership Chair", "secondvpscla@gmail.com"),
    ("Valerie Byrd Fort", "Secretary", "valeriebyrdfort@gmail.com"),
    ("Dr. April Williams", "Treasurer", "aprilwilliams@lancastercountysc.gov"),
    ("Kelly Jones", "Immediate Past President", None),
]
reps_table = [
    (
        "Tracey Elvis-Weitzel",
        "South Carolina Association of Public Library Administrators Liason",
        "elvist@horrycountysc.gov",
    ),
    (
        "Virginia Cononie",
        "South Carolina Association of School Librarians Liason",
        None,
    ),
    (
        "Amber Conger",
        "Southeastern Library Association Liason",
        "aconger@lexcolibrary.org",
    ),
]

officers_df = pd.DataFrame(officers_table, columns=["Name", "Title", "Email"])
reps_df = pd.DataFrame(reps_table, columns=["Name", "Title", "Email"])

with st.container(border=True):
    st.header("2026 Executive Officers")
    st.table(officers_df, border="horizontal")

with st.container(border=True):
    st.header("American Library Association Councilor")
    st.write("Sarah Schroeder")

with st.container(border=True):
    st.header("Executive Director")
    st.write(
        "Courtney Waldrup\n\nPremier Management Partners\n\n1 Windsor Cove, Suite 305\n\nColumbia, SC 29223\n\ncwaldrup@pmpamc.com"
    )

with st.container(border=True):
    st.header("2025 Association Representatives")
    st.table(reps_df, border="horizontal")
